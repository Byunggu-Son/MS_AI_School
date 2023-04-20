def solution(arr):
    answer=[]
    # answer = list(set(arr)), 오름차순으로 정렬되므로 set은 불가
    for i in range(len(arr)):
        if arr[i] not in answer or arr[i] != arr[i-1]:
            answer.append(arr[i]) #list에 넣을 때는 +=로 하면 오류뜨니 append()로 추가
    return answer