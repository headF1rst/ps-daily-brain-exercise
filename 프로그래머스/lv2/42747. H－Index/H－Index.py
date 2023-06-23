def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)  # 내림차순으로 정렬하여 높은 인용 횟수부터 확인
    
    for i, citation in enumerate(citations):
        if citation < i + 1:
            return i  # 인용 횟수가 현재 논문의 순위보다 작아지면 그 전 순위까지가 H-Index
    
    return n  # 모든 논문의 인용 횟수가 현재 논문의 순위보다 크거나 같은 경우, H-Index는 논문의 개수
