def make_multiplier(factor):
    def multiply(x):
        return x*factor
    return multiply

double = make_multiplier(2) # factor = 2
triple = make_multiplier(3) # factor = 3

print(double(5))
print(triple(5))


