choice = input("1.Control Flow \n2.Relational and Logical Operators \n3.For Loop and Bitwise Operator\n\nEnter Your Choice: ")
match choice:
    case "1":
        while True:
            user_input = input("\nEnter a number (or'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
            try:
                number = float(user_input)
                if number > 0:
                    print("\\nThe number is positive.")
                elif number < 0:
                    print("\nThe number is negative.")
                else:
                    print("\nThe number is zero.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number or 'exit' .")
            continue
    case "2":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if num1 % 2 == 0 and num2 % 2 == 0:
            print("Both numbers are even.")
        elif num1 % 2 != 0 and num2 % 2 != 0:
            print("Both numbers are odd.")
        else:
            print("One number is even, and the other is odd.")
    case "3":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        numbers = [num1, num2]
        def to_binary(n):
            binary = ""
            while n > 0:
                binary = str(n & 1) + binary
                n >>= 1
            return binary if binary else '0'
        def to_octal(n):
            octal = ""
            while n > 0:
                octal = str(n & 7) + octal
                n >>= 3
            return octal if octal else '0'
        def to_hexadecimal(n):
            hex_digits = "0123456789ABCDEF"
            hexadecimal = ""
            while n > 0:
                hexadecimal = hex_digits[n & 15] + hexadecimal
                n >>= 4
            return hexadecimal if hexadecimal else '0' 

for num in numbers:
    print(f"\nNumber: {num}")
    print(f"Binary: {to_binary(num)}")
    print(f"Octal: {to_octal(num)}")
    print(f"Hexadecimal: {to_hexadecimal(num)}")
    print("-" * 30)

