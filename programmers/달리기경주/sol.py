# def solution(players, callings):
#     a = 0
#     while a < len(callings):
#         for i in callings:
#             old = players.index(i) #불린 선수 전 등수
#             players[old] = players[old-1] # 밀린 선수
#             players[old-1] = i #역전 선수
#             a += 1
        
#     return players

def solution(players, callings):
    player_dict = {player: idx for idx, player in enumerate(players)}
    for call in callings:
        idx = player_dict[call] #call의 등수
        
        # 등수에 따라서 자리 바꾸기
        players[idx], players[idx-1] = players[idx-1], players[idx]
        # 바꾼 자리를 dict에 반영
        player_dict[players[idx]] = idx
        player_dict[players[idx-1]] = idx-1
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))