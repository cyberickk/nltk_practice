def solution(keyword, text):
    pun = [i for i, j in enumerate(text) if j == '.' or j == '?' or j == '!']
    sunset = [i for i, j in enumerate(text) if j == keyword]
    ans = []
    flag = 0
    for i in range(len(sunset)):
        j = flag
        while j < len(pun):
            if sunset[i] < pun[j] and pun[j - 1] < sunset[i]:
                ans.append([pun[j - 1] + 1, pun[j] + 1])
                flag = j + 1
                break
            j += 1
    # print ans
    for i in range(len(ans)):
        print ('start from %d to end in %d' % (ans[i][0], ans[i][1]))
        print (' '.join(text[ans[i][0]: ans[i][1]]))






