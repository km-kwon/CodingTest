import copy

def solution(players, callings):
    dict_player = {player: idx for idx,player in enumerate(players)}
    for call in callings:
        index = dict_player[call]

        dict_player[players[index]] = index-1
        dict_player[players[index-1]] = index

        players[index-1], players[index] = players[index], players[index-1]
    return players

solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])


"""import copy
def solution(players, callings):
    for call in callings:
        index = players.index(call)
        players[index-1], players[index] = players[index], players[index-1]
    return players
"""


