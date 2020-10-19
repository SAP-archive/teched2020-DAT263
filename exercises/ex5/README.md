# Exercise 4: Sending Device Data via RestAPI

## Description
In this exercise we create a RestAPI that could be called by devices to save the performance data to a file. That could be the very beginning of the whole use case: 
1. Devices are sending data to SAP Data Intelligence
2. Data is stored to HANA database
3. Quality assurance test verifies if the data is within the expected boundaries.
4. All failed data are recorded to a "QMTICKET" table to rectify the data or resolve any issues with devices
5. Further analysis by a data scientist could develop more sophisticated quality checks and create and even better prediction on failed data


## Exercise Summary

Creating a Pipeline with a web-service that can be called externally and hands-over the data to an operator for some processing before calling an operator for saving the data. 

In order to test the Rest-API a client application is provided that generates example data and sends it to the web-service. 

## Exercise 4.1

## Summary

You have learnt an alternative way to read and write to a HANA database as with the "Structured Data Operators" of the previous exercise. We used the "Validation Rule" operator to do simple data quality checks and finally how to use a python custom operator to leverage all the options provided by an advanced script. 


