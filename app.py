from flask import Flask, render_template, request, redirect, jsonify, session


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
    
