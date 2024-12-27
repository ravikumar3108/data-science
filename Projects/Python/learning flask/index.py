# Flask App Routing 

from flask import Flask , render_template,request,url_for,redirect

# create a simple flask application 
# __name__ is the entry point of our app 
app = Flask(__name__)

#  this is decorator @app
@app.route("/",methods=["GET"])
def HomePage():
    return "Heloo World"

@app.route("/index",methods=["GET"])
def Index():
    return "Heloo Welcome to Index Page"

#  variable rules 

@app.route("/success/<int:marks>",methods=["GET"])
def success(marks):
    return "My Score is" + str(marks)


@app.route("/fail/<int:marks>",methods=["GET"])
def fail(marks):
    return "My Score is" + str(marks)


# render a Html page 
@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        math = float(request.form['math'])
        science = float(request.form['science'])

        average = (math + science)/2

        result = ""
        if average >=50:
                result="success"
        else:
            result="fail"

        return redirect(url_for(result,marks=average))
    


if __name__ == "__main__":
    app.run(debug=True)
# 