from flask import Flask, render_template, request
from API.wombo_api import generateWomboPath


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')
    #imagePathList = ['Programming.JPG']
    #return render_template('home.html', imageList=imagePathList)

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        imagePathList = [generateWomboPath(form_data['Title'])]
        return render_template('homealt.html',imageList=imagePathList)

if __name__ == '__main__':
    app.run()