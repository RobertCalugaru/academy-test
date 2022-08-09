import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy import select
import numpy as np


mydb = mysql.connector.connect(
  host="34.163.182.248",
  port=3306,
  user="root",
  password="Ciocanul12@",
  database="academy"
)

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}:3306/{db}"
            .format(host="34.163.182.248", db='academy', user='root', pw='Ciocanul12%40'))
#

mycursor = mydb.cursor()

# com = "CREATE TABLE robert_city_average(city varchar(50), average_salary int, number_of_players int, PRIMARY KEY(city));"
# engine.execute(com)



#
# sql = "INSERT INTO city_average (city) VALUES (%s)"
# val = "SELECT team.city FROM nba_players"
# df = pd.DataFrame(val)
#
#
# mycursor.execute(sql, val)
# ADAUGARE DE ELEMENTE IN TABEL
# comanda = "INSERT INTO city_average (city) SELECT team.city from nba_players"
# mycursor.executemany(comanda, val)
# mydb.commit()

# row = mycursor.fetchall()
# print(row)


# mycursor.execute('select * from nba_players')
# row = mycursor.fetchall()
# print(row)

mycursor.execute("SELECT * FROM nba_players")
sql_data = pd.DataFrame(mycursor.fetchall())
sql_data.columns = mycursor.column_names
# print(sql_data.to_string())



# df_merge_col = pd.merge(df_row, df3, on='id')

mycursor.execute("SELECT * FROM nba_salary")
sql_data2 = pd.DataFrame(mycursor.fetchall())
sql_data2.columns = mycursor.column_names
# print(sql_data.to_string())

mycursor.execute("SELECT * FROM nba_savings")
sql_data3 = pd.DataFrame(mycursor.fetchall())
sql_data3.columns = mycursor.column_names
# print(sql_data2.to_string())

# mycursor.execute("SELECT * FROM robert_city_average")
# sql_data4 = pd.DataFrame(mycursor.fetchall())
# sql_data4.columns = mycursor.column_names
# print(sql_data4.to_string())

d = pd.merge(sql_data, sql_data2, left_index=True, right_index=True)
df_bun=d.drop(['id_x','id_y'],axis=1)
# print(df_bun.to_string())

d2 = pd.merge(df_bun, sql_data3, left_index=True, right_index=True)
print(d2.to_string())
# df_bun2=d.drop(['id'],axis=1)
# print(df_bun2.to_string())
#

# average=d2["Salary"].mean()
# print(average)

# nop = d2.groupby(['team.city'])['first_name'].count()
# print(nop)

# coloane = {'city': [],'average_salary':[], 'number_of_players':[]}
# d3 = pd.DataFrame(data = coloane)
# d3['city'] = d2['team.city']
# # d3['average_salary'] = d2.groupby(by=['team.city'])['Salary'].mean()
# d3['number_of_players'] = d2.groupby(['team.city'])['first_name'].count()
# print(d3)

# l1=d2.groupby(by=['team.city'])['Salary'].mean()
# l2=d2.groupby(['team.city'])['first_name'].count()
# l3=pd.merge(l1,l2, on='team.city')
# l4=l3.reset_index()
# print(l4)



# l4.to_sql('robert_city_average', con=engine, if_exists='replace', index=False)
# print(engine.execute("SELECT * FROM robert_city_average").fetchall())


# com = "CREATE TABLE robert_players_average(full_name varchar(50), above_average_salary varchar(50), PRIMARY KEY(full_name));"
# engine.execute(com)

l5=pd.DataFrame()
l5['full_name']=d2['first_name'] + d2['last_name']
avg=d2["Salary"].mean()
l5['Above_average_salary'] = np.where(d2['Salary'] > avg, True, False)
# print(l5)

l5.to_sql('robert_players_average', con=engine, if_exists='replace', index=False)
print(engine.execute("SELECT * FROM robert_players_average").fetchall())



# com = "CREATE TABLE robert_LA_salary(full_name varchar(50), salary int, PRIMARY KEY(full_name));"
# engine.execute(com)


# l7=d2.groupby(['team.city'])['first_name'].count()
# print(l7)


# merged_df = sql_data.merge(sql_data2, how='inner', on=["id"])
# print(merged_df.to_string())

# mycursor.execute("SELECT * FROM city_average")
# sql_data = pd.DataFrame(mycursor.fetchall())
# sql_data.columns = mycursor.column_names
# print(sql_data.to_string())


# mycursor.execute("SHOW TABLES")
# r = mycursor.fetchall()
# print(r)
