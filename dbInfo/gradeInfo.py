import dbInfo.db as db


class GradeInfo:
    student_id: str
    course_id: str
    grade: int

    def __init__(self, mes):
        self.student_id = mes[0]
        self.course_id = mes[1]
        self.grade = mes[2]

    def save_course(self):
        sql = "INSERT INTO `StudentCourse` (`student_id`, `course_id`, `grade`) VALUES ('{student_id}', '{course_id}', '{grade}')".format(
            student_id=self.student_id, course_id=self.course_id, grade=self.grade, )
        db.cursor.execute(sql)
        db.conn.commit()


def select_one_grade(key):
    sql = "select `student_id`,`course_name`,`grade` from `StudentCourse` natural join `StudentInfo` natural join `CourseInfo`" \
          "where `student_id` = '{key}'".format(key=key)
    db.cursor.execute(sql)
    ret = db.cursor.fetchall()
    return ret
