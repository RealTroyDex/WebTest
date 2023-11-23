import random

def generate_activation_code():
    code = ''
    for _ in range(5):
        code += str(random.randint(0, 9))
    return code
