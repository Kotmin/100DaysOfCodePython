# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

def sum_of_pieces(x):
    y=int(x)
    sum=0
    while(y>0):
        sum+=y%10
        y=(y//10)
    return sum

lista = ("10","52","92")
#print(sum_of_pieces(two_digit_number))
print(list(map(sum_of_pieces,lista)))