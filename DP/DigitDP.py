from functools import lru_cache

def count_upto(n):
    s = str(n)

    @lru_cache(None)
    def dp(pos, tight, started, state):
        if pos == len(s):
            return 1  # check final state here

        limit = int(s[pos]) if tight else 9
        ans = 0

        for digit in range(limit + 1):
            ntight = tight and (digit == limit)
            nstarted = started or digit != 0

            nstate = state

            if nstarted:
                # update state here
                nstate += digit

            ans += dp(pos + 1, ntight, nstarted, nstate)

        return ans

    return dp(0, True, False, 0)

# count in [L, R]
def count_range(L, R):
    return count_upto(R) - count_upto(L - 1)
