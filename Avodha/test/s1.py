import psycopg2
x=psycopg2.connect('john.db.elephantsql.com (john-01)','wvzrecoo','cp1NaLobSdY8mcbhNmrxgQ3UjrxJvom7','wvzrecoo')
cr=x.cursor()
cr.excecute('create table student(name char(50),age int)')
cr.execute('insert into students values("varun",36)')
x.commit()
x.close()
