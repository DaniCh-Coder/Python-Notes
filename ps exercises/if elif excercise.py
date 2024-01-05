# Condition if elif exercise
# set n to a value and see what happend
n = 15
ans = []
i = 1
while i <= n :
    if i % 3 == 0 and i% 5 == 0:
        ans.append("Dream Team")
    elif i % 3 == 0:
        ans.append("Dream Tree")
    elif i % 5 == 0:
        ans.append("Dream Five")
    else:
        ans.append(-1)
    i += 1

print(ans)
