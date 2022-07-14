# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

def sum_of_pieces(x:str) -> Integer:
    y=int(x)
    sum=0
    while(y>0):
        sum+=y%10
        y=(y//10)
    return sum


print(sum_of_pieces(two_digit_number))