Base = 2
Exponent = 7

if Exponent == 0:
    result = 1
else: 
    result = Base
    while Exponent > 1:
        Base *= result
        Exponent -= 1

print (f"2^7 = {Base}")