

import sqlite3 #imports sqlite3 module

conn = sqlite3.connect('test.db') #creates a variable that uses the sqlite3 module to connect to the database specified



with conn:
    cur = conn.cursor() #creates a variable that that uses the cursor function
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )") #uses cur variable to execute the command in sql to create a table if it doesn't already exist
    conn.commit()   #executes the commit function to save the data changes to the db

conn = sqlite3.connect('test.db')

file_names = ('information.docx', 'Hello.txt', 'myImage.png', \
              'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg',) #creates tuple of file names


for x in file_names:    #for loop to iterate through the tuple 'file_names'
    if x.endswith('.txt'):  #confirms items ending with .txt while iterating through the tuple
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_fname) VALUES (?)", (x,))   #executes command specified. In this case 
            print(x)                                                            #adding x from file_names

            
conn.close()    #terminates the connection to the db


