# Agenda--->Converting Natural text to SQL query----query hit the database and retrive the data
# 1st create the custom prompt---then with the help of LLM model/Gemini Pro---
# Prompt will convert into SQL query--- and we will use this query to hit the database---
# And finally will get the response
# I will use local DB sqlite--- to get quick and hasseleless response
# Inserting some data by python programming

import streamlit as st
import pandas as pd
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
# Return both column names and rows

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)

    # Fetch column names
    column_names = [description[0] for description in cur.description]

    # Fetch data
    rows = cur.fetchall()

    conn.commit()
    conn.close()

    return column_names, rows


## Defining my Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name DENTAL and has two tables - Provider_info & Contract_info,
    \n with having following columns - Taxid, Mtvid, Cisid, Prov_Name, Age, Contract_id, Contract_name,
    Contract_effective_date, Contract_end_date and Category \n\nFor example,
    \nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM Provider_info ;
    \nExample 2 - Tell me all the Contract_id ,which has category is direct?, 
    the SQL command will be something like this SELECT Contract_id FROM Contract_info
    where Category="Direct"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Sandeep_Gemini Pro App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
# Check for "date" in column name
# Convert to datetime format
# Format as DD/MM/YYYY
# Display the DataFrame with column names
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    column_names, rows = read_sql_query(response, "Dental.db")

    # Create a DataFrame with column names
    df = pd.DataFrame(rows, columns=column_names)
    # Format date columns
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col])
            df[col] = df[col].dt.strftime("%d/%m/%Y")
    st.subheader("The Response is")
    st.dataframe(df)
