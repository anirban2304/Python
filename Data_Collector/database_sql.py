import pyodbc
from sqlalchemy import create_engine
import urllib
server = 'python-project.database.windows.net'
database = 'height_data'
username = 'admin-python'
password = 'Kolkata@23'
driver= '{ODBC Driver 17 for SQL Server}'

params = urllib.parse.quote_plus\
    (r'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str,echo=True)

print('connection is ok')
print(engine_azure.table_names())

"""
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM dbo.email_height as pc")
row = cursor.fetchone()
while row:
    print (str(row[1]) + " " + str(row[2]))
    row = cursor.fetchone()
"""