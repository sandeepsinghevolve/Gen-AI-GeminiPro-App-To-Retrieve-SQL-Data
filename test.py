# Agenda--->Converting Natural text to SQL query----query hit the database and retrive the data
# 1st create the custom prompt---then with the help of LLM model/Gemini Pro---
# Prompt will convert into SQL query--- and we will use this query to hit the database---
# And finally will get the response
# I will use local DB sqlite--- to get quick and hasseleless response
# Inserting some data by python programming

import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables


# Configuring Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide sql queries as response from natural language text
# Here prompt is used for like how Google gemini pro to behave
# Question is like natural langauage text, which i really want to convert into a sql query

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the sql database
# Connect to the database---then execute the query---retrieving the results---keeping all the values into rows
# It will print the result and return it

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Defining my Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EMPLOYEE and has the following columns - NAME, DEPARTMENT, 
    SECTION and SALARY \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM EMPLOYEE ;
    \nExample 2 - Tell me all the employees working in Data Science department?, 
    the SQL command will be something like this SELECT * FROM EMPLOYEE 
    where DEPARTMENT="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini Pro App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"employee.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
