from flask import Flask
from flask import send_file
from flask import request
import shutil
import os

app = Flask(__name__)

@app.route("/")
def generateProject():
    myCmd = 'mn create-app '
    
    name = request.args.get('name')
    lang = request.args.get('lang')
    build = request.args.get('build')
    features = request.args.get('features')

    if name: myCmd += name
    if lang: myCmd += ' -l ' + lang
    if build: myCmd += ' -b ' + build
    if features: myCmd += ' -f ' + features

    os.system(myCmd)
    shutil.make_archive(name, 'zip', name)
    shutil.rmtree('./' + name)
    path = './' + name + '.zip'
    
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')