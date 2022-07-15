# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi=int(round(weight*(1/height**2)))

ans=""

if 18.5 <= bmi < 25:
    ans+="have a normal weight"
else:
    ans+="are "


if bmi <=18:
    ans+= "underweight"
if 25<= bmi < 30:
    ans+="slightly overweight"
if 30 <= bmi <35:
    ans+="obese"
if 35 <= bmi:
     ans+="clinically obese"


print(f"Your BMI is {bmi}, you {ans}.")