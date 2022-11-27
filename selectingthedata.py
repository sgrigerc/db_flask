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

table_select_query = '''
    select * from spisok

'''
connect.autocommit = True 
pointer = connect.cursor()
pointer.execute(table_select_query)
rows = pointer.fetchall()
# print(rows)

for each_row in rows:
    print(each_row[1])


