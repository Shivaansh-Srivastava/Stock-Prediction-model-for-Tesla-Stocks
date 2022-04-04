from flask import Flask, render_template, request
import joblib
import datetime

app=Flask(__name__)
model=joblib.load('model_jlib')

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        d=datetime.date(2010,6,29)
        seld=request.form.get('dates')
        if(seld==''):
            return render_template('home.html',price="Please select a value.")
        l1=seld.split('-')
        nd=datetime.date(int(l1[0]),int(l1[1]),int(l1[2]))
        diff=(nd-d).days
        ans=model.predict([[diff]])
        ans=round(ans[0],2)
        return render_template('home.html',price="The closing price predicted is "+str(ans))

if __name__=='__main__':
    app.run(debug=True)