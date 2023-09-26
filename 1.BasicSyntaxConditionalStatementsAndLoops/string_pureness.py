number_of_strings = int(input())
for current_string in range(number_of_strings):
    string_to_check = input()
    if "," in string_to_check or \
            "." in string_to_check or \
            "_" in string_to_check:
        print(f"{string_to_check} is not pure!")
    else:
        print(f"{string_to_check} is pure.")