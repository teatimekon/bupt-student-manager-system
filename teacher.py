import collections

from flask import Blueprint, request, jsonify, render_template

import dbInfo.courseInfo as couInfo
import dbInfo.gradeInfo as graInfo
import dbInfo.studentInfo as stuInfo
import dbInfo.teacherInfo as teaInfo

teacher = Blueprint('teacher', __name__, template_folder="templates", static_folder="static")


@teacher.route("/teacher/json/info/<id>")
def show_teacher_json(id=None):  # 展示信息接口
    list = teaInfo.select_my_info(id)
    print(list)
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@teacher.route("/teacher/info/<id>")
def show_teacher(id=None):  # 展示老师信息
    return render_template("teacher_teacherinfo.html")


@teacher.route("/teacher/json/grade/<id>")
def show_student_grade_json(id=None):
    print(id)
    list = teaInfo.select_my_student_grade(id)
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@teacher.route("/teacher/grade/<id>")
def show_student_grade(id=None):  # 展示老师教的学生的信息
    return render_template("teacher_studentinfo.html")


@teacher.route("/teacher/json/courseinfo/<id>")
def show_course_info(id=None):  # 展示老师教的课程的信息
    list = couInfo.select_my_course(id)
    print(list)
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@teacher.route("/teacher/courseinfo/<id>")
def show_course(id=None):  # 展示老师教的课程的信息

    return render_template("teacher_courseinfo.html")


@teacher.post("/teacher/edit")
def edit_student_info():
    post_data = request.form.to_dict()
    print(post_data)
    teaInfo.edit_grade(post_data["student_id"], post_data["course_id"], post_data["grade"])
    return jsonify({'success': 1, 'msg': '数据修改成功！'})


@teacher.post("/teacher/add")
def add_student_info():
    post_data = request.form.to_dict()

    if post_data["student_name"] != stuInfo.select_my_info(post_data["student_id"])[0]["student_name"]:
        return jsonify({'success': 0, 'msg': '姓名与学号不一致，对应姓名为{name}请重新录入！'.format(
            name=stuInfo.select_my_info(post_data["student_id"])[0]["student_name"])})
    elif post_data["course_name"] != couInfo.select_one_course(post_data["course_id"])[0]["course_name"]:
        return jsonify({'success': 0, 'msg': "课程ID与课程名不一致，对应名字为{name}请重新录入！".format(
            name=couInfo.select_one_course(post_data["course_id"])[0]["course_name"])})
    grade = graInfo.GradeInfo([post_data["student_id"], post_data["course_id"], post_data["grade"]])
    grade.save_grade()

    return jsonify({'success': 1, 'msg': '数据录入成功！'})


@teacher.route("/teacher/statistics/<id>")
def to_statistics(id=None):
    return render_template("teacher_statistics.html")


@teacher.route("/teacher/json/statistics/<id>")
def send_json(id=None):
    ls = couInfo.select_my_course_grade(id)
    print(ls)
    dic = collections.defaultdict(list)
    for i in ls:
        dic[i["course_name"]].append(i["grade"])

    data = {'success': 1, "code": 0, "msg": "", "count": len(ls), "page": "true", "data": dic}

    return jsonify(data)
