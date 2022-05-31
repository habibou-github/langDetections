from flask import Flask, render_template, url_for, request
from langdetect import detect
all_language_codes = {
      "en": "English",
      "fr": "French",
      "ar": "Arabic",
      "de": "Germane",
      "ru": "Russian"
}

app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    out = output["name"]
    name = ''
    if out:
        lang = detect(out)
        name = all_language_codes.get(lang)




    return render_template('index.html', name = name, out = out)
    




if __name__ == "__main__":
    app.run(debug=True)