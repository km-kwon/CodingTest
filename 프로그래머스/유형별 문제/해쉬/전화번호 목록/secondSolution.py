def solution(phone_book):
    answer = True
    list = dict.fromkeys(phone_book, 0)
    for i in phone_book:
        number = ""
        for j in i:
            number += j
            if number in list and number != i:
                answer = False
    return answer


solution(["119", "97674223", "1195524421"])
solution(["123", "456", "789"])
solution(["12", "123", "1235", "567", "88"])
