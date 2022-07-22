student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
# def translated(score):
#     verbally = ""

#     return verbally

def translated(x):
    return {
        x <= 70:"Fail",
        71 <= x < 81:"Acceptable",
        81 <= x <90:"Exceeds Expectations",
        91 <= x <=100:"Outstanding"
    }[x]


for key in student_scores:
    student_grades[key] = translated(student_scores[key])
    

# 🚨 Don't change the code below 👇
print(student_grades)


# That doesn't work probably this trick will work only with static keys. I'm not sure about investing time into searching how to type it this way

def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]


# this is working and returnning clear number, what's cool