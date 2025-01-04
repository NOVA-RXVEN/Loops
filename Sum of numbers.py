n = int(input("Enter a Number: "))

sum = 0
for i in range(1, n+1):
    sum = sum + i
    
    print(f"For {i}th Iternation Sum = {sum}")