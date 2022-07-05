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


def update_all(student_id, oldId, student_name, class_id, age, sex):
    sql = "UPDATE `StudentInfo` SET `student_id`= '{student_id}',`student_name`='{student_name}',`class_id`='{class_id}',`age`='{age}',`sex`='{sex}' WHERE student_id = '{oldId}'".format(
        student_id=student_id, student_name=student_name, class_id=class_id, sex=sex, age=age, oldId=oldId)
    db.cursor.execute(sql)
    db.conn.commit()


def select_my_info(key):
    sql = "SELECT `student_id`, `student_name`, `class_id`, `age`, `sex` FROM `StudentInfo` WHERE `student_id` = '{key}'".format(
        key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def select_my_grade(key):
    sql = "SELECT t1.`student_id`,t2.`course_id`, t2.`course_name`,t3.`grade` FROM `StudentInfo` as t1, `CourseInfo` as t2 ,`StudentCourse` as t3 WHERE t1.`student_id` = {key} and t1.`student_id` = t3.`student_id` and t2.`course_id` = t3.`course_id`".format(
        key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def deleteOne(key):
    sql = "DELETE FROM `StudentInfo` WHERE `student_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    db.conn.commit()
    print("删除{key}成功".format(key=key))


def select_password():
    sql1 = "SELECT `student_id` as `id`,`password` FROM `StudentInfo` WHERE 1"
    sql2 = "SELECT `teacher_id` as `id`,`password` FROM `TeacherInfo` WHERE 1"
    db.cursor.execute(sql1)
    ret1 = db.cursor.fetchall()
    db.cursor.execute(sql2)
    ret2 = db.cursor.fetchall()
    return ret1 + ret2


def update_password(id, password):
    sql = "UPDATE `StudentInfo` SET `password`= '{password}' WHERE student_id = '{id}'".format(
        id=id, password=password)
    db.cursor.execute(sql)
    db.conn.commit()
