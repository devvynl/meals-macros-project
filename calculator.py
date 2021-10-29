"""calorie and macro calculator"""

def calculate_bmr(gender, weight, height, age):
    if gender == "male":
        return  (4.536 * weight) + (15.88 * height) - (5 * age) + 5
    elif gender == "female":
        return (4.536 * weight) + (15.88 * height) - (5 * age) - 161

