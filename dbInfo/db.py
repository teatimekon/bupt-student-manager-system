import pymysql

conn = ""
cursor = ""


def init():
    global conn
    conn = pymysql.connect(host="182.92.83.39", user="soft", password="1145141919", database="db_new")
    #  数据库链接http://182.92.83.39:888/phpmyadmin_76806b89d8cae92d/index.php
    global cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)
