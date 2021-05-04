temp = input("Enter a Temperature to convert: ").upper().replace(" ", "")
float_temp = float(temp[:-1])

if temp[-1] == "F":
    newC = ((5 * float_temp) - 160) / 9
    print(str(newC) + "C")

elif temp[-1] == "C":
    newF = ((9 * float_temp) + (32 * 5)) / 5
    print(str(newF) + "F")

else:
    print("Error: please type a number followed by the letter C/F.")
