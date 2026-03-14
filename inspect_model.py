import pickle

try:
    with open('../customer-churn-webapp/model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
    print("Model type:", type(model))
    if hasattr(model, 'feature_names_in_'):
        print("Expected features:", model.feature_names_in_)
    if hasattr(model, 'n_features_in_'):
        print("Number of features:", model.n_features_in_)
except Exception as e:
    print("Error loading model:", e)
