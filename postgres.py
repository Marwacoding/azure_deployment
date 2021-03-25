from my_scrap import *
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
import logging

#print(os.environ["pw"])
logging.basicConfig(filename = "db_scrapping.log", 
                    level= logging.DEBUG, 
                    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')



host=os.environ["host"]
dbname=os.environ["db"]
user=os.environ["user"]
password=os.environ["pw"]

conn_string = "host={0} dbname={1} user={2} password={3}".format(host, dbname, user, password)
conn = psycopg2.connect(conn_string)


cursor = conn.cursor()
 

def erase_table():
    cursor.execute("DROP Table carpet")
    cursor.execute("DROP Table mirror")
    conn.commit()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS carpet (ID SERIAL PRIMARY KEY , NOM VARCHAR(255), PRIX VARCHAR(30))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mirror (ID SERIAL PRIMARY KEY, NOM VARCHAR(255), PRIX VARCHAR(30))")
    conn.commit()

def insert_info():
    carpet_sql = "INSERT INTO carpet (NOM, PRIX) VALUES (%s,%s)"
    carpet_valeur = c.zip_list_carpet()
    #print(carpet_valeur)
    cursor.executemany(carpet_sql, carpet_valeur)
    
    mirror_sql = "INSERT INTO mirror (NOM, PRIX) VALUES (%s,%s)"
    mirror_valeur = m.zip_list_mirror()
    #print(mirror_valeur)
    cursor.executemany(mirror_sql, mirror_valeur)

    conn.commit()

def select_latest():
    cursor.execute("SELECT * FROM carpet LIMIT 5")
    return cursor.fetchall()


#erase_table()
#create_table()
insert_info()
select_latest()



 