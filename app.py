from re import template
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("home.html")

print(__name__)
if (__name__ == "__main__" ) :
  print ("Inside if ")
  app.run(host="0.0.0.0",port=8080, debug=True)