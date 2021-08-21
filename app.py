import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

server = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@server.route('/')
def home():
    return render_template('index.html')

@server.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    output = refine(output)
    return render_template('index.html', prediction_text='The Employee Salary should be $ {}'.format(output) )

def refine(value):
    return(value*2)
    
   
@server.route('/home', methods=['POST','GET'])
def ecc():
    return("This is home page")
    
@server.route('/office', methods=['POST','GET'])
def packaging():
    return '''<h1>The name is: {}</h1>'''.format(request.args.get('name'))

if __name__ == "__main__":
    server.run(debug=True)
    #server.run(host='0.0.0.0',port=8080)