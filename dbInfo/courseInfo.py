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
        sql = "INSERT INTO `CourseInfo` (`course_id`, `course_name`, `time`, `classroom`, `teacher_id`) VALUES ('{course_id}', '{course_name}', '{time}', '{classroom}', '{teacher_id}')".format(
            course_id=self.course_id, course_name=self.course_name, time=self.time,
            classroom=self.classroom, teacher_id=self.teacher_id)
        db.cursor.execute(sql)
        db.conn.commit()


def select():
    sql = "select  `course_id`,`course_name`,`time`,`teacher_id`,`classroom` from `CourseInfo`"
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def update_all(course_id, course_name, time, classroom, teacher_id, oldId):
    sql = "UPDATE `CourseInfo` SET `course_id`= '{course_id}',`course_name`='{course_name}',`time` = '{time}',`classroom`='{classroom}' ,`teacher_id` = '{teacher_id}' WHERE `course_id` = '{oldId}'".format(
        course_id=course_id, course_name=course_name, time=time, classroom=classroom, teacher_id=teacher_id,
        oldId=oldId)
    db.cursor.execute(sql)
    db.conn.commit()


def select_my_course(key):
    sql = "select * from `CourseInfo` WHERE `teacher_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def select_my_course_grade(key):
    sql = "select t1.course_id,t1.course_name,t2.grade,t2.student_id from `CourseInfo` as t1,`StudentCourse` as t2 where t1.`course_id` = t2.`course_id` and `teacher_id` = '{key}'".format(
        key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def select_all_course_grade():
    sql = "select t1.course_id,t1.course_name,t2.grade,t2.student_id from `CourseInfo` as t1,`StudentCourse` as t2 WHERE t1.course_id = t2.course_id"
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def deleteOne(key):
    sql = "DELETE FROM `CourseInfo` WHERE `course_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    db.conn.commit()
    print("删除{key}成功".format(key=key))


def select_one_course(key):
    sql = "select `course_id`,`course_name`,`time`,`teacher_id`,`classroom` from `CourseInfo` WHERE `course_id` = '{key}'".format(
        key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret
