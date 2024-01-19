def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if dic.get(i[1], -1) == -1:
            dic[i[1]] = 2
            continue
        dic[i[1]] += 1
    for value in dic.values():
        answer *= value

    return answer-1


solution([["yellow_hat", "headgear"], ["blue_sunglasses",
         "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"],
         ["smoky_makeup", "face"]])
