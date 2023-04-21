def solution(rsp):
    answer = ''
    # 가위 : 2, 바위 : 0, 보 : 5
    if len(rsp)<=0:
        return False
    # if len(rsp) !=len(answer):
    #     return False
    for i in range(len(rsp)):
        if rsp[i] == '2':
            answer += '0'
        if rsp[i] == '0':
            answer +='5'
        if rsp[i] == '5':
            answer += '2'
    return answer