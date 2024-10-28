from flask import Flask, request, jsonify
import pickle

# Initialize Flask app
app = Flask("churn")

# Load the model and vectorizer from files in the image
with open("model2.bin", "rb") as model_file:
    model = pickle.load(model_file)

with open("dv.bin", "rb") as dv_file:
    dv = pickle.load(dv_file)

@app.route('/predict', methods=['POST'])
def predict():
    client_data = request.get_json()
    X = dv.transform([client_data])  # Transform input with dict vectorizer
    y_pred = model.predict_proba(X)[0, 1]  # Predict probability
    result = {'predicted_probability': float(y_pred)}
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9696)
