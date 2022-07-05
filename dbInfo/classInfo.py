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


def update_all(class_id, oldId, class_name, professional_name):
    sql = "UPDATE `ClassInfo` SET `class_id`= '{class_id}',`class_name`='{class_name}',`professional_name` = '{professional_name}' WHERE `class_id` = '{oldId}'".format(
        class_id=class_id, class_name=class_name, professional_name=professional_name, oldId=oldId)
    db.cursor.execute(sql)
    db.conn.commit()


def select_class(key):
    sql = "SELECT * FROM `ClassInfo` WHERE `class_id` = '{key}'".format(
        key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def deleteOne(key):
    sql = "DELETE FROM `ClassInfo` WHERE `class_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    db.conn.commit()
    print("删除{key}成功".format(key=key))
