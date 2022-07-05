import collections

from flask import Blueprint, jsonify, render_template, request

import dbInfo.classInfo as claInfo
import dbInfo.courseInfo as couInfo
import dbInfo.gradeInfo as graInfo
import dbInfo.studentInfo as stuInfo
import dbInfo.teacherInfo as teaInfo

admin = Blueprint('admin', __name__, template_folder="templates", static_folder="static")


############################学生信息#############################


@admin.route("/admin/json/student")
def admin_student_info():  # 学生信息接口
    list = stuInfo.select()
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@admin.route("/admin/student")
def to_admin_student():  # 返回管理员学生信息页面
    return render_template("admin_studentinfo.html")


@admin.route("/admin/student/delete/<id>")
def admin_delete_student(id=None):
    # graInfo.deleteOne(id)
    stuInfo.deleteOne(id)
    return jsonify({'success': 1, 'msg': "数据删除成功！"})


@admin.post("/admin/student/edit")
def admin_edit_student():  # 编辑学生信息
    post_data = request.form.to_dict()
    if stuInfo.select_my_info(post_data["student_id"]) and post_data["student_id"] != post_data[
        "oldId"]:  # 如果新输入的学生id不为空且更改了id，则说明id重复
        return jsonify({'success': 0, 'msg': "学生id重复！"})
    elif not claInfo.select_class(post_data["class_id"]):
        return jsonify({'success': 0, 'msg': "输入班级不存在！"})

    stuInfo.update_all(post_data["student_id"], post_data["oldId"], post_data["student_name"],
                       post_data["class_id"], post_data["age"], post_data["sex"])
    print(post_data)
    return jsonify({'success': 1, 'msg': "数据编辑成功！"})


@admin.post("/admin/student/add")
def admin_add_student():  # 录入学生信息
    post_data = request.form.to_dict()
    if stuInfo.select_my_info(post_data["student_id"]):
        return jsonify({'success': 0, 'msg': "学生id重复！"})
    elif not claInfo.select_class(post_data["class_id"]):
        return jsonify({'success': 0, 'msg': "输入班级不存在！"})
    student = stuInfo.StudentInfo([post_data["student_id"], post_data["student_name"],
                                   post_data["class_id"], int(post_data["age"]), post_data["sex"],
                                   "123456"])
    student.save_student()
    return jsonify({'success': 1, 'msg': "数据录入成功！"})


#############################老师信息#############################

@admin.post("/admin/teacher/add")
def admin_add_teacher():  # 录入老师信息
    post_data = request.form.to_dict()
    print(post_data)

    if teaInfo.select_my_info(post_data["teacher_id"]):
        return jsonify({'success': 0, 'msg': "老师id重复！"})
    teacher = teaInfo.TeacherInfo([post_data["teacher_id"], post_data["teacher_name"],
                                   int(post_data["teacher_age"]), post_data["teacher_sex"], "123456"])
    teacher.save_teacher()
    return jsonify({'success': 1, 'msg': "数据录入成功！"})


@admin.post("/admin/teacher/edit")
def admin_edit_teacher():  # 编辑老师信息
    post_data = request.form.to_dict()
    if teaInfo.select_my_info(post_data["teacher_id"]) and post_data["teacher_id"] != post_data[
        "oldId"]:  # 如果新输入的老师id不为空且更改了id，则说明id重复
        return jsonify({'success': 0, 'msg': "学生id重复！"})
    print(post_data)
    teaInfo.update_all(post_data["teacher_id"], post_data["oldId"], post_data["teacher_name"], post_data["teacher_age"],
                       post_data["teacher_sex"])
    print(post_data)
    return jsonify({'success': 1, 'msg': "数据编辑成功！"})


@admin.route("/admin/json/teacher")
def admin_teacher_info():  # 老师信息接口
    list = teaInfo.select()
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@admin.route("/admin/teacher")
def to_admin_teacher():  # 返回管理员老师信息页面
    return render_template("admin_teacherinfo.html")


@admin.route("/admin/teacher/delete/<id>")
def admin_delete_teacher(id=None):
    # graInfo.deleteOne(id)
    teaInfo.deleteOne(id)
    return jsonify({'success': 1, 'msg': "数据删除成功！"})


#############################班级信息#############################


@admin.route("/admin/json/class")
def admin_class_info():  # 班级信息接口
    list = claInfo.select()
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@admin.route("/admin/class")
def to_admin_class():  # 返回班级信息页面
    return render_template("admin_classinfo.html")


@admin.route("/admin/class/delete/<id>")
def admin_delete_class(id=None):
    # graInfo.deleteOne(id)
    claInfo.deleteOne(id)
    return jsonify({'success': 1, 'msg': "数据删除成功！"})


@admin.post("/admin/class/edit")
def admin_edit_class():  # 编辑老师信息
    post_data = request.form.to_dict()
    if claInfo.select_class(post_data["class_id"]) and post_data["class_id"] != post_data[
        "oldId"]:  # 如果新输入的老师id不为空且更改了id，则说明id重复
        return jsonify({'success': 0, 'msg': "课程id重复！"})
    claInfo.update_all(post_data["class_id"], post_data["oldId"], post_data["class_name"],
                       post_data["professional_name"])
    print(post_data)
    return jsonify({'success': 1, 'msg': "数据编辑成功！"})


@admin.post("/admin/class/add")
def admin_add_class():  # 录入学生信息
    post_data = request.form.to_dict()
    if claInfo.select_class(post_data["class_id"]):
        return jsonify({'success': 0, 'msg': "课程id重复！"})

    class_ex = claInfo.ClassInfo([post_data["class_id"], post_data["class_name"],
                                  post_data["professional_name"]])
    class_ex.save_class()
    return jsonify({'success': 1, 'msg': "数据录入成功！"})


#############################课程信息############################

@admin.route("/admin/json/course")
def admin_course_info():  # 班级信息接口
    list = couInfo.select()
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@admin.route("/admin/course")
def to_admin_course():  # 返回班级信息页面
    return render_template("admin_courseinfo.html")


@admin.route("/admin/course/delete/<id>")
def admin_delete_course(id=None):
    # graInfo.deleteOne(id)
    couInfo.deleteOne(id)
    return jsonify({'success': 1, 'msg': "数据删除成功！"})


@admin.post("/admin/course/edit")
def admin_edit_course():  # 编辑老师信息
    post_data = request.form.to_dict()
    if couInfo.select_one_course(post_data["course_id"]) and post_data["course_id"] != post_data[
        "oldId"]:  # 如果新输入的老师id不为空且更改了id，则说明id重复
        return jsonify({'success': 0, 'msg': "课程id重复！"})
    couInfo.update_all(post_data["course_id"], post_data["course_name"], post_data["time"],
                       post_data["classroom"], post_data["teacher_id"], post_data["oldId"])
    print(post_data)
    return jsonify({'success': 1, 'msg': "数据编辑成功！"})


@admin.post("/admin/course/add")
def admin_add_course():  # 录入学生信息
    post_data = request.form.to_dict()
    if couInfo.select_one_course(post_data["course_id"]):
        return jsonify({'success': 0, 'msg': "课程id重复！"})
    elif not teaInfo.select_my_info(post_data["teacher_id"]):
        return jsonify({'success': 0, 'msg': "输入老师不存在！"})
    course_ex = couInfo.CourseInfo([post_data["course_id"], post_data["course_name"], post_data["time"],
                                    post_data["classroom"], post_data["teacher_id"]])
    course_ex.save_course()
    return jsonify({'success': 1, 'msg': "数据录入成功！"})


#############################成绩信息#############################


@admin.route("/admin/json/grade")
def admin_grade_info():  # 班级信息接口
    list = graInfo.select_all()
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@admin.route("/admin/grade")
def to_admin_grade():  # 返回班级信息页面
    return render_template("admin_studentcourse.html")


@admin.route("/admin/grade/delete/<string:id>")
def admin_delete_grade(id=None):
    id = str(id)
    new_list = id.split('&')
    student_id, course_id = new_list[0], new_list[1]
    # graInfo.deleteOne(id)
    graInfo.deleteOne(student_id, course_id)
    return jsonify({'success': 1, 'msg': "数据删除成功！"})


@admin.post("/admin/grade/edit")
def admin_edit_grade():  # 编辑成绩信息
    post_data = request.form.to_dict()

    graInfo.update_all(post_data["student_id"], post_data["course_id"], post_data["grade"])
    print(post_data)
    return jsonify({'success': 1, 'msg': "数据编辑成功！"})


@admin.post("/admin/grade/add")
def admin_add_grade():  # 录入学生信息
    post_data = request.form.to_dict()
    if graInfo.select_one_grade(post_data["student_id"], post_data["course_id"]):
        return jsonify({'success': 0, 'msg': "课程成绩重复！"})
    elif not stuInfo.select_my_info(post_data["student_id"]):
        return jsonify({'success': 0, 'msg': "输入学生不存在！"})
    elif not couInfo.select_one_course(post_data["course_id"]):
        return jsonify({'success': 0, 'msg': "输入课程不存在！"})
    grade_ex = graInfo.GradeInfo([post_data["student_id"], post_data["course_id"], post_data["grade"]])
    grade_ex.save_grade()
    return jsonify({'success': 1, 'msg': "数据录入成功！"})


#############################系统配置#############################

@admin.route("/admin/json/system")
def admin_system_info():  # 系统配置接口
    list = stuInfo.select_password()

    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@admin.route("/admin/system")
def to_admin_system():  # 返回班级信息页面
    return render_template("system.html")


@admin.route("/admin/system/delete/<string:id>")
def admin_delete_system(id=None):
    # graInfo.deleteOne(id)
    if stuInfo.select_my_info(id):
        print("这是学生id")
        stuInfo.deleteOne(id)
    else:
        teaInfo.deleteOne(id)
    return jsonify({'success': 1, 'msg': "数据删除成功！"})


@admin.post("/admin/system/edit")
def admin_edit_system():  # 编辑密码
    post_data = request.form.to_dict()
    id, password = post_data["id"], post_data["password"]
    if stuInfo.select_my_info(id):
        print("这是学生id")
        stuInfo.update_password(id, password)
    else:
        print("这是老师id")
        teaInfo.update_password(id, password)
    return jsonify({'success': 1, 'msg': "密码修改成功！"})


# @admin.post("/admin/system/add")
# def admin_add_system():
#     post_data = request.form.to_dict()
#     id, password, kind = post_data["id"], post_data["password"], post_data["kind"]
#     if kind == "学生":
#         if stuInfo.select_my_info(id):
#             return jsonify({'success': 0, 'msg': "该学生已存在！"})
#         else:
@admin.route("/admin/statistics")
def to_statistics():
    return render_template("admin_statistics.html")


@admin.route("/admin/json/statistics")
def send_json():
    ls = couInfo.select_all_course_grade()
    dic = collections.defaultdict(list)
    for i in ls:
        dic[i["course_name"]].append(i["grade"])

    data = {'success': 1, "code": 0, "msg": "", "count": len(ls), "page": "true", "data": dic}

    return jsonify(data)
