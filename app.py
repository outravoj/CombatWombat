from flask import Flask, render_template, request
from API.wombo_api import generateWomboPath


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cora_design.html')
    #imagePathList = ['Programming.JPG']
    #return render_template('home.html', imageList=imagePathList)

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        try:
            imagePath = generateWomboPath(form_data)
        except:
            return render_template('cora_design.html')
        return render_template('result_page.html',imagePath=imagePath, form_data_passed=form_data)

if __name__ == '__main__':
    app.run()