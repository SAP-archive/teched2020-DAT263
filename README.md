# DAT263 - Create and Manage End-to-End Data Pipelines with SAP Data Intelligence

## Description

This repository contains the material for the SAP TechEd 2020 session called Session ID - DAT263. 

## Overview

This session introduces attendees to use the **SAP Data Intelligence Modeler** to create data pipelines. We try to touch as many aspects as possible within an interactive 2h workshop. We will follow a use case that is based on a customer request in the area of IoT and quality management. The background story is quite simple.

### Setup
 The customer gets on a daily basis the configuration of several devices that means the nominal value the device should produce. During the day additional files are received that contain the actual values of each device. All files are stored in an object store in a separate folder.

### Process
1. Append all configuration files and all performance files into corresponding single files and store them to another object store location.

2. Merge the 2 resulting files into a HANA table by using projections, aggregation and joining. 

3. Do a simple data validation and create for the failed data a quality management service ticket. 

4. In order to improve the quality check a data scientist should be able to do an analysis of the IoT data to eventually develope an early alert schema. 

5. The central device configuration and performance table should be exposed via a webservice to retrieve the device status from outside. 

### Aquired Skills
After having done all the tasks you are familiar with the general concept of **SAP Data Intelligence Modeler **


## Requirements

The requirements to follow the exercises in this repository are...

## Exercises

Provide the exercise content here directly in README.md using [markdown](https://guides.github.com/features/mastering-markdown/) and linking to the specific exercise pages, below is an example.

- [Getting Started](exercises/ex0/)
- [Exercise 1 - First Exercise Description](exercises/ex1/)
    - [Exercise 1.1 - Exercise 1 Sub Exercise 1 Description](exercises/ex1#exercise-11-sub-exercise-1-description)
    - [Exercise 1.2 - Exercise 1 Sub Exercise 2 Description](exercises/ex1#exercise-12-sub-exercise-2-description)
- [Exercise 2 - Second Exercise Description](exercises/ex2/)
    - [Exercise 2.1 - Exercise 2 Sub Exercise 1 Description](exercises/ex2#exercise-21-sub-exercise-1-description)
    - [Exercise 2.2 - Exercise 2 Sub Exercise 2 Description](exercises/ex2#exercise-22-sub-exercise-2-description)


**OR** Link to the PDF document stored in your github repo for example...

Start the exercises [here](exercises/myPDFDoc.pdf).
    
**OR** Link to the Tutorial Navigator for example...

Start the exercises [here](https://developers.sap.com/tutorials/abap-environment-trial-onboarding.html).

**IMPORTANT**

Your repo must contain the .reuse and LICENSES folder and the License section below. DO NOT REMOVE the section or folders/files. Also, remove all unused template assets(images, folders, etc) from the exercises folder. 

## How to obtain support

Support for the content in this repository is available during the actual time of the online session for which this content has been designed. Otherwise, you may request support via the [Issues](../../issues) tab.

## License
Copyright (c) 2020 SAP SE or an SAP affiliate company. All rights reserved. This file is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSES/Apache-2.0.txt) file.
