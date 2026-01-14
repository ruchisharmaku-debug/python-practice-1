#Write a Python program that takes two integers as input from user (num1 and num2). If their sum is less than 50, print their product. Otherwise, print their sum. Format output as "The result is [value]".
#do number input lo 
num1= int(input ("enter first number:"))
num2= int(input ("enter second number:"))

# sum calculate karo
total = num1+num2
# condition check kro
if total < 50 :
    result = num1 * num2 
    # product print karo
else:
    result= total
print("the result is", result)
