# Write a Python program to solve quadratic equation.
# The standard form of a quadratic equation is:
# where
# a, b and c are real numbers and
# The solutions of this quadratic equation is given by:
# 𝑎𝑥 + 𝑏𝑥 + 𝑐 = 0
# 2
# 𝑎 ≠ 0
# (−𝑏 ± (𝑏 − 4𝑎𝑐 )/(2𝑎)

try:
    a = int(input("Enter a: "))
    while a == 0:
        print("'a' value cannot be 0")
        a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    print(f"Substitute (a={a}), (b={b}) and (c={c}) into the quadratic formula")

except:
    pass
else:
    pass
finally:
    pass