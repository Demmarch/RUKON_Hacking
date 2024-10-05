for i in range(1, 11):
    with open(f"TABL/tabl{i}.txt", "w", encoding="utf-8") as file:
        for j in range(1, 11):
            file.write(f"{i} * {j} = "+str(i*j) + "\n")
    file.close()
for i in range(1, 11):
    with open(f"TABL/tabl{i}.txt", "r", encoding="utf-8") as file:
        print(f"tabl{i}.txt")
        for txt in file.readlines():
            print(txt[:len(txt)-1])
