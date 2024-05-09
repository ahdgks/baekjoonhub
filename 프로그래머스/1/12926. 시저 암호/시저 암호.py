def solution(s, n):
    answer = ''
    for i in s:
        asc=ord(i)
        total_asc=ord(i)+n
        if i ==' ':
            answer+=i
        elif asc>=97:
            if total_asc>122:
                answer+=chr(total_asc-122+96)
            else:
                answer+=chr(total_asc)
        elif asc>=65:
            if total_asc>90:
                answer+=chr(total_asc-90+64)
            else:
                answer += chr(total_asc) 
    return answer