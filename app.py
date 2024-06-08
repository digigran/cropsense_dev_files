from flask import Flask, render_template, request
from recommendation_logic import generate_recommendations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    if request.method == 'POST':
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])
        soil_type = request.form['soil_type']
        region = request.form['region']
        recommendations = generate_recommendations(temperature, humidity, rainfall, soil_type, region)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)

