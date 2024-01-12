#border
rows = 7  
half = (rows + 1) // 2


for i in range(1, half + 1):
    for j in range(half - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


for i in range(half - 1, 0, -1):
    for j in range(half - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
   






#diamond
rows = 4
for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(" ", end="  ")
    for j in range(0, 2 * i + 1):
        print("*", end="  ")
    print()

for i in range(rows - 2, -1, -1):
    for j in range(0, rows - i - 1):
        print(" ", end="  ")
    for j in range(0, 2 * i + 1):
        print("*", end="  ")
    print()








rows = 4
for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(" ", end="  ")
    for j in range(0, 2 * i + 1):
        print("*", end="  ")
    print()







#step *
steps = 5
for i in range(1, steps + 1):
    for j in range(1, i + 1):
        print("*", end =" ")
    print()





#steps
steps = 5
for i in range(1, steps + 1):
    for j in range(1, i + 1):
        print(j, end =" ")
    print()






#step reverse
steps = 5
for i in range(steps, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
