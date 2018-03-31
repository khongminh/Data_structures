# https://www.geeksforgeeks.org/the-stock-span-problem/

def prevLarger(a):
    n = len(a)
    stack = [n-1]
    result = [None] * n

    for i in range(n-2, -1, -1):
        while stack:
            cur = stack[-1]
            if a[cur] < a[i]:
                result[cur] = i
                stack.pop()
            else:
                break
        stack.append(i)
    while stack:
        cur = stack.pop()
        result[cur] = -1
    return result

def calculateSpan(price):
    prevLarge = prevLarger(price)
    result = []
    for i in range(len(price)):
        result.append(i-prevLarge[i])

    return result


price = [100, 80, 60, 70, 60, 75, 85]
print(*calculateSpan(price))