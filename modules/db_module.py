import sqlite3
from urllib.request import pathname2url

db_name = r'dev_choice_db.sqlite3'

def create_connection():
    """
    This function establishes a connection to the database.
    :returns conn: a database connection object if the given db_name
    exists, otherwise rise an error and return false.
    """

    try:
        dburi = 'file:{}?mode=rw'.format(pathname2url(db_name))
        conn = sqlite3.connect(dburi, uri=True)
        print("connected successfuly.")
        return conn
    except sqlite3.OperationalError as err:
        print("connection failed.")
        print("make sure that you have typed the correct database name.")