

import sqlite3

conn = sqlite3.connect('test.db')


def makeTbl():
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            )")
        conn.commit()
    conn.close()


def infoAdd():
    conn = sqlite3.connect('test.db')
    
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files(col_fname) \
            VALUES (?)", ('information.docx', 'Hello.txt', 'myImage.png', \
                          'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg'))
        conn.commit()
    conn.close()


def showFiles():
    conn = sqlite3.connect('test.db')

    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_fname WHERE col_fname = '*.txt'")
        varFile = cur.fetchall()
        for item in varFile:
            msg = "File Name: {}".format(item[0])
        print(msg)


