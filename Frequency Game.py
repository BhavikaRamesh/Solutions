def LargButMinFreq(arr,n):
    #code here
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            
    values = sorted(d.items(), key = lambda v: v[1])
    minValue = values[0][1]
    maxi = 0
    for k, v in d.items():
        if v == minValue:
            maxi = max(maxi, k)
    return maxi
