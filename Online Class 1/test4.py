# Strings and formatting

x = "python"
y = "awesome"

# Ways to print out strings
print(x + " is " + y) # method 1 "+"
print(x,"is",y) # method 2 ","

# f-string (format-string) or f""
print(f"{x} is {y}")

# left align use <
# right align use >
# center is ^

n1 = 50
n2 = 100
print(f"Sum of n1 and n2 is {n1+n2:>15}")

x = 'CSU'
print(f"I LOVE {x}!!!")