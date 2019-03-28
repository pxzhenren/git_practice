# Write your max_num function here:
# Write your max_num function here:
def max_num(num1,num2,num3):
  if num1>num2 and (num2>num3 or num2==num3): 
    return num1
  elif num2>num1 and num2>num3: 
    return num2
  elif num3>num1 and num3>num2: 
    return num3
  else:
    return "It's a tie!"
  
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(3, 3, -13))
# should print "It's a tie!"
print(max_num(-3,-2,-3))
