def substrnorep(s):

    dic, res, start, = {}, 0, 0

    for i, ch in enumerate(s):
        print(i, ch)
        if ch in dic:
            res = max(res, i - start)
            print(res)
            start = max(start, dic[ch] + 1)
            print(start)
        dic[ch] = i
    return max(res, len(s) - start)


y = "gooddaytoyoulaady"

print(substrnorep(y))