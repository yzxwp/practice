# encoding:utf-8
from flask import Flask, request, jsonify

app = Flask(__name__)


# @app.route('/login/<condition>', methods=['GET'])
@app.route('/login/<condition>', methods=['POST', 'GET'])
def login_in(condition=None):
    tel = None
    if request.method == "GET":
        tel = condition.split('_')[-1]
        if condition.startswith("tel_"):
            if len(tel) == 11 or len(tel) == 4:
                tel = {"tell": tel, "code": 200}
            else:
                tel = {"tell": "不存在", "code": 400}
    elif request.method == "POST":
        tel = request.form['tel']
        if tel != None:
            if len(tel) == 11 or len(tel) == 4:
                tel = {"tell": tel, "code": 200}
            else:
                tel = {"tell": "不存在", "code": 400}
        else:
            tel = {"tell": "不存在", "code": 400}
    return jsonify(tel)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80)
