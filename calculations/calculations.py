from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/v1/double/<number>", methods=["GET"])
def get_double(number):
    """
    :param number: a numeric value passed in the path
    :return: See specification.yaml -- a json with code, type and result where result is 2 times the number
    """
    try:
        result = float(number) * 2
        response = {"code": "200", "type": "OK", "result": result}

    except ValueError:
        response = {"code": "400", "type": "BAD REQUEST"}
    return jsonify(response)


if __name__ == "__main__":
    app.run()
