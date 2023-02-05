def solution(arr):
    answer = [0, 0]
    length = len(arr)
    
    def compress(r, c, length):
        start = arr[r][c]
        for i in range(r, r + length):
            for j in range(c, c + length):
                if arr[i][j] != start:
                    length = length // 2
                    compress(r, c, length)
                    compress(r, c + length, length)
                    compress(r + length, c, length)
                    compress(r + length, c + length, length)
                    return
        answer[start] += 1
    
    compress(0, 0, length)
    return answer