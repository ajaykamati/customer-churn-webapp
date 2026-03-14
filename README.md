# Customer Churn Prediction Web App

A clean, modern, and professional machine learning web application for predicting whether a customer will churn or not based on an XGBoost classification model.

## Technology Stack
* **Backend:** Python, Flask
* **Machine Learning:** XGBoost, Scikit-learn, Pandas, Numpy
* **Frontend:** HTML5, CSS3, Bootstrap 5

## Project Structure
```text
customer-churn-webapp/
│
├── app.py                  # Flask application entry point
├── model.pkl               # Pickled trained XGBoost model
├── dataset.csv             # Raw dataset (dummy/sample data)
├── requirements.txt        # Python dependencies
│
├── templates/              # HTML Templates
│   ├── base.html           # Main layout
│   ├── index.html          # Landing page
│   ├── predict.html        # Prediction form 
│   ├── result.html         # Prediction result page
│   └── about.html          # Project details page
│
├── static/                 # Static Assets
│   └── css/
│       └── style.css       # Custom styling
│
└── README.md
```

## How to Run Locally

1. **Clone the repository or navigate to the folder:**
   ```bash
   cd customer-churn-webapp
   ```

2. **Create a virtual environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open a web browser and go to `http://127.0.0.1:5000/`.

## Deployment
This app uses `gunicorn` in `requirements.txt` making it ready for deployment on platforms like Render or Heroku.
