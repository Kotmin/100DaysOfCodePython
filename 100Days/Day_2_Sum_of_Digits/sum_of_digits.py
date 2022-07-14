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


# From internet

# sum_digits = lambda number: 0 if number == 0 else (number % 10) + sum_digits (number / 10)

# count_digit = lambda number: 0 if number == 0 else 1 + count_digit(number/10)

# https://stackoverflow.com/questions/43302412/using-lambda-functions-to-sum-digits-and-count-digits


# Even better 

# sum_of_digits = lambda n: sum(int(d) for d in str(n))
# count_digit = lambda n: len(str(n))

# Same site