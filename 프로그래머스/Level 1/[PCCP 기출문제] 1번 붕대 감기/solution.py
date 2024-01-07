def solution(bandage, health, attacks):
    cur_health = health
    last_attack = int(attacks[len(attacks)-1][0])
    cur_bandage = 0
    for i in range(last_attack+1):
        if attacks:
            if i == attacks[0][0]:
                cur_health -= attacks[0][1]
                if cur_health <= 0:
                    cur_health = -1
                    break
                attacks.pop(0)
                cur_bandage = 0
                continue
        cur_health += bandage[1]
        cur_bandage += 1
        if cur_bandage == bandage[0]:
            cur_health += bandage[2]
            cur_bandage = 0
        if cur_health > health:
            cur_health = health
    return cur_health


# solution([5, 1, 5],	30,	[[2, 10], [9, 15], [10, 5], [11, 5]])
# solution([3, 2, 7], 20,	[[1, 15], [5, 16], [8, 6]])
solution([4, 2, 7], 20,	[[1, 15], [5, 16], [8, 6]])
solution([1, 1, 1], 5,	[[1, 2], [3, 2]])
