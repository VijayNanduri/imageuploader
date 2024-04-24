from flask import Flask, request, send_from_directory, render_template
import os

app = Flask(__name__, template_folder='.')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Get the list of filenames from the uploads folder
    uploads_dir = os.path.join(app.config['UPLOAD_FOLDER'])
    filenames = os.listdir(uploads_dir)
    # Pass the list of filenames to the template
    return render_template('index.html', filenames=filenames)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        print("Saving file to:", filename)  # Add this line for debugging
        return 'File uploaded successfully.'
    return 'No file uploaded.'


@app.route('/clear', methods=['POST'])
def clear_files():
    # Remove files from the uploads folder
    uploads_dir = os.path.join(app.config['UPLOAD_FOLDER'])
    for filename in os.listdir(uploads_dir):
        file_path = os.path.join(uploads_dir, filename)
        os.remove(file_path)

    # Clear the imageContainer by returning an empty response
    return 'cleared images'



@app.route('/<path:path>')
def static_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
