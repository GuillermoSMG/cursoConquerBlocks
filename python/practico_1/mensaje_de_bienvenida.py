text = ", estás usando python";
name = input("Introduce tu nombre: ");

upper_case = f"¡Hola, {name} {text}!".upper()
print(upper_case)

lower_case = f"¡Hola, {name} {text}!".lower()
print(lower_case)

correct_format = f"¡Hola, {name.replace(".","").title()} {text}!"
print(correct_format)

