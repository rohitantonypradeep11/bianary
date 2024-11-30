def integer_to_binary(integer):
    return bin(integer)[2:]

integer = int(input("Enter an integer: "))
binary_value = integer_to_binary(integer)
print(f"The binary value of {integer} is {binary_value}")