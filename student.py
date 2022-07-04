from flask import Blueprint, render_template, jsonify

import dbInfo.studentInfo as stuInfo

student = Blueprint('student', __name__, template_folder="templates", static_folder="static")


@student.route("/student/info/json/<string:id>")
def student_info_json(id=None):  # 学生信息接口
    print(id)
    list = stuInfo.select_my_info(id)
    print(list)
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@student.route("/student/grade/json/<string:id>")
def student_grade_info(id=None):  # 选课成绩接口
    print(id)
    list = stuInfo.select_my_grade(id)
    print(list)
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@student.route("/student/info/<string:id>")
def show_student(id=None):
    print(id)
    return render_template("student_studentinfo.html")


@student.route("/student/grade/<string:id>")
def show_student_grade(id=None):
    print(id)
    return render_template("student_studentcourse.html")
