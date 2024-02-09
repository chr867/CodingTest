def solution(data, ext, val_ext, sort_by):
    answer = [[]]
#   정보 추출 기준
    if ext == 'code':
        ext_idx = 0
    elif ext == 'date':
        ext_idx = 1
    elif ext == 'maximum':
        ext_idx = 2
    elif ext == 'remain':
        ext_idx = 3
#   정보 추출
    data = list(filter(lambda x: x if x[ext_idx] < val_ext else '', data))
#   정렬 기준
    if sort_by == 'code':
        sort_idx = 0
    elif sort_by == 'date':
        sort_idx = 1
    elif sort_by == 'maximum':
        sort_idx = 2
    elif sort_by == 'remain':
        sort_idx = 3
#   정렬
    data.sort(key=lambda x: x[sort_idx], reverse=False)
    answer = data
    return answer