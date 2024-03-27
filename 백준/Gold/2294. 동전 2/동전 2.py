import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
coins = sorted(list(set(coins)))

dp = [k + 1] * (k + 1)
dp[0] = 0

for coin in coins:
    if coin > k:
        break
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == k + 1:
    print(-1)
else:
    print(dp[k])