# A User_finder web application using flask, SQLITE, and Python using MVC Architecture
  User can register their phone number and username and can search their phonenumber using username. 
  
# Features
  1. User can register name and their phone number.
  2. Data of the user is stored permanently using SQlite.
  3. Search Phonenumber using Username
  4. Simple and Beginner Friendly
  5. Clean seperation within a code using MVC Architecture
     
# Technology
**Python3**
**Flask**
**SQlite**
**HTML (Jinja Technique)**

# System Architecture
The User_finder Web Application follows a three-tier architecture based on the Model–View–Controller (MVC) design pattern. The system is divided into presentation, application, and data layers to ensure modularity, maintainability, and clarity.

1️⃣ Presentation Layer (View)
The Presentation Layer is responsible for interacting with the user. It provides web pages where users can enter data and view results.
Implemented using HTML templates with Jinja
Displays:
Search form
Registration form
Search results and messages
Receives data from the Controller and renders it dynamically
Components:
homepage.html
register.html
2️⃣ Application Layer (Controller)
The Application Layer controls the flow of the system. It handles user requests, processes input, and coordinates between the View and the Model.
Implemented using Flask routes
Responsibilities:
Receive HTTP requests (GET, POST)
Extract user input
Call appropriate Model functions
Select and return the correct View
Handle redirection after form submission
Components:
Flask route handlers (/, /search, /register, /users)
3️⃣ Data Layer (Model)
The Data Layer manages data storage and retrieval. It directly interacts with the database and enforces data rules.
Implemented using SQLite
Uses parameterized SQL queries for security
Performs:
Insert user data
Search user phone numbers
Components:
user_db.py
database.db
🔄 System Flow
User sends a request via the browser
Controller receives and processes the request
Model performs database operations if required
Controller sends processed data to the View
View renders the response to the user

# Installation
This section describes the steps required to install and run the User_finder Web Application on a local system.
🔧 Prerequisites
Before installing the project, ensure the following are available:
Python 3.8 or higher
pip (Python package manager)
A web browser (Chrome, Firefox, Safari, etc.)
To check Python installation:
python --version
📥 Step 1: Clone the Repository
Download the project from GitHub:
git clone https://github.com/your-username/flask-phonebook.git
cd flask-phonebook
📦 Step 2: Install Required Packages
Install Flask using pip:
pip install flask
(SQLite is built into Python, so no separate installation is required.)
🗄️ Step 3: Initialize the Database (Run Once)
Create the SQLite database and required tables by running the database setup file:
python db_setup.py
📌 This step is required only once.
The database file (database.db) will be created automatically.
▶️ Step 4: Run the Application
Start the Flask development server:
python app.py
If successful, you will see output similar to:
Running on http://127.0.0.1:5000/
