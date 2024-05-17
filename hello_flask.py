from flask import Flask,render_template,request,redirect

app=Flask(__name__)

@app.route("/inputpage")
def input():
    return render_template("inputpage.html")

@app.route("/statuspage",methods=["GET"])
def status():
    status=request.args.get('textinput')
    return render_template("statuspage.html",status=status)
    
if __name__=="__main__":
    app.run()