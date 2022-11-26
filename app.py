from flask import Flask, render_template, request
import csv
import io
import joblib

nb_model = joblib.load('models/dectree.joblib')
dt_model = joblib.load('models/naiveb.joblib')

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

outcomes = ['<=50K', '>50K']

@app.route('/')
def index(name=None):
    return render_template("index.html")

@app.post('/result')
def result():
    data = request.form
    age = request.form.get('age')
    sex = request.form.get('sex')
    bp = request.form.get('bp')
    cholesterol = request.form.get('cholesterol')
    natk = request.form.get('natk')
    classifier = request.form.get('classifier')
    
    test_input = request.files.get('test_input_file')
    test_input.stream.seek(0)
    test_stream = io.StringIO(test_input.stream.read().decode('UTF8'))
    csv_reader = csv.DictReader(test_stream, delimiter=',', quotechar='"')
    for row in csv_reader:
        age = row['age']
        sex = row['sex']
        bp = row['bp']
        cholesterol = row['cholesterol']
        natk = row['sodium to potasium ratio']

    return f'Age: {age}, Sex: {sex}, BP: {bp}, Cholesterol: {cholesterol}, Sodium to Potassium Ratio: {natk}, Classifier: {classifier}'