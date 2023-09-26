input_string = input()

while input_string != "End":
    if input_string != "SoftUni":
        new_string = ""
        for character in input_string:
            new_string += character * 2
        print(new_string)
    input_string = input()
