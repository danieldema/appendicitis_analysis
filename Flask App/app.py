from flask import Flask, render_template, request, make_response
import joblib

model = joblib.load('model/model5.joblib')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        alvarado_score = float(request.form['Alvarado_Score'])
        appendix_diameter = float(request.form['Appendix_Diameter'])
        lower_right_abd_pain = int(request.form['Lower_Right_Abd_Pain'])
        contralateral_rebound = int(request.form['Contralateral_Rebound_Tenderness'])
        coughing_pain = int(request.form['Coughing_Pain'])
        nausea = int(request.form['Nausea'])
        loss_of_appetite = int(request.form['Loss_of_Appetite'])
        body_temperature = float(request.form['Body_Temperature'])
        stool = int(request.form['Stool'])
        psoas_sign = int(request.form['Psoas_Sign'])

        binary_features = [lower_right_abd_pain, contralateral_rebound, coughing_pain, nausea, loss_of_appetite, psoas_sign]
        if any(f not in (0,1) for f in binary_features):
            return render_template('index.html', prediction="Error: Binary inputs must be 0 or 1.")
        if stool not in (0,1,2):
            return render_template('index.html', prediction="Error: Stool must be 0, 1, or 2.")

        features = [[
            alvarado_score,
            appendix_diameter,
            lower_right_abd_pain,
            contralateral_rebound,
            coughing_pain,
            nausea,
            loss_of_appetite,
            body_temperature,
            stool,
            psoas_sign
                    ]]
    
        prob = model.predict_proba(features)[0][1]

        threshold = 0.5
    
        if prob > threshold:
            label = 'Likely Appendicitis'
        else:
            label = 'Unlikely Appendicitis'

        percent = prob * 100
        result = f'{label} ({percent:.2f}%)'

        return render_template('index.html', prediction=result, prediction_percent=percent)
    
    except ValueError: 
         return render_template('index.html', prediction="Error: Invalid input detected. Please enter valid inputs.")
    

if __name__ == '__main__':
    app.run(debug=True)