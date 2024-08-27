import mysql.connector

#def createcon() :
 #   try:
  #      con = mysql.connector.connect(
   #         host ="localhost",
    #        user ="ajees",
     #       password ="",
      #      database = "ajeesdb"
#)
  #      cursor =con.cursor()
   #     return cursor
    #except Exception as err:
     #   print(str(err))
con = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="ajees2609",
    database = "ajeesdb"
)
cursor = con.cursor()
query = "select * from employee"
cursor.execute(query)
data = cursor.fetchall()

print(data)
