def solution(names, yearning, photos):
    value_dic = {}
    answer = []
    for i, name in enumerate(names):
        value_dic[name] = yearning[i]
    for photo in photos:
        each_photo_value = 0
        for person in photo:
            each_photo_value += value_dic.get(person, 0)
        answer.append(each_photo_value)
    return answer


solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain",
         "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
solution(["kali", "mari", "don"],	[11, 1, 55],	[
         ["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])
solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],	[
         ["may"], ["kein", "deny", "may"], ["kon", "coni"]])
