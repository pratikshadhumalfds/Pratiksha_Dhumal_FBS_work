###WAP to find the roots of a Quadratic equation.

a = int(input("Enter 1st no:"))
b = int(input("Enter 2nd NO:"))
c = int(input("Enter 3rd no:"))

Sqrt = ((b**2)-(4*a*c))**0.5

res1 = (-b+Sqrt)/2*a
res2 = (-b-Sqrt)/2*a

print(f'Roots of Quadratic Equation is {res1} {res2}')    ###roots= (2,3,-2)
