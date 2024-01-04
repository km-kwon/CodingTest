### 달리기 경주

---

성공 코드

```
def solution(players, callings):
    dict_player = {player: idx for idx,player in enumerate(players)}
    for call in callings:
        index = dict_player[call]

        dict_player[players[index]] = index-1
        dict_player[players[index-1]] = index

        players[index-1], players[index] = players[index], players[index-1]
    return players

solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])
```
사용 개념
- dictionary 자료형
- dictionary 자료형 선언 enumerate
- for
---
실패 코드
```
import copy
def solution(players, callings):
    for call in callings:
        index = players.index(call)
        players[index-1], players[index] = players[index], players[index-1]
    return players
```
실패 원인
- index의 시간 복잡도는 O(n)임
- dictionary의 시간 복잡도는 O(1)임

그래서 index는 최대 O(n^2)
dictionary의 시간 복잡도는 최대O(n)


