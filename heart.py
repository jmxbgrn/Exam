from flask import Flask, jsonify, request
app = Flask(__name__)
newRate = [
    {

    "1": {"heart_id": 1, "date": "2023-11-29", "heart_rate": 75},
    "2": {"heart_id": 2, "date": "2023-11-30", "heart_rate": 80},
    "3": {"heart_id": 3, "date": "2023-12-01", "heart_rate": 70}
}

]
@app.route('/newRate', methods=['Get'])
def getnewHeart():
	return jsonify(newRate)

if __name__=='__main__':
    app.run()
