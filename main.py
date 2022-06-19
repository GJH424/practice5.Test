from flask import Flask, render_template, jsonify, request
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='web_test', charset="utf8")
cursor = db.cursor()

@app.route("/", methods=["GET"])
def hello():
	return "Hello Front-end"

@app.route("/page", methods=["GET"])
def mainPage():
    return render_template('index.html')

#GET API
@app.route("/backend", methods=["GET"])
def get_info():
    cursor.execute("select * from student_score")
    students = cursor.fetchall()
    # print(students)
    info = []
    for s in students:
        info.append({
            'id':s[0],
            'name':s[1],
            'kuk':s[2],
            'su':s[3],
            'eng':s[4]
        })
    return jsonify(info)

#GET API(kuk_sort)
@app.route("/backend/kuk", methods=["GET"])
def kuk_sort():
    cursor.execute("select * from student_score order by kuk desc")
    students = cursor.fetchall()
    # print(students)
    info = []
    for s in students:
        info.append({
            'id':s[0],
            'name':s[1],
            'kuk':s[2],
            'su':s[3],
            'eng':s[4]
        })
    return jsonify(info)

#GET API(eng_sort)
@app.route("/backend/eng", methods=["GET"])
def eng_sort():
    cursor.execute("select * from student_score order by eng desc")
    students = cursor.fetchall()
    # print(students)
    info = []
    for s in students:
        info.append({
            'id':s[0],
            'name':s[1],
            'kuk':s[2],
            'su':s[3],
            'eng':s[4]
        })
    return jsonify(info)

#GET API(su_sort)
@app.route("/backend/su", methods=["GET"])
def su_sort():
    cursor.execute("select * from student_score order by su desc")
    students = cursor.fetchall()
    # print(students)
    info = []
    for s in students:
        info.append({
            'id':s[0],
            'name':s[1],
            'kuk':s[2],
            'su':s[3],
            'eng':s[4]
        })
    return jsonify(info)


#POST API(학생 저장)
@app.route("/backend", methods=["POST"])
def save():
    name = request.form['name']
    kuk = request.form['kuk']
    su = request.form['su']
    eng = request.form['eng']
    cursor.execute(f"insert into student_score (name, kuk, eng, su) values ('{name}', {kuk}, {eng}, {su})")
    db.commit()
    return "POST API"

#DELETE API(학생 삭제)
@app.route("/backend", methods=["DELETE"])
def delete():
    name = request.args.get('name')
    cursor.execute(f"delete from student_score where name='{name}'")
    db.commit()
    return "DELETE API"

#PUT API(학생 수정)
@app.route("/backend", methods=["PUT"])
def put():
    name = request.form['name']
    kuk = request.form['kuk']
    su = request.form['su']
    eng = request.form['eng']
    cursor.execute(f"update student_score set kuk={kuk}, su={su}, eng={eng} where name='{name}'")
    db.commit()
    return "PUT API"

if __name__ == "__main__":
    app.run(debug=True)
