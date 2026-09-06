import math

def calculate_factorial(n):
    return math.factorial(n)

def calculate_compound_interest(principal, rate, time):
    return principal * (math.pow((1 + rate / 100), time))

def calculate_trigonometry(angle_degrees):
    rad = math.radians(angle_degrees)
    return math.sin(rad), math.cos(rad), math.tan(rad)
