# DAT263 - Create and Manage End-to-End Data Pipelines with SAP Data Intelligence

[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/teched2020-DAT263)](https://api.reuse.software/info/github.com/SAP-samples/teched2020-DAT263)

## Tutorial Description

This repository contains the material for the SAP TechEd 2020 workshop with Session ID - DAT263. This tutorial can be completed as part of an SAP guided workshop or on your own time by using your own SAP Data Intelligence instance.

## Overview

This session introduces participants to use the **SAP Data Intelligence Modeler** to create data pipelines. We try to touch as many aspects as possible within an interactive 2h workshop. We will follow a use case that is based on a customer request in the area of IoT and quality management. The background story is quite simple.

If you are doing these tutorials as part of a workshop then please follow the **2h tutorials**

If you are doing these tutorials on your own time then please follow the **3h tutorials** which includes two additional exercises: File concatenation and Jupyter Notebook analysis)

### Scenario description
 On a daily basis a customer receives the configured values of several IoT device that reflect what nominal value that the device should produce. We refer to this as the **configuration dataset**. Throughout the day actual performance values of each device is received, we refer to this dataset as the **performance dataset**. All datasets are stored as files in separate subdirectories in an object store e.g. an Amazon S3 bucket.

### Process
1. Append all configuration files and all performance files into corresponding single files and store them to another object store location. (3h tutorials only)

2. Merge the 2 resulting files into a HANA table by using projections, aggregation and joining.

3. Do a simple data validation and create for the failed data a quality management service ticket.

4. In order to improve the quality check a data scientist should be able to do an analysis of the IoT data to eventually develop an early alert schema (3h tutorials only).

5. The central device configuration and performance table should be exposed via a webservice to retrieve the device status from outside.

### Acquired Skills
After having done all the tasks you are familiar with the general concept of using operators in **SAP Data Intelligence Modeler**, how to read and ingest data to/from multiple data sources, and how to analyze this data using **Jupyter Notebook**


## Requirements

  * One of the following SAP Data Intelligence versions:
    * SAP Data Intelligence 3.1 On-premise edition, patch 0
    * SAP Data Intelligence 3.1 Trial Edition
    * SAP Data Intelligence Cloud Edition 2010 or newer
  * Chrome browser (Recommended)
  * **[Workshop participants only]** Login credentials to your SAP Data Intelligence Cloud instance
    * See [registration page](http://workshop_registration.cfapps.eu10.hana.ondemand.com/register/Thorsten).
  * **[Self-guided users only]** The following connections must be created in Connection Manager.
    * A cloud storage connection e.g S3 / GCS / WASB / ADL
    * A Smart Data Lake (SDL) connection
    * A HANA database connection

    *Note that above connections are already predefined in SAP Data Intelligence 3.1 Trial Edition*

## Video walkthrough at SAP HANA Academy

    If you do not have access to a instance of SAP Data Intelligence or want to review the tutorials then you can watch a video walkthrough on [SAP HANA Academy](https://www.youtube.com/playlist?list=PLkzo92owKnVyY89xEshp_cSQ0QF8EE927)
    
## Exercises

### 2h Workshop (Guided workshop tutorials)

- [Getting Started](exercises/2h/gettingstarted/)
- [Exercise 1 - Joining and writing workflow data to SAP HANA](exercises/2h/ex1/)
- [Exercise 2 - Running a simple data validation](exercises/2h/ex2/)
- [Exercise 3 - Create a RestAPI receiving data from devices (simulation)](exercises/2h/ex3/)

### 3h Workshop (Self-guided tutorials)

- [Getting Started (Self-guided)](exercises/3h/gettingstarted/)
- [Exercise 1 - Appending multiple source files to a single file](exercises/3h/ex1/)
- [Exercise 2 - Joining and writing workflow data to SAP HANA](exercises/3h/ex2/)
- [Exercise 3 - Running a simple data validation](exercises/3h/ex3/)
- [Exercise 4 - Analyse data with Jupyter Notebook](exercises/3h/ex4/)
- [Exercise 5 - Create a RestAPI receiving data from devices (simulation)](exercises/3h/ex5/)




## How to obtain support

Support for the content in this repository is available during the actual time of the online session for which this content has been designed. Otherwise, you may request support via the [Issues](../../issues) tab.

## License
Copyright (c) 2021 SAP SE or an SAP affiliate company. All rights reserved. This file is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
