count=int(input("How many numbers do you want to print?"))
print("---OUTPUT---")
for i in range(count):
    num=int(input(f"Number {i+1}:"))
    if num%2==0:
        print("Even number skipped")
        continue
    print(num,"is an odd number")