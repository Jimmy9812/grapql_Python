
# GraphQL in Python
## Description
This project implements a simple GraphQL API using Graphene and Flask in Python. The API allows querying a basic dataset and returns data in a GraphQL format.

## Technologies Used
- Python 3.x: Programming language used for the application.
- Flask: A lightweight framework for building web applications in Python.
- Graphene: A library for building GraphQL APIs in Python.
- Flask-GraphQL: A Flask extension for integrating GraphQL with Flask.
## Requirements
- Python 3.x or higher.
- pip for installing dependencies.
## Installation
1. Clone the repository
To get started, clone the repository to your local machine:
```bash
git clone https://github.com/Jimmy9812/grapql_Python.git
```
2. Navigate to the project directory
After cloning the repository, navigate to the project directory:
```bash
cd grapql_Python
```
3. Create a virtual environment (optional, but recommended)
It's a good practice to use a virtual environment. You can create one with:
```bash
python -m venv venv
```
Then, activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
4. Install dependencies
Once the virtual environment is activated, install the required dependencies:
```bash
pip install -r requirements.txt
```
Running the Application
To run the application, execute the following command:
```bash
python app.py
```
The server will start and you can access the GraphQL API at:
```bash
http://localhost:5000/graphql
```
You can now send queries to this endpoint using a GraphQL client, such as GraphiQL or Postman.

Example Query
To query the data, you can use the following GraphQL query:
```bash
{
  user(id: 1) {
    id
    name
    email
  }
}
```
