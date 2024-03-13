p = "enter password\n"

d = {"len": False, "digit": False, "upper": False}

while True:
    op = input(p)
    print(op)
    if op in "q!":
        break
    else:
        if len(op) >= 6:
            d["len"] = True

        for i in op:
            if i.isdigit():
                d["digit"] = True
                break

        for i in op:
            if i.isupper():
                d["upper"] = True
    print(d)
    if all(d.values()):
        print("Strong Password")
    else:
        print("Weak Password")
