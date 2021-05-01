from random import randint, seed

scores = [randint(1, 10) for i in range(0, 20)]
wait = [randint(1, 5) for i in range(0, 20)]
n = 10


def findMaxScore(currSong):
    if currSong >= n:
        return 0
    else:
        return max(scores[currSong] + findMaxScore(currSong + wait[currSong]), findMaxScore(currSong+1))


setOfBills = [365, 91, 52, 28, 13, 7, 4, 1]


def giveFewestDreamDollars(change, billsToUse):
    if (change == 0):
        return billsToUse
    else:
        for bill in setOfBills:
            if bill <= change:
                billsToUse.append(bill)
                return giveFewestDreamDollars(change - bill, billsToUse)


def memoizedFewestDreamDollars(change):
    dpChange = [0 for i in range(0, change+1)]
    print(len(dpChange))
    for i in range(0, len(dpChange)):
        for bill in setOfBills:
            if bill <= change:
                dpChange[i] = max(dpChange[i], bill + dpChange[change-bill])
    return dpChange[change]


#print(giveFewestDreamDollars(123, []))
# print(memoizedFewestDreamDollars(123))


def memofib(n):
    count = 0
    dpFib = [0 for i in range(0, n+1)]
    dpFib[0] = 0
    dpFib[1] = 1
    dpFib[2] = 1
    for i in range(3, n+1):
        count = count + 1
        dpFib[i] = dpFib[i-1] + dpFib[i-2]

    return dpFib[n], count


print(memofib(200))

count2 = 0


def fib(n):
    global count2
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    count2 = count2 + 1
    return fib(n-1) + fib(n-2)


print(fib(200), count2)
