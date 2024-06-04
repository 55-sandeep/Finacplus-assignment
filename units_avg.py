def find_avg(units):
    units_cnt = 0
    units.sort(reverse=True)
    for val in range(100) :
        cur_cnt = 0
        for i in units :
            if val>=i :
                count = val//i
                cur_cnt += count
                val -= i*count
        units_cnt += cur_cnt
    return units_cnt/100

units = list(map(int,input().split()))
print("AVG of units =",find_avg(units))
