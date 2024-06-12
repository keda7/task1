
string1 = "Hello"
string2 = "World"

concatenated_string = string1 + " " + string2
print("Concatenated String:", concatenated_string)

string_length = len(concatenated_string)
print("Length of String:", string_length)


substring = "World"
if substring in concatenated_string:
    print("Substring '{}' found in the concatenated string.".format(substring))
else:
    print("Substring '{}' not found in the concatenated string.".format(substring))


uppercase_string = concatenated_string.upper()
print("Uppercase String:", uppercase_string)

lowercase_string = concatenated_string.lower()
print("Lowercase String:", lowercase_string)


if concatenated_string.startswith("Hello"):
    print("The concatenated string starts with 'Hello'.")
else:
    print("The concatenated string does not start with 'Hello'.")


if concatenated_string.endswith("World"):
    print("The concatenated string ends with 'World'.")
else:
    print("The concatenated string does not end with 'World'.")
