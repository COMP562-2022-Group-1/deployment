from pandas import DataFrame
from flask import Flask, render_template, send_from_directory, request
from constants import model, most_common_output, keys, result_mapping


app = Flask(__name__)


def convert_results_to_input(results: dict[str, int]):
    temp = {}
    for key in keys:
        if key in results:
            temp[key] = int(results[key])
            continue
        temp[key] = most_common_output[key]
    return DataFrame.from_dict(temp, orient="index").T


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submission", methods=["POST"])
def submission():
    global model
    results = request.form
    r = model.predict(convert_results_to_input(results))
    result = f"You are most likely to vote {result_mapping[r[0]]}."

    return render_template("result.html", result=result)


@app.route("/assets/<path:path>")
def send_js(path):
    return send_from_directory("assets", path)


if __name__ == "__main__":
    app.run()
