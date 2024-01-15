SHIP_PATH = "C:\\Users\\AnMV\\Desktop\\Temp\\\Dâu\\tinh_sl.txt"

if __name__ == '__main__':
    f = open(SHIP_PATH, mode="r", encoding="utf-8")
    lines = f.readlines()

    list_sl = []

    for line in lines:
        temp = line.split(" ")
        obj_temp = [temp[1].replace("\n", "").lower(), temp[0]]
        list_sl.append(obj_temp)
        # print(obj_temp)

    svip = 0
    vip = 0
    nho = 0
    bi = 0
    ve = 0

    for obj in list_sl:
        if obj[0].lower() == "svip":
            svip += float(obj[1])
        if obj[0].lower() == "vip":
            vip += float(obj[1])
        if obj[0].lower() == "nhỡ":
            nho += float(obj[1])
        if obj[0].lower() == "bi":
            bi += float(obj[1])
        if obj[0].lower() == "ve":
            ve += float(obj[1])

    print("Svip: " + str(svip))
    print("Vip: " + str(vip))
    print("Nhỡ: " + str(nho))
    print("Bi: " + str(bi))
    print("Ve: " + str(ve))
    print("Total: " + str(svip + vip + nho + bi + ve))
