__author__="Majid shiri"

#function welcome user
def hello(name):
    return (f'hello {name},Your Welcome')

#For RUN TEST Function
if __name__ == '__main__':
    print(hello(input('Enter your Name:')))

"""
trace function hello
1. line 9 first get name for test
2. line 5 return say hello and format
3. line 9 print return function hello 
"""