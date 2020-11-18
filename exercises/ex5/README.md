# Exercise 5: Sending Device Data via RestAPI

## Description
In this exercise we create a RestAPI that could be called by devices to save the performance data to a file. That could be the very beginning of the whole use case you just accomplished so far.  
1. Devices are sending data to SAP Data Intelligence
2. This data is written to a HANA database
3. Quality assurance test verifies if the data is within the expected boundaries.
4. All records which do not pass validation written to a `QMTICKET` table which will be used to correct the data or resolve any issues with the devices
5. Further analysis by a data scientist could develop more sophisticated quality checks and create and even better prediction on failed data


## Exercise Summary

In this exercise we will create a pipeline that will host an HTTP REST web service that can be called from an external application and hand over the data to an operator for further processing before calling an operator for saving the data.

In order to test the Rest-API a client web application is provided that can generate sample data and dispatch it to the web service. You can also of course also Postman or command line terminal (curl) to send the same request there.

## Exercise 5.1
Each running pipeline consumes a node in the cluster. Due to the limited size of our workshop-cluster we ask you kindly to ensure that the web-service pipeline is only running as short as possible. For testing purpose we write the web-service response to a file and then terminate the graph.

Creating the basic RestAPI:

1. Create new Graph
2. Add the RestAPI operator **OpenAPI Servlow** and the **Wiretap** opertorator
3. Configure the **OpenAPI Servlow** operator
	1.  Base Path: 'teched2020/\<di_user\>\_performance - This defines which service the Web-server calls.
	2. One-Way: True (operator is not waiting for a response but sends immediatedly HTTP 204 back.
4. Add the **Write File** operator and the **To File** converter
5. Configure the **Write File** operator:
	1. Connection: S3 - TechEd2020_S3
	2. Path mode: "Static (from configuration)
	3. Path: */output/\<di_user\>/logrestapi.csv* (this format is currently supported by Metadata explorer and the result can be viewed. Otherwise the file had to be downloaded first.)
6. Add the **Workflow Terminator** to the graph.
7. Connect all operators  

![restapi](./images/restapi1.png)


## Exercise 5.2
### HTML Test Page

The easiest way to interact with the web service hosted inside SAP Data Intelligence is using the external web based client that you can access at [sendcelldata.cfapps.eu10.hana.ondemand.com](sendcelldata.cfapps.eu10.hana.ondemand.com). Note that this is not a feature of SAP Data Intelligence and is provided for convenience at TechEd 2020.
![Test Page](./images/TestRestAPI.png)

Use the same username and password you used to log on to SAP Data Intelligence and enter the complete URL that the following format:

		https://<DI Hostname>/app.pipeline-modeler/openapi/service/teched2020/<USER_ID>_performance/test/

![Response Page](./images/ResponseTestRestAPI.png)

### Postman
#### Request URL

POST and url: \<url pipeline modeler\>/openapi/service/\<di_user\>\_performance/test

It is important to add a process-tag at the end, otherwise the request gets an error although the process tag is not used.

#### Request Header
In the "Headers"-tab add the parameter: X-Requested-With - XMLHttpRequest. Without this parameter you get the error: "Forbidden cross-site request"

![postman1](./images/postman1.png)

#### Authorization
1. Change the authorization TYPE: Basic Auth
2. Enter your credentials while adding before your user the tenant name 'default' separated with a backslash '\'.

![postman3](./images/postman3.png)

#### Request Body

In the body you can add the actual data that should be posted. Here we can add already a JSON that contains the data of the device:

{"TIMESTAMP":"2020-10-19 20:06:55","CELLID":1234512,"KEY1":111.1,"KEY2":222.2}

![postman2](./images/postman2.png)

#### Test

1. Now you can start the pipeline
2. When the pipeline is running send the postman request by pushing the "Send" button.
3. The received request is saved to the specified file and the pipeline terminates
4. Check the file.

### CURL
If you are not using postman you can send a command from a terminal. CURL is pre-installed on nearly all systems.

1. Open your terminal application and paste the following command to a text editor (recommended)

```
curl --location --request POST 'https://vsystem.ingress.dh-ia37o5zq.dhaas-live.shoot.live.k8s-hana.ondemand.com/app/pipeline-modeler/openapi/service/teched2020/performance/test' \
--header 'X-Requested-With: XMLHttpRequest' \
--header 'Authorization: Basic ZGVmYXVsdFx0ZWNoZWQyMDIwOlRlZDIzNDUh' \
--header 'Content-Type: text/plain' \
--data-raw '{"TIMESTAMP":"2020-10-19 20:06:55","CELLID":1234512,"KEY1":111.1,"KEY2":222.2}'
```

2. Change the url and the path to the service according to your system environment and settings.
3. Change the Authorization string after "Authorization: Basic" to the base64 encoded DI credentials provided with your credentials.
3. Maybe change the data in --data-raw
4. Start the RestAPI pipeline
5. When the pipeline is running, send the curl command
6. The received request is saved to the specified file and the pipeline terminates
7. Check the file.

### Python client

If you have a Python3.x installed on your local system then you could also use the script that you have downloaded from this GitHub repository together with the Jupyter Notebook: [scripts.zip](../../scripts.zip).

First you have to ensure that the url in the script is the right one. Open the script with a text editor and verify and adjust the url described in the section Postman/Request URL.

Start the RestAPI pipeline and wenn running then start the script in a terminal with:

```
python3 ./celldata.py --cellid 1234512 --user <di_user> --pwd <password>
```




## Exercise 5.3

In this exercise you will create `Python3` operator that processes the received data and sends it to `Write File` operator to append the data to the existing `performance.csv` file. A response is also created but not used for this use case.

1. Add a `Python3` operator to the existing pipeline and add the following ports
	|Type type|Name|Datatype|
	|----|----|--------|
	|Inport|input|Basic/message|
	|Output|output|Basic/message
	|Outport|response|Basic/message|

2. Place and connect the new `Python3` operator between the `Wiretap` operator and the `in` port of the `To File` operator.

3. Change the configuration of the `Write File` operator to write to the following path: */input/\<di_user_id\>/performance.csv*

3. Right click the `Python3` operator and open the script editor. This will open a new tab in the modeler. Delete any existing code and copy/paste the following code:

```
import json
import sys

def on_input(msg):

    #prepare for a response message
    attributes = {}
    for key in msg.attributes :
        # only copy the headers that won't interfer with the recieving operators
        if not "openapi.header" in key  or  key == "openapi.header.x-request-key" :
             attributes[key] = msg.attributes[key]

    # Send data to output and response
    # In case of a body with wrong format exceptions are caught to avoid a pipeline crash
    try :
        devdata = json.loads(msg.body)
        str_line = devdata['TIMESTAMP'] + ',' +  str(devdata['CELLID']) + ','+ str(devdata['KEY1'])  + ','  + str(devdata['KEY2']) + '\n'
        api.send("output", str_line)
        api.send("response",api.Message(attributes=attributes,body=msg.body))
    except ValueError as e:
        error_str = "Value Error: {}\n{}".format(e,msg.body)
        api.send("log",error_str)
        api.send("response",api.Message(attributes=attributes,body=error_str))
    except json.decoder.JSONDecodeError as e:
        error_str = "JSONDecodeError: {}\n{}".format(e,msg.body)
        api.send("log",error_str)
        api.send("response",api.Message(attributes=attributes,body=error_str))


api.set_port_callback("input", on_input)

```

![restapi2](./images/restapi2.png)

4. Close the script editor tab and save the pipeline.

5. Run the pipeline and use any method from exercise 5.2 to input data into the the HTTP web service

6. When the pipeline successfully terminates you can inspect your output data */input/\<di_user_id\>/performance.csv* using the Metadata Explorer

![Data Preview](./images/metadataExplorer.png)

## Summary

In this exerise you have learnt how to setup a HTTP web service hosted inside SAP Data Intelligence and how to send a POST HTTP request to this service and process the this input using a python3 operator before writing it to S3.
