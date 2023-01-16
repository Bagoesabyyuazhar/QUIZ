import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port=23306,
  user="root",
  password="p455w0rd",
  database="garden"
)

#print(mydb)

db = mydb.cursor()
db.execute("Create database garden")
db.execute("CREATE TABLE Mawar (id INT AUTO_INCREMENT PRIMARY KEY, Beri_Air VARCHAR(255), Beri_Pupuk VARCHAR(255), Status VARCHAR(255))")
sql = "INSERT INTO Anggrek (Beri_Air, Beri_Pupuk, Status) VALUES (%s, %s, %s)"
val = ("4", "2", " Berbunga ")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")

db.execute("SELECT * FROM Anggrek")

res = db.fetchall()

for x in res:
  print(x)

db.execute("SHOW TABLES")
for x in db:
  print(x)

db.execute("Show databases")
for x in db:
  print(x)







