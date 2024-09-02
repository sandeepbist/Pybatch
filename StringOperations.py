choice = input("1.Reverse Name \n2.Numeric Data Types and Conversion \n3.Simple Input/Output \n4.Format Method \n5.Percent Method \n\nEnter Your Choice: ")
match choice:
    case "1":
        first_name = input("\nEnter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()
        reversed_name = " ".join([last_name, first_name])
        print("\nReversed order: ", reversed_name)
        # .strip() removes any leading or trailing whitespace
        # .join() combines the last and first names with a space in between
    case "2":
        num = input("\nEnter a number: ")
        integer_value = int(num) 
        float_value = float(num)
        complex_value = complex(num)
        print(f"\nInteger: {integer_value},Float: {float_value},Complex: {complex_value}")
        # int: Whole numbers without a decimal point. Used only when only whole numbers are required.
        # float: Numbers with a decimal point (real numbers).Used when precision with fractional value is important
        # complex: Numbers with both a real and imaginary part. Used in advanced maths, scientific calculations
    case "3":
        len = int(input("\nEnter the Length Of Rectangle: "))
        wid = int(input("Enter the Width of the Rectangle: "))
        area = len*wid
        print("\nThe Area Of Rectangle: ",area)
    case "4":
        len = int(input("\nEnter the Length Of Rectangle: "))
        wid = int(input("Enter the Width of the Rectangle: "))
        area = len*wid
        print("\nThe Area Of Rectangle: ",area)
        if area >= 0:
            print("Formatted Area of Rectangle",float(area))
        else:
            print("Formatted Area Of Rectangle",float(area))
    case "5":
        num1 = int(input("Enter Number 1: "))
        num2 = int(input("Enter Number 2: "))
        num3 = int(input("Enter Number 3: "))
        calculated_average = (num1 + num2 + num3) / 3
        print("The average of three numbers is %.2f" % calculated_average)