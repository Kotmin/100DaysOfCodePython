# Link

#https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python




# The original answer below was written in 2008. Since then, Python 3.10 (2021) introduced the match-case statement which provides a first-class implementation of a "switch" for Python. For example:

def f(x):
    match x:
        case 'a':
            return 1
        case 'b':
            return 2
        case _:
            return 0   # 0 is the default case if x is not found

# The match-case statement is considerably more powerful than this simple example.

# You could use a dictionary:

def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]

