import dbInfo.db as db


class ClassInfo:
    class_id: str
    class_name: str
    professional_name: str

    def __init__(self, mes):
        self.class_id = mes[0]
        self.class_name = mes[1]
        self.professional_name = mes[2]

    def save_class(self):
        sql = "INSERT INTO `ClassInfo` (`class_id`, `class_name`, `professional_name`) VALUES ('{class_id}', '{class_name}', '{professional_name}')".format(
            class_id=self.class_id, class_name=self.class_name, professional_name=self.professional_name, )
        db.cursor.execute(sql)
        db.conn.commit()


def select():
    sql = "select * from `ClassInfo`"
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret
