import psycopg2


username="postgres"
pwd="32794"
hostname="localhost"
port_id="5432"
dbname="postgres"
connect = None
cur = None

connect = psycopg2.connect(
    host = hostname,
    database = dbname,
    user = username,
    port = port_id,
    password = pwd, )

insert_sql_query = '''
insert into spisok(text,created_date,rubrics)
values('описание 1502 14 лет, пошлый', '09-11-22', 'тема 1502')
'''

pointer = connect.cursor()
pointer.execute(insert_sql_query)

connect.commit()
print("record is created")
connect.close()
    
