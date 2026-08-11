print("Welcome! to the intetractive personal data collector")
print()

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
favourite_number = int(input("Enter your favourite number: "))

current_year = 2026
birth_year = current_year - age
age_after_5_years = age + 5

print()
print("           USER INFORMATION")
print()
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Favourite Number: {favourite_number}")
print(f"Estimated Birth Year: {birth_year}")
print(f"Your age after 5 years will be: {age_after_5_years}")

print()
print("        COLLECTED INFORMATION")
print()

print(f"Name: {name} (Type: {type(name)}, ID: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, ID: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, ID: {id(height)})")
print(f"Favourite Number: {favourite_number} "
      f"(Type: {type(favourite_number)}, ID: {id(favourite_number)})")

print()
print("          TYPE CASTING")
print()
height_integer = int(height)

print(f"Original height: {height}")
print(f"Original type: {type(height)}")
print(f"After conversion: {height_integer}")
print(f"New type: {type(height_integer)}")
print()

age_float = float(age)

print(f"Original age: {age}")
print(f"Original type: {type(age)}")
print(f"After conversion: {age_float}")
print(f"New type: {type(age_float)}")

print()
print()
print("Thank you for using the Personal Information Program!")
print("Keep exploring Python!")
