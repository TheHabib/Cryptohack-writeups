def xor_operation(number1, number2):
    # Convert the numbers to strings to make it easier to work with digits
    str_num1 = str(number1)
    str_num2 = str(number2)
    
    # Find the maximum length of the two strings
    max_length = max(len(str_num1), len(str_num2))
    
    # Pad the shorter string with leading zeros if needed
    str_num1 = str_num1.zfill(max_length)
    str_num2 = str_num2.zfill(max_length)

    # Initialize an empty result string
    result = ""

    # Iterate through the indices of the digits in the strings
    for i in range(max_length):
        digit1 = str_num1[i]
        digit2 = str_num2[i]
        
        if digit1 == digit2:
            result += "1"
        else:
            result += "0"

    # Convert the result back to an integer if needed
    # result_int = int(result, 2)  # Uncomment this line if you want the result as an integer
    return result

# Example usage:

print("Input Two Numbers:")
number1 = input()
number2 = input()
result = xor_operation(number1, number2)
print(result)  # Output: "11000"
