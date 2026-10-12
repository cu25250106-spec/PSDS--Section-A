N, K = map(int, input("Enter N and K: ").split())

arr = list(map(int, input("Enter array elements: ").split()))
window_sum = sum(arr[:K])

max_sum = window_sum

for i in range(K, N):
    window_sum = window_sum + arr[i] - arr[i - K]

    max_sum = max(max_sum, window_sum)

print("Maximum Sum:", max_sum)




'''s = input()
seen = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    max_length = max(max_length, right - left + 1)

print(max_length)'''



'''n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

INF = float('inf')
dp = [INF] * (n + 1)
dp[1] = 0
for _ in range(k):
    new_dp = dp.copy()

    for u, v, w in edges:
        if dp[u] != INF:
            new_dp[v] = min(new_dp[v], dp[u] + w)

        if dp[v] != INF:
            new_dp[u] = min(new_dp[u], dp[v] + w)
    dp = new_dp
if dp[n] == INF:
    print(-1)
else:
    print(dp[n])'''
