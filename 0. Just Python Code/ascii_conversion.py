""" num = int(input("Enter a number: "))

# Convert the number to ASCII character
ascii_char = chr(num)

# Print the ASCII character
print(f"The ASCII character for {num} is '{ascii_char}'")
 """

ascii_array = [109, 121, 88, 79, 82, 107, 101, 121]

for value in ascii_array:
    print(chr(value), end='')