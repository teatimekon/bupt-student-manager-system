import dbInfo.db as db


class TeacherInfo:
    teacher_id: str
    teacher_name: str
    teacher_age: int
    teacher_sex: str
    password: str

    def __init__(self, mes):
        self.teacher_id = mes[0]
        self.teacher_name = mes[1]
        self.teacher_age = mes[2]
        self.teacher_sex = mes[3]
        self.password = mes[4]

    def save_teacher(self):
        sql = "INSERT INTO `TeacherInfo` (`teacher_id`, `teacher_name`, `teacher_age`, `teacher_sex`, `password`) VALUES ('{teacher_id}', '{teacher_name}', '{teacher_age}', '{teacher_sex}', '{password}')".format(
            teacher_id=self.teacher_id, teacher_name=self.teacher_name, teacher_age=self.teacher_age,
            teacher_sex=self.teacher_sex, password=self.password)
        db.cursor.execute(sql)
        db.conn.commit()


def select():
    sql = "select * from `TeacherInfo`"
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def deleteOne(key):
    sql = "DELETE FROM `TeacherInfo` WHERE `teacher_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    db.conn.commit()
    print("删除{key}成功".format(key=key))


def select_my_info(key):
    sql = "SELECT `teacher_id`, `teacher_name`, `teacher_sex`, `teacher_age` FROM `TeacherInfo` WHERE `teacher_id` = '{key}'".format(
        key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def select_my_student(key):
    sql = "SELECT `student_id`, `student_name`, `class_id`, `age`, `sex` FROM `StudentInfo` NATURAL JOIN `CourseInfo` NATURAL JOIN `StudentCourse` WHERE `teacher_id` = '{key}'".format(
        key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def select_my_student_grade(key):
    sql = "SELECT `student_id`,`student_name`,`course_id`,`course_name`,`grade` FROM `TeacherInfo` NATURAL JOIN `StudentInfo` NATURAL JOIN `CourseInfo` NATURAL JOIN `StudentCourse` WHERE `teacher_id` = '{key}'".format(
        key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def edit_grade(student_id, course_id, value):
    sql = "UPDATE `StudentCourse` SET `grade` = '{value}' WHERE `student_id` = '{student_id}' AND `course_id` = '{course_id}'".format(
        value=value, student_id=student_id, course_id=course_id)
    db.cursor.execute(sql)
    db.conn.commit()


def add_grade(student_id, course_id, value):
    sql = "INSERT INTO `StudentCourse` (`student_id`,`course_id`,`grade`) values ('{student_id}','{course_id}','{value}')".format(
        value=value, student_id=student_id, course_id=course_id)
    db.cursor.execute(sql)
    db.conn.commit()
