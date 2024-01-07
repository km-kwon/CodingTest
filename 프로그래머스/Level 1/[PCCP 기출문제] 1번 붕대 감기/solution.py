def solution(park, routes):
    answer = []
    len_w = len(park[0])-1
    len_h = len(park)-1
    loc_x = 0
    loc_y = 0
    for i in range(len(park)):
        check = park[i].find("S")
        if check != -1:
            loc_x = i
            loc_y = check
    for i in routes:
        flag = False
        order = i.split()
        if order[0] == "E":
            if (loc_y + int(order[1])) > len_w:
                flag = True
                continue

            for check in range(int(order[1])):
                if park[loc_x][loc_y + check + 1] == "X":
                    flag = True
                    break

            if flag == False:
                loc_y = loc_y + int(order[1])

        if order[0] == "W":

            if (loc_y - int(order[1])) < 0:
                flag = True
                continue

            for check in range(int(order[1])):
                if park[loc_x][loc_y - (check + 1)] == "X":
                    flag = True
                    break

            if flag == False:
                loc_y = loc_y - int(order[1])

        if order[0] == "S":

            if (loc_x + int(order[1])) > len_h:
                flag = True
                continue

            for check in range(int(order[1])):
                if park[loc_x + check + 1][loc_y] == "X":
                    flag = True
                    break

            if flag == False:
                loc_x = loc_x + int(order[1])

        if order[0] == "N":

            if (loc_x - int(order[1])) < 0:
                flag = True
                continue

            for check in range(int(order[1])):
                if park[loc_x - (check + 1)][loc_y] == "X":
                    flag = True
                    break

            if flag == False:
                loc_x = loc_x - int(order[1])
    answer.append(loc_x)
    answer.append(loc_y)
    return answer


solution(["SOO", "OOO", "OOO"],	["E 2", "S 2", "W 1"])
solution(["SOO", "OXX", "OOO"],	["E 2", "S 2", "W 1"])
solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"])
