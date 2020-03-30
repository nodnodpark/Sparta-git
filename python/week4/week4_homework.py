from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template("homework.html")

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def buyClick():
    #클라이언트가 입력한거 가져오기
    name = request.form["name_give"]
    number = request.form["number_give"]
    address = request.form["address_give"]
    phone = request.form["phone_give"]

    print(name)
    print(number)
    print(address)
    print(phone)

    #db에 정보삽입
    db.orderCollection.insert_one({
        "name": name,
        "number": number,
        "address": address,
        "phone": phone
    })

    return jsonify({'result':'success', 'msg': '주문완료!'})


@app.route('/orders', methods=['GET'])
def read_orders():
    # 1. DB에서 리뷰 정보 모두 가져오기
    orders = list(db.orderCollection.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)