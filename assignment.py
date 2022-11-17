import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="5321Han5321!", database="assignment")
mycurs = db.cursor()
# mycurs.execute("select * from Country")
# result = mycurs.fetchall()
# for i in result:
#     print(i)

# mycurs.execute("select * from Users where salary>150000")
# result = mycurs.fetchall()
# for i in result:
#     print(i)

#1
mycurs.execute("select distinct a.disease_code, a.description from Disease a join Discover b on a.disease_code = b.disease_code where a.pathogen = 'bacteria' and b.first_enc_date < '1990-01-01'")

#2
# mycurs.execute("select name, surname, degree from Users, Doctor where ")

#3
# mycurs.execute("")

#4
# mycurs.execute("")

#5
# mycurs.execute("")

#6
# mycurs.execute("")

#7
mycurs.execute("delete from Users where name like ('%bel%' or '%gul%')")

#8
mycurs.execute("create index idx_pathogen on Disease (pathogen)")

#9
# mycurs.execute("")

#10
# mycurs.execute("")

#11
# mycurs.execute("")
