import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('dt_model_diabete.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = "positive" if prediction == 1 else "negative"

    return render_template('index.html', prediction_text='Diabetes Test is {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)