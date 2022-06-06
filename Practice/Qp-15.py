import mysql.connector

dbConnect = mysql.connector.connect(
    host="localhost",
    user="vikash",
    passwd="rrsv",
    database="APP"
)

db = dbConnect.cursor()

# db.execute("CREATE TABLE Students (s_no INT AUTO_INCREMENT, reg_no INT(20) , name VARCHAR(100), email VARCHAR(100), phone INT(50), dept VARCHAR(50), PRIMARY KEY(s_no))")
# db.execute("INSERT INTO Students (name, email, phone, dept) values ('asdf','we@aa.as',22332,'ERS'),('vikash','asdf@sdf.as',1212,'CSE')")
# db.execute("SELECT reg_no , dept , name FROM Students")
# db.execute("SELECT * FROM Students WHERE name LIKE '%f' ")
db.execute("SELECT * FROM Students")


for x in db:
    print(x)
