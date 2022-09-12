import pandas as pd
from flask import Flask, render_template, request, app
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
import pickle

app=Flask(__name__)

data=pd.read_csv('Admission_Predict_Ver1.1.csv')
pipe = pickle.load(open("LinearRegressionModel.pkl",'rb'))
@app.route("/")
def index():
    researches = sorted(data['Research'].unique())
    return render_template('index.html', researches = researches)

@app.route('/predict', methods=['POST'])
def predict():
    gre = request.form.get('gre')
    toefl = request.form.get('toefl')
    cgpa = request.form.get('CGPA')
    sop = request.form.get('SOP')
    lor = request.form.get('LOR')
    univ = request.form.get('univ')
    research = request.form.get('research')
    print(gre, toefl,cgpa,sop,lor,univ, research)
    input = pd.DataFrame([[gre,toefl, univ,sop,lor,cgpa,research]],columns=['GRE_Score','TOEFL_Score','Univ_Rating','SOP', 'LOR','CGPA','Research'])
    prediction = pipe.predict(input)[0]
    result = prediction*100
    return str(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, port=5000)
