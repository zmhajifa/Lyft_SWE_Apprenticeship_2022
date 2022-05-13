from flask import Flask, request

app = Flask(__name__)


@app.route('/test', methods=["POST"])
def string_slicing():
    """ Method to get string from POST request and
    return every 3rd letter """

    data = {"string_to_cut": request.json["string_to_cut"]}
    if len(data["string_to_cut"]) < 3:
        return {"return_string": "error, string length less than 3"}
    else:
        sliced_string = data["string_to_cut"][2::3]
        return {"return_string": sliced_string}


if __name__ == '__main__':
    app.run()

# curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'