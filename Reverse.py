string = input("Please enter your Own string: ")

string2 = ""

for i in string:
    string2 = i + string2
    
print("\nThe Original String: ", string)
print("The Reversed String: ", string2)