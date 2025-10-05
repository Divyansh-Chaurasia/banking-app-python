import pymysql

def connect_database():
    global cursor, conn

    conn = pymysql.connect(host='localhost', user='root', password='987654321')
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS bank_data')
    cursor.execute('USE bank_data')
    cursor.execute('CREATE TABLE IF NOT EXISTS data (acc_no VARCHAR(30), name VARCHAR(30), gender VARCHAR(30), dob VARCHAR(30), contact VARCHAR(30), acc_type VARCHAR(30), balance VARCHAR(30))')

def insert(acc_no, name, gender, dob, contact, acc_type, balance):
    cursor.execute('INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s, %s)', (acc_no, name, gender, dob, contact, acc_type, balance))
    conn.commit()

def update(acc_no, name, gender, dob, contact, acc_type):
    cursor.execute('UPDATE data SET name=%s, gender=%s, dob=%s, contact=%s, acc_type=%s WHERE acc_no=%s', (name, gender, dob, contact, acc_type, acc_no))
    conn.commit()

def delete(acc_no):
    cursor.execute('DELETE FROM data WHERE acc_no=%s', (acc_no))
    conn.commit()

def get_balance(acc_no):
    cursor.execute('SELECT balance FROM data WHERE acc_no=%s', (acc_no))
    result = cursor.fetchone()
    conn.commit()
    return result[0]

def update_balance(acc_no, balance):
    cursor.execute('UPDATE data SET balance=%s WHERE acc_no=%s', (balance, acc_no))
    conn.commit()

def acc_no_exists(acc_no):
    cursor.execute('SELECT COUNT(*) FROM data WHERE acc_no=%s', acc_no)
    result = cursor.fetchone()
    return result[0] != 0

def specific_data(Acc_no):
    cursor.execute('SELECT name, gender, dob, contact, acc_type FROM data WHERE acc_no=%s', (Acc_no))
    result = cursor.fetchone()
    conn.commit()
    return result

def fetch_data():
    cursor.execute('SELECT acc_no, name, acc_type, balance FROM data')
    result = cursor.fetchall()
    conn.commit()
    return result

def get_all_data(acc_no):
    cursor.execute('SELECT * FROM data WHERE acc_no=%s', acc_no)
    result = cursor.fetchone()
    conn.commit()
    return result

connect_database()