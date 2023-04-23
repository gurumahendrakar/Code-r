import sys

import mysql.connector as mysql
from contextlib import contextmanager

import pandas as pd


# all commands sql
# show table # show databases;
# create table create database;
# select * from table_name;

# unique values ko check karna ek column me table pe work nahi karega
    # select distinct name from students1; distinct unique kitne hai o return karta hai

# new column create in tables
    # alter table (table ka name daal) add (column ke name daala jo banana hai) varchar(20);

# drop columns
        # alter table (table_name)  drop (jo drop karna hai o daal);

# column datatype changeing
         #ALTER TABLE ORDERS MODIFY CITY INT;

# modify changing position columns
            # ALTER TABLE ORDER MODIFY CITY AFTER NAME;

# modify column name
            #ALTER TABLE ORDERS CHANGE NAME NAMES VARCHAR(20);


# rename table name
#         alter table orderr rename orders;


#update column value
        # update orders set names = "Kill" where names= "Guru"



# all columns change same value
#             update orders set city = 3;


@contextmanager
def manager():

    conn = mysql.connect(host='localhost',
                         user='root',
                         password='JOKeR@7411',
                         database='student1',
                         port=1432)
    curser = conn.cursor()
    globals()['connon'] = conn
    yield  curser



a = pd.read_csv('s:/csvfiles/movies.csv')
data = (zip(a.title_x,a.year_of_release,a.imdb_rating))


# "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
with manager() as conn:


    for xx in data:
        io = conn.execute(f'insert into movie values{xx}')


    else:
        globals()['connon'].commit()
        conn.execute('select * from movie')

    for x in conn:
        print(x)



