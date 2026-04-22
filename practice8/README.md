PhoneBook Application – Practice 8
📌 Overview

This project is an extension of the PhoneBook application from Practice 7.
The main goal is to implement PostgreSQL functions and stored procedures and move core logic into the database layer.

The application allows you to:

Search contacts by pattern
Insert or update contacts
Insert multiple contacts with validation
Retrieve contacts with pagination
Delete contacts
🛠 Technologies Used
Python (psycopg2)
PostgreSQL
PL/pgSQL
📁 Project Structure
Practice8/
├── phonebook.py        # Main application file
├── functions.sql       # SQL functions
├── procedures.sql      # Stored procedures
├── config.py           # Database configuration
└── connect.py          # Database connection