from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/v1/double/<number>', methods=["GET"])
def get_double(number):
    try:
        result = float(number) * 2
        response = {"code":"200", "type":"OK", "result":result}
    except ValueError:
        response = {"code":"400", "type":"BAD REQUEST"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0")