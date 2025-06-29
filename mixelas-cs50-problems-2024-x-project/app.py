from flask import Flask, render_template, request

app = Flask(__name__, template_folder='frontend')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100  # Convert height from cm to meters
    activity_level = request.form['activity_level']

    # Calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation
    bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5  # Assuming male for simplicity

    # Adjust BMR based on activity level
    if activity_level == 'sedentary':
        caloric_needs = bmr * 1.2
    elif activity_level == 'light':
        caloric_needs = bmr * 1.375
    elif activity_level == 'moderate':
        caloric_needs = bmr * 1.55
    elif activity_level == 'active':
        caloric_needs = bmr * 1.725
    else:  # very active
        caloric_needs = bmr * 1.9

    # Calculate BMI
    bmi = weight / (height ** 2)  # height is already in meters

    # Generate advice based on BMI
    advice = ""
    if bmi < 18.5:
        advice = "You are underweight. Consider increasing your caloric intake with nutrient-dense foods."
    elif 18.5 <= bmi < 24.9:
        advice = "You have a healthy weight. Maintain your current diet and exercise routine."
    elif 25 <= bmi < 29.9:
        advice = "You are overweight. Consider a balanced diet and regular exercise to reach a healthier weight."
    else:
        advice = "You are classified as obese. It's advisable to consult with a healthcare provider for personalized advice."

    # Example dietary goals (macronutrient distribution)
    protein = caloric_needs * 0.25 / 4  # 25% of calories from protein
    carbs = caloric_needs * 0.50 / 4     # 50% of calories from carbs
    fats = caloric_needs * 0.25 / 9      # 25% of calories from fats

    return render_template('results.html', caloric_needs=caloric_needs, protein=protein, carbs=carbs, fats=fats, bmi=bmi, advice=advice)
if __name__ == '__main__':
    app.run(debug=True)
