print("Välkommen till miniräknaren!")
tal1 = float(input("Skriv första talet: "))
operator = input("Välj (+, -, *, /): ")
tal2 = float(input("Skriv andra talet: "))

if operator == "+":
    print("Svar:", tal1 + tal2)
elif operator == "-":
    print("Svar:", tal1 - tal2)
elif operator == "*":
    print("Svar:", tal1 * tal2)
elif operator == "/":
    print("Svar:", tal1 / tal2)
else:
    print("Felaktig operator!")
