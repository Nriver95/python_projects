import sqlite3


#connection = sqlite3.connect("D:\Work\GitHub\python_projects\sqlite&python\myTestDatabase.db")
#connection.close()
#with sqlite3.connect('test_database.db') as connection:
#    c = connection.cursor()
#    c.executescript("""DROP TABLE IF EXISTS People;
#                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
#                    INSERT INTO People VALUES('Ron', 'Obvious', '42');
#                    """)

"""#get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)"""

"""#execute insert statement for supplied person data
with sqlite3.connect('myTestDatabase.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)"""
    
"""#execute insert statement for supplied person data
with sqlite3.connect('myTestDatabase.db') as connection:
    personData = (firstName, lastName, age)
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)"""

#c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
#          (29, 'Nick', 'Rivera'))

#peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('myTestDatabase.db') as connection:
    c = connection.cursor()
#    c.execute("DROP TABLE IF EXISTS Others")
#    c.execute("CREATE TABLE Others(FirstName TEXT, LastName TEXT, Age INT)")
#    c.executemany("INSERT INTO Others VALUES(?,?,?)", peopleValues)

#select all first and last names from people over 30
    c.execute("SELECT FirstName, LastName FROM Others WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
