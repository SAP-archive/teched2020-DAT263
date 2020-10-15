# Exercise 1: Appending multiple source files to a single file

In this exercise, you will use the Metadata Explorer to explorer and view a batch of files stored in an Amazon S3 bucket. Using the Pipeline Modeler you will read the entire of batch of files and consolidate them into a single csv file that will be used in a later exercise. 

  ![](/exercises/ex0/images/completedModel.png)

## Part 1: Preview the source data in Metadata Explorer

**Objective**: To better understand the data we will be working in the later sections of this exercise we will first preview the datasets using the Metadata Explorer.

1. Select the Metadata Explorer from the drop-down menu in the top-left of the screen.

  ![](/exercises/ex0/images/dropdown_metadataExplorer.png)

2. Click on **Browse Connections**

  ![](/exercises/ex0/images/browseConnections.png)

3. Select the ```device_performance``` directory. This directory contains all of the source .csv files we will be appending in the next section of this exercise.

  ![](/exercises/ex0/images/directory_device_performance.png)

4. Click on the **View Factsheet** button

  ![](/exercises/ex0/images/button_viewFactsheet.png)

5. Click on the **Data Preview** button. You should see that our source file contains four unlabelled columns: A timestamp, a device ID, and two columns describing the value of this device.

  ![](/exercises/ex0/images/button_dataPreview.png)

## Part 2: Building the pipeline

**Objective**: In the previous section you observed that the ```device_performance``` directory contains multiple small source csv files. In this section we will read the contents of these sources file and re-write them into a single output csv file.

1. Return to the  Modeler by using the dropdown menu in the upper left corner of your screen.
  ![](/exercises/ex0/images/dropdown_pipelineModeler.png)

2. Create a new graph by first selecting the `Graphs` tab (shown vertically) and then the **+** button.
  ![](/exercises/ex0/images/createGraph.png)


3. When creating a new graph the modeler should automatically switch to the `Operators` tab (shown vertically), if not then select it. Use the search field to find the `List Files` and drag drop it into the new graph.
  ![](/exercises/ex0/images/operator_listFiles.png)

4. The `List Files` operator takes a directory as an input or configurable parameter and outputs a list of all files and sub-directories in a given storage service such as Amazon S3 buckets. You can view more information about this operator by right clicking it and select `Open Documentation`.

  ![](/exercises/ex0/images/doc_listFiles.png)

5. Like many other operators the `List File` operator will by default read configuration parameters from its input node `dirRef` during runtime. However, in this exercise the parameters will be provided during design time:
  - Configure the `List Files` operator by right clicking and selecting `Open Configuration`
  - Set the list operation to occur only `Once`
  - Select the **pencil icon** to define which storage account to read from.

  ![](/exercises/ex0/images/configure_listFiles.png)

6. Set the **Configuration Type** to `Connection Management`  and **Connection ID** to `TechEd2020_S3`x and select **Save**
 ![](/exercises/ex0/images/s3_Connection.png)

7. Browse the connection by clicking on the **monitor icon** and select the path directory `/device_performance` and click **Save**

8. Now would be a great time to save your progress. Click on the **floppy disk** icon located in the toolbar at the top of the screen. Enter the name `FileCollection_TAxx` where xx is the ID assigned to you at the beginning of the workshop.

  ![](/exercises/ex0/images/saveGraph.png)

9. Use the search field to find the `Read File` operator. Drag and drop it into your graph. This operator reads the contents of files from various storage services.

  ![](/exercises/ex0/images/operator_readFile.png)

10. The file path to be read by the `Read File` operator can be provided either via its input node at runtime or configured at design time. In this exercise we will provide the path at runtime using the `List File` operator. Connect the output node `ref`  to the input node of the `Read Operator`

11. Use the search field to find the `Write File` operator.  Drag and drop it into your graph. The `Write File` operator writes any content that is provided to its input node as a file to various object store services. Connect the output node `file` to the input node of the `Write File` operator.

12. Like the `Read File` operator the `Write File` operator can be configured at runtime or design time. In this exercise we will provide the target directory at design time.
- Select **Path Mode** to `Static`
- Click on the **pencil button** to select the `TechEd2020_S3` connection.
- Set **Mode** to `Append`
- Since the file we want to write does not yet exist we cannot browse for the path. Instead manually enter the following path: `/input/performance.csv`
- *\[Optional\]* You can change the label of the `Write File` operator to `Append File`. This can be helpful for other users to understand what the pipeline is designed to do at a glance.
  ![](/exercises/ex0/images/configure_writeFile.png)

13. When the `Write File` operator has successfully written the last batch of data it will mark its last output with an attribute `lastBatch`. We can use this as a trigger to safely terminate the pipeline.
  - Use the search field to find the `Message Filter` operator, drag and drop it into your graph.
  - Connect the `file` output node to its input node
  - Because the output node is of different datatype than the input node you will be prompted select to conversion method: Choose `From File (com.sap.from.File)`

  ![](/exercises/ex0/images/operator_messageFilter.png)

  ![](/exercises/ex0/images/conversion_fromFile.png)

14. Right click the `Message Filter` operator, select the **Open Configuration** button, and then click the **penctil button** define which condition to filter for.

  ![](/exercises/ex0/images/configure_messageFilter.png)

15. Copy/paste the following json code snippet into the text editor and click **Save**
  ```
  {
  	"message.lastBatch": true
  }
  ```
  ![](/exercises/ex0/images/editProperty_messageFilter.png)


16. Use the search field to find the `Graph Terminator` operator. Drag and drop it into your graph. This operator will terminate the pipeline execution when receiving any input to its input node. Connect the output node of the `Message Filter` to the input node of the `Graph Terminator`.

  ![](/exercises/ex0/images/operator_graphTerminator.png)

  Since the `Message Operator` is filtering out all messages that do not contain the `lastBatch` attribute the graph will not be terminated until we are sure that the last batch was written by the  for the `Write File` operator.

17. Save the graph by clicking on the **floppy disk** icon located in the toolbar at the top of the screen.

  ![](/exercises/ex0/images/saveGraphAgain.png)

## Part 3: Executing the pipeline

Now that you've created a complete graph it is time to execute it and look at the output data.

1. To execute the pipeline click on the **play button** at the top of the screen. The pipeline will appear under the **Status** tab. It will first appear to be in status ``Pending`` and then after a few seconds ``Running``.

  ![](/exercises/ex0/images/runGraph.png)

2. If the pipeline did not run into any errors then the execution should reach the `Graph Terminator` operator and the status will eventually switch to status `Completed`.

  **Tip:** *If the pipeline terminates with an error you can click on the title of the failed graph to view a detailed error message.*

  ![](/exercises/ex0/images/deadGraph.png)

3. After the pipeline reaches status `Completed` return to the **Metdata Explorer** using the drop-down menu in the top left corner of the screen.

  ![](/exercises/ex0/images/goTometadataExplorer.png)

4. Click on **Browse Connections** and navigate to the `/input/` directory in the `TechEd2020_S3` connection.

5.  click on on the **View Factsheet** button on the `performance.csv` file

  ![](/exercises/ex0/images/performance_viewFactsheet.png)


6. Click on the **Data Preview** button. Observe that all of the individual files from the source directory have been appended into a single consolidated csv files. The file size should be approx 40kb.

  ![](/exercises/ex0/images/performance_dataPreview.png)

## Summary  

In this exercise you have consolidated a batch of csv files into a single csv file using the List, Read, and Write file operators. By using the Message Filter operator you were also able to gracefully terminate the pipeline when all files have been processed and written to S3. Finally, you were able to verify the correctness of your output using the Metadata Explorer.

[**Click here to move to the next exercise**](/exercises/ex1/README.md)  where you will learn to use the workflow operators to join and aggregate two csv files and store the result in a HANA database.
