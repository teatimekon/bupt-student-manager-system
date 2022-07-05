from flask import Blueprint, request, render_template, jsonify

import login_info
from dbInfo import db

login = Blueprint('login', __name__, template_folder="templates", static_folder="static")


@login.get("/login")
def init_login():
    login_info.my_id = ""
    return render_template("login.html")


@login.post("/login")
def login_check():
    data = request.form
    user_id = data.get("userid")
    password = data.get("password")
    kind = data.get("identity")
    print(user_id, password, kind)
    if kind == "admin" and user_id != "admin" and password != "admin":  # 管理员特殊登陆
        mess = "账号或密码错误！请重试！"
        return jsonify({'success': 0, 'msg': mess})
    elif kind == "admin" and user_id == "admin" and password == "admin":
        login_info.my_id = "admin"
        return jsonify({'success': 1, 'msg': "管理员登陆成功"})
    stu_sql = "select `student_id`,`password` from `StudentInfo`"
    db.cursor.execute(stu_sql)
    stu_ret = db.cursor.fetchall()
    tea_sql = "select `teacher_id`,`password` from `TeacherInfo`"
    db.cursor.execute(tea_sql)
    tea_ret = db.cursor.fetchall()
    if kind == "student":
        for i in stu_ret:
            if i["student_id"] == user_id and i["password"] == password:  # 登陆成功，其余都是登陆失败
                login_info.my_id = user_id  # 存当前登陆id
                return jsonify({'success': 1, 'msg': '登陆成功'})
    elif kind == "teacher":
        for i in tea_ret:
            if i["teacher_id"] == user_id and i["password"] == password:  # 登陆成功，其余都是登陆失败
                login_info.my_id = user_id  # 存当前登陆id
                return jsonify({'success': 1, 'msg': '登陆成功'})
    return jsonify({'success': 0, 'msg': '账号或密码错误！请重试！'})
