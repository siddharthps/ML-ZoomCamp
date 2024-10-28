from flask import Flask, request, jsonify
import pickle

# Initialize the Flask app
app = Flask('churn')

# Load the DictVectorizer and model
dv_path = 'dv.bin'
model_path = 'model1.bin'

with open(dv_path, 'rb') as f_in:
    dv = pickle.load(f_in)

with open(model_path, 'rb') as f_in:
    model = pickle.load(f_in)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input JSON data
    client_data = request.get_json()
    
    # Transform the input data using the dict vectorizer
    X = dv.transform([client_data])
    # Predict the probability of the input data using the model
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5
    
    # Prepare the result in JSON format
    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }
    return jsonify(result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696, use_reloader=False)
