import dbInfo.db as db


class StudentInfo:
    student_id: str
    student_name: str
    class_id: str
    age: int
    sex: str
    password: str

    def __init__(self, mes):
        self.student_id = mes[0]
        self.student_name = mes[1]
        self.class_id = mes[2]
        self.age = mes[3]
        self.sex = mes[4]
        self.password = mes[5]

    def save_student(self):
        sql = "INSERT INTO `StudentInfo` (`student_id`, `student_name`, `class_id`, `age`, `sex`, `password`) VALUES ('{student_id}', '{student_name}', '{class_id}', '{age}', '{sex}', '{password}')".format(
            student_id=self.student_id, student_name=self.student_name, class_id=self.class_id, age=self.age,
            sex=self.sex, password=self.password)
        db.cursor.execute(sql)
        db.conn.commit()


def select():
    sql = "select `student_id`, `student_name`, `class_id`, `age`, `sex` from `StudentInfo`"
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def select_my_info(key):
    sql = "SELECT `student_id`, `student_name`, `class_id`, `age`, `sex` FROM `StudentInfo` WHERE `student_id` = '{key}'".format(
        key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def select_my_grade(key):
    sql = "SELECT `student_id`,`course_id`, `course_name`,`grade` FROM `StudentInfo` NATURAL JOIN `CourseInfo` NATURAL JOIN `StudentCourse`" \
          "WHERE `student_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def deleteOne(key):
    sql = "DELETE FROM `StudentInfo` WHERE `student_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    db.conn.commit()
    print("删除{key}成功".format(key=key))
