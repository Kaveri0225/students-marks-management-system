import streamlit as st
import sqlite3


#DataBase connectivity
conn = sqlite3.connect("student.db")
print("successfully connected with DataBase")
cursor = conn.cursor()

#creating student  table in database
cursor.execute("create table if not exists student(id integer primary key autoincrement,name text,sub1 integer,sub2 integer,sub3 integer,total integer)")
print("table created")
conn.commit()

st.title(" Students Marks Management system")
st.write("This application stores the marks of the student")

name = st.text_input("Enter the student name:")
sub1 = st.number_input("Enter the subject 1 marks:")
sub2 = st.number_input("Enter the subject 2 marks:")
sub3 = st.number_input("Enter the subject 3 marks:")
total = sub1+sub2+sub3
avg = total/3


if st.button("Save"):
   cursor.execute("insert into student(name,sub1,sub2,sub3,total)values(?,?,?,?,?)",(name,sub1,sub2,sub3, total))
   conn.commit()
   st.success("Students marks stored succesfully:")


if st.button("view all student data"):
   cursor.execute("select * from student")
   data = cursor.fetchall()
   st.dataframe(data,column_config={"0":"ID","1":"NAME","2":"SUB1","3":"SUB2","4":"SUB3","5":"TOTAL","6":"avg","7":"percentage"})

conn.close()