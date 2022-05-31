from flask import Flask, render_template, url_for, request
from langdetect import detect

app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = detect(output["name"])


    return render_template('index.html', name = name)
    




if __name__ == "__main__":
    app.run(debug=True)