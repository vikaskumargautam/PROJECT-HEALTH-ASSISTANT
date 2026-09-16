def bmi_calculator(weight,height):
    bmi = weight/(height**2)
    return bmi

def bmr_calculator(gender,age,weight,height):
    if gender == "male":
        bmr = (10*weight)+(6.25*height)-(5*age)+5
        return bmr
    elif gender == "female":
        bmr = (10*weight)+(6.25*height)-(5*age)-161
        return bmr

def tdee_calculator(bmr,activity):
    activity_factor={
        "Sendentary" : 1.20,
        "Lightly Active":1.375,
        "Moderately Active":1.55,
        "Very Active":1.725,
        "Extra Active":1.90
    }
    tdee = bmr*activity_factor[activity]
    return tdee

def calories_target(tdee,aim) :
    if aim == "maintain":
        calorie = tdee 
    elif aim == "loss":
        calorie= tdee-400
    elif aim == "gain":
        calorie = tdee+300
    return calorie 