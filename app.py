from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/article")
def article():
    return render_template("article.html")

@app.route("/test")
def test():
	return render_template("tester.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
    app.debug = True
