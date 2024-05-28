from flask import Flask,render_template, request
import joblib

#initialise the app
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/submit',methods=['post'])
def submit():

    #load the model
    model=joblib.load('diabetes_79.pkl')

    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    predi=request.form.get('predi')
    age=request.form.get('age')

    print(preg,plas,pres,skin,test,mass,predi,age)

    output=model.predict([[preg,plas,pres,skin,test,mass,predi,age]])
    
    if output[0]==0:
        data='person is not diabatic'
    else:
        data='person is diabatic'
    
    return render_template('predict.html', data=data)

if __name__=="__main__":
    app.run(debug=True)