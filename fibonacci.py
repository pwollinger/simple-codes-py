#Fibonacci - Code solution to the fibonacci sequence. Here we have two ways to solve this problem, using recursion and using memoization.

#Fibonacci with recurtion is a elegant way to solve fibonacci because the compact code, but the code cost a lot. Because in this solution we create a binary tree for every recursion we use. Because of that, the Big O notation for this code is O(2^number)
def fibo(number):
    if number < 3:
        return 1
    return fibo(number-1) + fibo(number-2)

#Fibonacci with memoization is a better solution than the normal recursive code because we store the result of a node in the binary tree create for the recursive function so that we can check the already processed result inside the dictionary we create to save those numbers we will use in another node. THe Big O notation for this code is O(n)
def fibo_memo(number, memo = {}):
    if number in memo:
        return memo[number]
    if number < 3:
        return 1
    memo[number] = fibo(number-1, memo) + fibo(number-2, memo)
    return memo[number]  