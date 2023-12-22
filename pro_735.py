# -*- coding: utf-8 -*-
"""pro_735.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Agl_uEsRdTJ2LHawtLN0L1XauMXMDyg
"""

import pandas as pd
import sqlite3
import sys
from termcolor import colored
a=pd.read_excel("eg.xlsx")
d=a.values
c=sqlite3.connect('database.db')
b=c.cursor()
e=b.execute(""" create table studentdata (name text,pin text,quiz1 int,mid1 int,total int) """)
h=b.executemany("""insert into studentdata values (?,?,?,?,?)""",d)
f=b.execute(""" select * from studentdata""")
for g in f:
  print(g)

print(colored("SELECT",'red'))
k=b.execute(""" select name from studentdata""")
for i in k:
  print(i)

print(colored("SELECT DISTINCT",'blue'))
d=b.execute(""" select distinct quiz1 from studentdata""")
for c in d:
  print(c)

print(colored("DISTINCT 2C",'blue'))
d=b.execute(""" select distinct quiz1,mid1 from studentdata""")
for c in d:
  print(c)

print(colored("COUNT DISTINCT","green"))#no multiple
d=b.execute(""" select count(distinct total) from studentdata""")
for c in d:
  print(c)

print(colored("DISNTINCT SUM","yellow"))#no multiple
d=b.execute(""" select sum(distinct quiz1) from studentdata""")
for c in d:
  print(c)

print(colored("SUM","magenta"))#no multiple
d=b.execute(""" select sum(quiz1) from studentdata""")
for c in d:
  print(c)

print(colored("CONDITION","red"))
d=b.execute(""" select name from studentdata where mid1>6""")
for c in d:
  print(c)

print(colored("CONDITION2","red"))
d=b.execute(""" select name,pin from studentdata where mid1>=7.67""")
for c in d:
  print(c)

print(colored("CONDITION3","red"))
d=b.execute(""" select name from studentdata where mid1>7.67 and quiz1>=10""")
for c in d:
  print(c)

print(colored("CONDITION4","red"))
d=b.execute(""" select name,pin from studentdata where mid1>=7.67 and quiz1>=10""")
for c in d:
  print(c)

print(colored("ORDER BY - ASCENDING ORDER","blue"))
d=b.execute(""" select * from studentdata order by mid1""")
for c in d:
  print(c)

print(colored("ORDER BY - DESCENDING ORDER","green"))
d=b.execute(""" select * from studentdata order by mid1 desc""")
for c in d:
  print(c)

print(colored("UPDATE","yellow"))
b.execute("""update studentdata set quiz1=0 where quiz1="-" """)
d=b.execute(""" select * from studentdata""")
for a in d:
  print(a)

print(colored("DELETE","magenta"))
b.execute(""" delete from studentdata where quiz1=0 """)
d=b.execute(""" select * from studentdata""")
for a in d:
  print(a)

print(colored("MAX & MIN & AVG","red"))
j=b.execute(""" select min(mid1) from studentdata """)
for k in j:
  print(k)
k=b.execute(""" select max(quiz1) from studentdata """)
for l in k:
  print(l)
k=b.execute(""" select avg(total) from studentdata """)
for l in k:
  print(l)

print(colored("ALTER","blue"))
b.execute(""" alter table studentdata add grade text """)
d=b.execute(""" select * from studentdata""")
for a in d:
  print(a)

import pandas as pd
excel_file = 'eg.xlsx'
df = pd.read_excel(excel_file)
csv_file = 'output_csv_file.csv'
df.to_csv(csv_file, index=False)

import pandas as pd
file_path = 'output_csv_file.csv'
data = pd.read_csv(file_path)

import matplotlib.pyplot as plt

# Histogram for Quiz-1 scores
plt.hist(data['Quiz: Quiz-1 (Real)'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Quiz-1 Scores')
plt.xlabel('Quiz-1 Scores')
plt.ylabel('Frequency')
plt.xticks([])
plt.show()

# Bar chart for course total scores
plt.bar(data['Surname'], data['Course total (Real)'], color='lightcoral')
plt.title('Course Total Scores')
plt.xlabel('Students')
plt.ylabel('Course Total Scores')
plt.xticks(rotation=90)
plt.xticks([])
plt.show()

# Scatter plot for Quiz-1 vs Mid1 scores
plt.scatter(data['Quiz: Quiz-1 (Real)'], data['Quiz: Mid1 (Real)'], color='green')
plt.title('Quiz-1 vs Mid1 Scores')
plt.xlabel('Quiz-1 Scores')
plt.ylabel('Mid1 Scores')
plt.xticks([])
plt.show()

# Line plot for individual student performance
plt.plot(data['Surname'], data['Quiz: Quiz-1 (Real)'], marker='o', label='Quiz-1')
plt.plot(data['Surname'], data['Quiz: Mid1 (Real)'], marker='x', label='Mid1')
plt.plot(data['Surname'], data['Course total (Real)'], marker='s', label='Course Total')
plt.title('Student Performance')
plt.xlabel('Students')
plt.xticks([])
plt.ylabel('Scores')
plt.xticks(rotation=90)
plt.legend()
plt.show()

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Surname'], y=data['Quiz: Quiz-1 (Real)'], mode='markers+lines', name='Quiz-1'))
fig.add_trace(go.Scatter(x=data['Surname'], y=data['Quiz: Mid1 (Real)'], mode='markers+lines', name='Mid1'))
fig.add_trace(go.Scatter(x=data['Surname'], y=data['Course total (Real)'], mode='markers+lines', name='Course Total'))
fig.update_layout(title='Student Performance', xaxis_title='Students', yaxis_title='Scores')
fig.show()

fig = go.Figure(data=[go.Histogram(x=data['Quiz: Quiz-1 (Real)'], nbinsx=10)])
fig.update_layout(title='Distribution of Quiz-1 Scores', xaxis_title='Quiz-1 Scores', yaxis_title='Frequency')
fig.show()

fig = go.Figure(data=[go.Bar(x=data['Surname'], y=data['Course total (Real)'], marker_color='lightcoral')])
fig.update_layout(title='Course Total Scores', xaxis_title='Student Surnames', yaxis_title='Course Total Scores')
fig.show()

fig = go.Figure(data=[go.Scatter(x=data['Quiz: Quiz-1 (Real)'], y=data['Quiz: Mid1 (Real)'], mode='markers', marker=dict(color='green'))])
fig.update_layout(title='Quiz-1 vs Mid1 Scores', xaxis_title='Quiz-1 Scores', yaxis_title='Mid1 Scores')
fig.show()