import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import random

app = Flask(__name__)
model = pickle.load(open('ipython/model.pkl', 'rb'))
details = []
@app.route('/')  
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
  
    count = 0

    details = []
    for i in request.form.values():
        details.append(i)
    print("details is ",details)
    d_copy = []
    nam = details.pop(0)
    for ii in range(0,12):
        if ii == 1:
            d_copy.insert(ii,int(details[1]))  
        elif ii == 0:
            if details[0] == 'F' or 'f':
                d_copy.insert(ii,0)
            else:
                d_copy.insert(ii,1)
        elif ii == 2:
            chk = random.randint(0,1)
            d_copy.insert(ii,chk)
        
        elif ii == 3:
            d_copy.insert(ii,int(details[2]))
        
        elif ii == 4:
            chk = random.randint(0,1)
            d_copy.insert(ii,chk)
        elif ii == 5:
            chk = random.randint(0,2)
            d_copy.insert(ii,chk)
        elif ii == 6:
            d_copy.insert(ii,int(float(details[3])*10))
        elif ii == 7:
            chk = random.randint(0,2)
            d_copy.insert(ii,chk)
        elif ii == 8:
            if details[4] == 'Y' or'y':
                d_copy.insert(ii,1)
            else: 
                d_copy.insert(ii,0)
        elif ii == 9:
            d_copy.insert(ii,int(details[5])*10)
        elif ii == 10:
            chk = random.randint(0,1)
            d_copy.insert(ii,chk)
        elif ii == 11:
            d_copy.insert(ii,int(details[6])*10)
        count = count+1


    final_features = [np.array(d_copy)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    print("Output is ",prediction[0])
    if d_copy[1] <=50 or  d_copy[3] <=50  or d_copy[6] <=50:
        output = 0
    print("Output is ",output)
    if(output==1):
        return render_template('index.html', prediction_text=f'Congrats {nam},you have high possiblity to be placed')
    if(output==0):
        return render_template('index.html', prediction_text=f'Sorry {nam}, Your placement chances are Low')
    
    del d_copy
    del details
    
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)