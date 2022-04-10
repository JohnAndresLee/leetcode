def convertToBase7(num):
    ans = []
    flag = True
    if num < 0:
        num = -num
        flag = False
    while num >= 7:
        a = num % 7
        ans.append(str(a))
        num = int((num - a) / 7)
    ans.append(str(num))
    ans = list(reversed(ans))
    s = ''
    s = s.join(ans)
    if not flag:
        s = '-'+s
    print(s)


if __name__ == "__main__":
    convertToBase7(-7)
