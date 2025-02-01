from flask import Flask , render_template,url_for

app  = Flask(__name__)


# Routing 
def index():
    return render_template("index.html")


@app.route("/",methods=["GET"])
@app.route("/home",methods=["GET"])
def home():
    return render_template("Home.html")

@app.route("/studentform")
def StudentForm():
    return render_template('StudentForm.html')

@app.route("/studentrecord")
def StudentRecord():
    return render_template('StudentRecord.html')







if __name__ == "__main__":
    app.run(debug=True)