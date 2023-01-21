from flask import Flask,jsonify


app = Flask(__name__)   #noqa : F821
@app.route('/')
def home():
    return jsonify({"message":"This api is working"}) 

if __name__=="__main__":   #noqa : F821
    app.run(debug=False)    