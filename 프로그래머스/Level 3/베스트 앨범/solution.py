
def solution(genres, plays):
    answer = []
    info = []
    dic = {}
    dic_count = {}
    for i in range(len(genres)):
        info.append([plays[i], genres[i],  -i])
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
            dic_count[genres[i]] += 1
            continue
        dic[genres[i]] = plays[i]
        dic_count[genres[i]] = 1
    info.sort(reverse=True)
    while dic:
        high_genres = max(dic, key=dic.get)
        count = 0
        if dic_count[high_genres] >= 2:
            for i in info:
                if i[1] == high_genres:
                    count += 1
                    answer.append(-i[2])
                    if count >= 2:
                        break
        dic.pop(high_genres)
        dic_count.pop(high_genres)
    print(answer)
    return answer


solution(["classic", "pop", "classic", "classic", "pop"],
         [500, 600, 150, 800, 2500])


'''
def solution(genres, plays):
    answer = []
    dic = {}
    dic_count = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
            dic_count[genres[i]][0] += 1
            dic_count[genres[i]][1].append(i)
            continue
        dic[genres[i]] = plays[i]
        dic_count[genres[i]] = [1, [i]]
    while True:
        high_genres = max(dic, key=dic.get)
        songs = []
        if dic_count[high_genres][0] >= 2:
            while len(songs) < 2:
                max_value = 0
                idx = 0
                for i in dic_count[high_genres][1]:
                    if plays[i] > max_value:
                        max_value = plays[i]
                        idx = i
                dic_count[high_genres][1].pop(
                    dic_count[high_genres][1].index(idx))
                dic_count[high_genres][0] -= 1
                dic[high_genres] -= max_value
                songs.append(idx)
            for i in songs:
                answer.append(i)
            continue
        break'''
