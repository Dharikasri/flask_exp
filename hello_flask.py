from flask import Flask,render_template,request,redirect

app=Flask(__name__)

@app.route("/postinput")
def input():
    return render_template("postinput.html")

@app.route("/poststatus",methods=["POST"])
def status(): 
    status = request.form["textinput"]
    print(status)
    return render_template("poststatus.html",status=status)
    
if __name__=="__main__":
    app.run()