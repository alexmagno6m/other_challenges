#Day 17 - More excepctions
class Calculator(object):
    def power(self, n, p):
        self.n = n
        self.p = p
        if self.n >= 0 and self.p >= 0:
            total = self.n ** self.p
            return total
        else:
            raise Exception('n and p should be non-negative')


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
