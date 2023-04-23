import collections

import mysql.connector
from contextlib import contextmanager
from pprint import pprint
import csv 

def connector(connection):
    try:
        
        _ = connection.connect(
                                user="root",
                                password='JOKeR@7411',
                                host='localhost',
                                port=1432,
                                database='performance_schema'
                                    )
        @database_name
        def use_database():
            return _.database


        @query
        def show_databases():
             cursor = _.cursor()
             cursor.execute("SHOW DATABASES")
             return  cursor

        return _

    except:
        class WrongInfo(Exception):
            def __str__(self) -> str:
                return "Server Not Found Please Check Your Filled Details"

        raise WrongInfo()


def query(argument=None):
        pprint(tuple(argument()))



def database_name(database=None)->str:
    print("Your Database Use -->",database())




io = connector(mysql.connector)
cursor = io.cursor()
cursor.execute('use players')



with open('S:/floor/cool2.csv') as file:
    reader = csv.reader(file)
    next(reader)
 
    for data in reader:
        cursor.execute(f"INSERT INTO killers values('{data[0]}','{data[1]}','{data[2]}')") 
        io.commit()
    
