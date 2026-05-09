class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # try with sieve approch 
        num = 2
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        while num * num < n:
            if is_prime[num]:

                for multiple in range(num * num , n , num):
                    is_prime[multiple] = False
            
            num += 1
        
        return sum(is_prime)


            