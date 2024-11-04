# 1cm = 10,000,000nm
while True:
    try:
        wide = int(input()) # 채워야할 너비
        n = int(input())    # 블록 수
        block = [int(input()) for _ in range(n)]
        block.sort()
        answer = []
        total = 0
        wide *= 10000000

        start, end = 0, n-1
        while start < end :
            total = block[start] + block[end]
            if total < wide :
                start += 1
            elif total > wide :
                end -= 1
            else :
                answer = [block[start], block[end]]
                break
        if answer :
            print("yes {0} {1}".format(block[start], block[end]))
        else :
            print("danger")
    except :
        break

