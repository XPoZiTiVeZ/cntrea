data = [[int(row.split()[0]), int(row.split()[1]), row.split()[2]] for row in open("26.txt").read().splitlines()]
datas = sorted(data, key=lambda t: t[0])

placesA = [0] * 80
placesB = [0] * 20

c_success = 0
c_unsuccess = 0

for t, d, tp in datas:
    f = False
    if tp == "A":
        for i in range(len(placesA)):
            if placesA[i] > t: continue

            placesA[i] = t + d
            c_success += 1
            f = True
            break
        
        if not f:
            for i in range(len(placesB)):
                if placesB[i] > t: continue

                placesB[i] = t + d
                c_success += 1
                f = True
                break

        if not f:
            c_unsuccess += 1

    elif tp == "B":
        for i in range(len(placesB)):
            if placesB[i] > t: continue

            placesB[i] = t + d
            f = True
            break

        if not f:
            c_unsuccess += 1

print(c_success, c_unsuccess)

# print(*datas, sep="\n")