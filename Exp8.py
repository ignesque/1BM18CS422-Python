from sqlite3 import Error, connect


def connection():
    try:
        con = connect('Student.db')
        return con
    except Error:
        print(Error)


def table(con):
    query = "CREATE TABLE if exists information(USN text PRIMARY KEY,Name text,Department text,CGPA real)"
    cursor = con.cursor()
    try:
        cursor.execute(query)
        con.commit()
    except Error:
        print(Error, "Table Already Exists")
    else:
        print("Table Created")


def insert(con, sdict):
    query = "INSERT INTO information(USN,Name,Department,CGPA) values(?,?,?,?)"
    cursor = con.cursor()
    try:
        cursor.execute(query, (sdict.get('USN'), sdict.get(
            'Name'), sdict.get('Department'), sdict.get('CGPA')))
        con.commit()
    except Error:
        print(Error, "Values missing or Wrong datatype")
    else:
        print("Values Inserted")


def display(con):
    query = "SELECT * FROM information"
    cursor = con.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print('USN is', row[0])
            print('Name is', row[1])
            print('Department is', row[2])
            print('CGPA is', row[3])
            print("\n")
        cursor.close()
    except Error:
        print(Error, "Table Empty")


def search(con, key):
    query = "SELECT * FROM information WHERE USN=?"
    cursor = con.cursor()
    try:
        cursor.execute(query, (key,))
    except Error:
        print(Error)
    else:
        row = cursor.fetchone()
        if not row:
            print("Record not found")
        else:
            print('USN is', row[0])
            print('Name is', row[1])
            print('Department is', row[2])
            print('CGPA is', row[3])
            cursor.close()


def update(con, key, new):
    query = "UPDATE information SET CGPA=? WHERE USN=?"
    cursor = con.cursor()
    try:
        cursor.execute(query, (new, key))
        con.commit()
    except Error:
        print(Error, "Record not found or Wrong Datatype")
    else:
        print("Value Updated")


def delete(con, key):
    query = "DELETE information WHERE USN=?"
    cursor = con.cursor()
    try:
        cursor.execute(query, (key,))
        con.commit()
    except Error:
        print(Error, "Table Empty or USN not found")
    else:
        print("Values Deleted")


def control(con):
    type = input(
        "\n1:Create, 2:Delete, 3:Insert, 4:Update, 5:Display, 6:Search, 7:Exit\nEnter:")
    if type == '1':
        table(con)
    elif type == '3':
        usn, name, dept, cgpa = input(
            "Enter USN, Student Name, Department, CGPA scored:").split(',')
        studentdict = {'USN': usn, 'Name': name,
                       'Department': dept, 'CGPA': cgpa}
        insert(con, studentdict)
    elif type == '5':
        display(con)
    elif type == '6':
        key = input("Enter USN to search record:")
        search(con, key)
    elif type == '4':
        key, new = input("Enter USN and CGPA to be changed:").split(',')
        update(con, key, new)
    elif type == '2':
        key = input("Enter Student USN to be removed from table:")
        delete(con, key)
    elif type == '7':
        con.close()
        exit()
    control(con)


con = connection()
control(con)
