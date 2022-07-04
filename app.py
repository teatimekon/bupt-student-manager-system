from flask import Flask, render_template, jsonify, request

import dbInfo.db as db
import dbInfo.studentInfo as stuInfo
from admin import manager
from loginController import login
from student import student
from teacher import teacher

app = Flask(__name__, template_folder="./templates", static_folder="./static")

app.register_blueprint(student)
app.register_blueprint(teacher)
app.register_blueprint(manager)
app.register_blueprint(login)
db.init()


@app.route('/')
def hello_world():  # put application's code here
    return render_template("hello.html")


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
