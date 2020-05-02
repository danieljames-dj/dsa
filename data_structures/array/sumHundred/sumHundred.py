def checkIfHundred(cur, next):
    if next > 9:
        sum = 0
        for i in cur:
            sum += i;
        if sum == 100:
            print(cur);
    else:
        cur.append(next);
        checkIfHundred(cur, next + 1);
        cur[len(cur)-1] = -next;
        checkIfHundred(cur, next + 1);
        cur.pop(len(cur)-1);
        cur[len(cur)-1] = cur[len(cur)-1] * 10 + ( -next if (cur[len(cur)-1] < 0) else next);
        checkIfHundred(cur, next + 1);

checkIfHundred([1], 2);