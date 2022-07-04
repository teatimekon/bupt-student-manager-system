import dbInfo.db as db


class Test:
    id: int
    username: str

    def __init__(self, mes):
        self.id = mes[0]
        self.username = mes[1]

    def save_test(self):
        sql = "insert into `test`(`id`,`username`) values ('{id}','{username}')".format(
            id=self.id, username=self.username)
        db.cursor.execute(sql)
        db.conn.commit()


def select():
    sql = "select * from `StudentInfo`"
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret
