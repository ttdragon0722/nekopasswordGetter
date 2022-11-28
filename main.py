from flask import Flask,render_template,request
from passwordGetter.getpassword import get

app = Flask(__name__,template_folder="templates")


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/exe",methods=["POST"])
def exe():
    if request.method == "POST":
        return get()


app.run(host='0.0.0.0', port=81)
