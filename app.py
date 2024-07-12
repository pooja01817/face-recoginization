from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = r'C:\Users\OneDrive\Documents\face_rec\images' //use ur own path  where ur images file is stored
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html', success=False)

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    name = request.form.get('name', '').strip()
    if not name or file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        file_extension = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{name}.{file_extension}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('upload.html', success=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
