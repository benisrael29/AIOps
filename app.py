from flask import Flask, request,render_template
app = Flask(__name__)



@app.route('/', methods = ["POST","GET"])
def getHello():
    if request.method == 'POST':
        user = request.form["entry"]
        return(str(user))        
    else:
        return app.send_static_file('main.html')

@app.route('/main')
def getMain():
    return render_template("./main.html")

@app.route('/about')
def getAbout(): 
    return ('Artificial Intelligence for IT Operations (AIOps) is a term coined by Gartner in 2016 as an industry category for machine learning analytics technology that enhances IT operations analytics.')

@app.route("/hello")
def hello():
    return ("Hello, AIOps Team!")

@app.route("/test")
def test():
    return ("Testing is fun!!")

#token
@app.route("/loaderio-cf29df6bc3ec7151c1e535b12a47a968.txt")
def loader():
    return ('loaderio-cf29df6bc3ec7151c1e535b12a47a968.txt')
