<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF- <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dietary Goals Results</title>
</head>
<body>
    <h1>Your Dietary Goals</h1>
    <p>Daily Caloric Needs: {{ caloric_needs | round(2) }} calories</p>
    <p>Protein: {{ protein | round(2) }} grams</p>
    <p>Carbohydrates: {{ carbs | round(2) }} grams</p>
    <p>Fats: {{ fats | round(2) }} grams</p>
    <a href="/">Calculate Again</a>
</body>
</html>
