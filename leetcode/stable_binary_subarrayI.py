def StableBinarySubarrayI(zero, one, limit):
    MOD = 10**9 + 7
    memo = {}

    def Solve(z, o, last):
        if z == 0 and o == 0:
            return 1
        
        state = (z, o, last)
        if state in memo:
            return memo[state]
        
        res = 0
        if last == 1: 
            for k in range(1, min(z, limit) + 1):
                res = (res + Solve(z - k, o, 0)) % MOD
        else: 
            for k in range(1, min(o, limit) + 1):
                res = (res + Solve(z, o - k, 1)) % MOD
        
        memo[state] = res
        return res

    return (Solve(zero, one, 0) + Solve(zero, one, 1)) % MOD
    


print(StableBinarySubarrayI(1,1,2))