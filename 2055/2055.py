def platesBetweenCandles(s, queries):
    s = list(s)
    ans = []
    for query in queries:
        begin = query[0]
        end = query[1]
        stick1 = 0
        stick2 = 0
        a = 0
        flag = False
        for j in range(begin, end + 1):
            if s[j] == '|':
                stick1 = j
                flag = True
                break
        if flag:
            for i in range(stick1 + 1, end + 1):
                if s[i] == '|':
                    stick2 = i
                    a = a + stick2 - stick1 - 1
                    stick1 = stick2
        else:
            a = 0
        ans.append(a)
    return ans


if __name__ == '__main__':
    ss = "***|**|*****|**||**|*"
    qqueries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
    print(platesBetweenCandles(ss, qqueries))
