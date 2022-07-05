import dbInfo.db as db


class GradeInfo:
    student_id: str
    course_id: str
    grade: int

    def __init__(self, mes):
        self.student_id = mes[0]
        self.course_id = mes[1]
        self.grade = mes[2]

    def save_grade(self):
        sql = "INSERT INTO `StudentCourse` (`student_id`, `course_id`, `grade`) VALUES ('{student_id}', '{course_id}', '{grade}')".format(
            student_id=self.student_id, course_id=self.course_id, grade=self.grade)
        db.cursor.execute(sql)
        db.conn.commit()


def select_one_grade(student_id, course_id):
    sql = "select * from `StudentCourse` where `student_id` = '{student_id}' and `course_id` = '{course_id}'".format(
        student_id=student_id,
        course_id=course_id)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def update_all(stu_key, cou_key, grade):
    sql = "UPDATE `StudentCourse` SET `grade` = '{grade}' WHERE `student_id` = '{stu_key}' and `course_id` = '{cou_key}'".format(
        grade=grade, stu_key=stu_key, cou_key=cou_key)
    db.cursor.execute(sql)
    db.conn.commit()


def select_all():
    sql = "select t1.`student_id`,t3.`student_name`,t1.`course_id`,t2.`course_name`,t1.`grade` from `StudentCourse` as t1, `CourseInfo` as t2 ,`StudentInfo` as t3  WHERE t1.student_id = t3.student_id and t2.course_id = t1.course_id"
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret


def deleteOne(stu_key, cou_key):
    sql = "DELETE FROM `StudentCourse` WHERE `student_id` = '{stu_key}' and `course_id` = '{cou_key}'".format(
        stu_key=stu_key, cou_key=cou_key)
    db.cursor.execute(sql)
    db.conn.commit()
