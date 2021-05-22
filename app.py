from flask import Flask,render_template,request,flash,redirect,url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'E:/python/Diabetic_retina_deployment'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join("E:/python/Diabetic_retina_deployment/", file.filename))
        return render_template('upload.html',message="success")
    return render_template('upload.html',message="uplaod")

if __name__=="__main__":
    app.run(debug=True)
    app.config["TEMPLATES_AND_RELOAD"]==True
