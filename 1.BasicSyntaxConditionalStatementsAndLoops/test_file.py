import random
import string


def generate_code():
    code = ""
    for _ in range(3):  # Генерираме три блока
        block = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
        code += block + "-"

    # Премахваме последния тире
    code = code[:-1]

    return code


# Генерираме кодове
for _ in range(5):  # Примерно, може да генерирате колкото искате кодове
    generated_code = generate_code()
    print(generated_code)
