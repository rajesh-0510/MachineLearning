# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 16:34:49 2018

@author: Rajesh Arumugam
"""
# used cx_oracle library
# https://pypi.python.org/pypi/cx_Oracle
# Connect to Oracle DB,retrive data and create csv file

import cx_Oracle
import pandas as pd

# DB connection Details
USERNAME = 'username'
PASSWORD = 'password'
IP = "ipaddress"
PORT = "1521"
service_name="DBSERVICENAME" 

# Function in retrive the Values
def dbquery(query):
    # Create Connection using CX_Oracle
    dsn_tns = cx_Oracle.makedsn(IP, PORT, service_name=service_name)
    connection = cx_Oracle.connect(USERNAME, PASSWORD, dsn_tns)
    # Use connection, retrive the data using Pandas read_sql_query and save it in the dataframe (df)
    with connection:
            try:
                df = pd.read_sql_query(query,connection)
            except cx_Oracle.DatabaseError as dberror:
                print(dberror)
    return df    
    
def Validate():
    # Enter the Query
    JenkinsidQuery="""select  * from table_name"""
    # Call dbquery function to retrive the data
    sqlreturnvaluedf=dbquery(JenkinsidQuery)
    #Fill NA for empty columns in each row
    query_by_Jenkinsid=sqlreturnvaluedf.fillna('NA')
    #Generate CSV File
    query_by_Jenkinsid.to_csv('SampleFileName.csv')

# Call the Validate method    
Validate()
