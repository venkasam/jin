from flask import Flask, jsonify,request
from live import get_predict
app=Flask(__name__)
@app.route("/")
def helloworld():
    return "helloworld"
@app.route("/predict-digit",methods=["POST"])
def predict():
    image=request.files.get("digit")
    prediction=get_predict(image)
    return jsonify({
        "prediction":prediction
    }
                ),200
if __name__=="__main__":
    app.run(debug=True)
    