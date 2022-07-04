import dbInfo.db as db


class CourseInfo:
    course_id: str
    course_name: str
    time: str
    classroom: str
    teacher_id: str

    def __init__(self, mes):
        self.course_id = mes[0]
        self.course_name = mes[1]
        self.time = mes[2]
        self.classroom = mes[3]
        self.teacher_id = mes[4]

    def save_course(self):
        sql = "INSERT INTO `TeacherInfo` (`course_id`, `course_name`, `time`, `classroom`, `teacher_id`) VALUES ('{course_id}', '{course_name}', '{time}', '{classroom}', '{teacher_id}')".format(
            course_id=self.course_id, course_name=self.course_name, time=self.time,
            classroom=self.classroom, teacher_id=self.teacher_id)
        db.cursor.execute(sql)
        db.conn.commit()


def select():
    sql = "select * from `CourseInfo`"
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def select_my_course(key):
    sql = "select * from `CourseInfo` WHERE `teacher_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def deleteOne(key):
    sql = "DELETE FROM `CourseInfo` WHERE `course_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    db.conn.commit()
    print("删除{key}成功".format(key=key))


def select_one_ourse(key):
    sql = "select * from `CourseInfo` WHERE `course_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret
