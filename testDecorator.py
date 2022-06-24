# functions : input / functinnality / output
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# functions are known as first class objects, that means you can pass a function around as an argument for another function.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

print(calculate(add, 3, 4))

# nested functions : functions car also be nested inside other functions. 
def outer_function():
    print("I am outer")
    
    #scope : only accessible inside the confines of this function
    def nested_function():
        print("I am inner")
    
    nested_function()
        
outer_function()

# functions can be returned for other functions

def outer_function_2():
    print("I am outer")

    def nested_function_2():
        print("I am inner")
    
    return nested_function_2
        
inner_function = outer_function_2()
inner_function()

## Python Decorator Function

import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # here, add what has to be done before the function
        function()
        function()
        # here, add what has to be done after the function
    return wrapper_function

# now we can call the delay_decorator in front of the methods
@delay_decorator
def say_hello():
    print("hello")

def say_bye():
    print("bye")

@delay_decorator
def say_greeting():
    print("greeting")

#with @ sugar
say_hello()

# instead of @ which is syntaxic sugar, we could have done:
delayed_bye = delay_decorator(say_bye)
delayed_bye()

#with @ sugar
say_greeting()



