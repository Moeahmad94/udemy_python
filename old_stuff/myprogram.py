temperatures=[10,-20,-289,100]
def c_to_f(temperatures):
    with open("temperatures", "w") as file:
        for t in temperatures:
            if t > -273.15:
                f=t*9/5+32
                file.write(str(f) + "\n")

print(c_to_f(temperatures))
