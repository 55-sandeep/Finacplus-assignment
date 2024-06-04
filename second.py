def find(units):
    ans = 0
    units.sort(reverse=True)
    for val in range(100) :
        cur = 0
        for i in units :
            if val>=i :
                count = val//i
                cur += count
                val -= i*count
        ans += cur
    return ans/100

units = list(map(int,input().split()))
print("AVG of units =",find(units))