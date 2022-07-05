from flask import Flask, jsonify, request, redirect, render_template

import dbInfo.db as db
import dbInfo.studentInfo as stuInfo
import login_info
from admin import admin
from loginController import login
from student import student
from teacher import teacher

app = Flask(__name__, template_folder="./templates", static_folder="./static")

app.register_blueprint(student)
app.register_blueprint(teacher)
app.register_blueprint(admin)
app.register_blueprint(login)
db.init()


@app.route('/')
def hello_world():  # put application's code here
    return redirect("/login")


@app.before_request
def before():
    url = request.url
    passUrl = ["http://127.0.0.1:5000/login", "http://127.0.0.1:5000/static/*"]
    print(url)
    if url in passUrl or "static" in url:
        pass
    else:
        if login_info.my_id == "":
            return render_template("login.html")
        else:
            pass


@app.get('/test/table/demo1.json')
def returnJson():
    list = stuInfo.select()
    print(list)
    data = {"code": 0, "msg": "", "count": len(list), "page": "true", "data": list}
    return jsonify(data)


@app.get('/delete/<parse>')
def delete(parse=None):
    print(parse)
    # stuInfo.deleteOne(parse)
    return jsonify({'success': 1, 'msg': '删除成功！'})


@app.post('/add')
def add():
    data = request.form
    print(data)
    return jsonify({'msg': '数据接收成功'})


@app.post('/edit')
def edit():
    data = request.form

    return jsonify({'msg': '数据接收成功'})


if __name__ == '__main__':
    app.run()
