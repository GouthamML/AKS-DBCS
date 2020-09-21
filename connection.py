##############################################################################################
# Sample script to connect Oracle Database Cloud Service
#
# 
# Written using SQLAlchemy and cx_Oracle,  https://docs.sqlalchemy.org/en/13/dialects/oracle.html
#
##############################################################################################
import sqlalchemy
import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Oracle Database Cloud Service credentials
#documentation https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Tasks/connectingDB.htm
username = ""
password = ""
ip = ""
service_name = ""
tableName = ""

#Creating Connection sursor
print("\n\nInitiating connection\n\n")
dsn = cx_Oracle.makedsn(ip,'1521',service_name=service_name)
engine = create_engine('oracle+cx_oracle://%s:%s@%s' % (username, password, dsn))
conn = engine.connect()
print("\n\nConnection established\n\n")

DBSession = sessionmaker(bind=engine)
session = DBSession()
print("\n\nSession Strated\n\n")

metadata = sqlalchemy.MetaData() 
table = sqlalchemy.Table(tableName, metadata, autoload=True, autoload_with=engine)
column_keys = table.columns.keys()
print(column_keys)
query = sqlalchemy.select([table])
res = conn.execute(query)
res_set = res.fetchall()
print(res_set)
#session.close()
