from flask import Flask, render_template, request
import pickle
import numpy as np
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)

import os

# Load the model
try:
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    print(f"Error loading the model: {e}")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_form')
def predict_form():
    return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return render_template('result.html', prediction_text="Model not loaded. Contact administrator.", probabilities=None)

    try:
        # Get features from the form
        features = [
            float(request.form['Customer_Age']),
            float(request.form['Dependent_count']),
            float(request.form['Months_on_book']),
            float(request.form['Total_Relationship_Count']),
            float(request.form['Months_Inactive_12_mon']),
            float(request.form['Contacts_Count_12_mon']),
            float(request.form['Credit_Limit']),
            float(request.form['Total_Revolving_Bal']),
            float(request.form['Total_Trans_Amt'])
        ]
        
        # Convert to a 2D array
        features_array = np.array([features])
        
        # Make prediction
        prediction = model.predict(features_array)[0]
        
        try:
            probability = model.predict_proba(features_array)[0][1]
            prob_percent = round(probability * 100, 2)
        except Exception:
            prob_percent = None

        if prediction == 1:
            result_text = "Customer is likely to churn"
            card_class = "border-danger text-danger"
            icon = "bi-exclamation-triangle-fill"
        else:
            result_text = "Customer is not likely to churn"
            card_class = "border-success text-success"
            icon = "bi-check-circle-fill"
            
        return render_template('result.html', 
                               prediction_text=result_text, 
                               probability=f"{prob_percent}%" if prob_percent is not None else "N/A",
                               card_class=card_class,
                               icon=icon)

    except Exception as e:
        return render_template('result.html', prediction_text=f"Error in prediction: {str(e)}", probabilities=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
