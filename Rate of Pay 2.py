h = float(input("Enter Hours:"))
r = float(input("Ebter Hours:"))
if h<=40:
    print(h * r)
else:
    print(40 * r + (h - 40) * r * 1.5)