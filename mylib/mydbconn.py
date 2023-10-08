"""
Connects to an Azure Sql Server database and returns a connection object
along with a "success" message string.
"""
import os
import pypyodbc as odbc
from dotenv import load_dotenv


def setConn():
    # Load environment variables from .env file
    load_dotenv()

    SERVER = os.getenv("SERVER_NAME")
    DATABASE = os.getenv("DATABASE")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    conn_string = (
        "Driver={ODBC Driver 18 for SQL Server};Server="
        + SERVER
        + ",1433;Database="
        + DATABASE
        + ";Uid="
        + USERNAME
        + ";Pwd="
        + PASSWORD
        + ";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    )
    myConn = odbc.connect(conn_string)
    return myConn, "Success"
