from flask import Flask,render_template

app=Flask(__name__)

@app.route("/pageone")
def one():
    return render_template("firstpage.html")

@app.route("/pagetwo")
def two():
    return render_template("secondpage.html")


if __name__=="__main__":
    app.run()