from flask import Flask, render_template, send_from_directory, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submission", methods=["POST"])
def submission():
    results = request.form
    ## Todo: Use the model and save it
    print(results)
    result = "The model is still training, please come back in the future when it is completed."

    return render_template("result.html", result=result)


@app.route("/assets/<path:path>")
def send_js(path):
    return send_from_directory("assets", path)


if __name__ == "__main__":
    app.run()
