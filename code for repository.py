n=int(input("n: "))
rev=0
t=n
while(n!=0):
    a=n%10
    rev=rev*10+a
    n=n//10
print(f"reverse of a number={rev}")
if(t==rev):
    print("palindrome")
else:
    print("not palindrome")