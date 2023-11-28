def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fpm(b, e, m):
    t = 1
    while e:
        if e & 1:
            t = t * b % m
        e >>= 1
        b = b * b % m
    return t

p, q = 1009, 3643

cnt_p = [0] * 10000
cnt_q = [0] * 10000

for e in range(p - 1):
    for i in range(p):
        cnt_p[e] += fpm(i, e, p) == i

for e in range(q - 1):
    for i in range(q):
        cnt_q[e] += fpm(i, e, q) == i

phi = (p - 1) * (q - 1)
min_ans = phi
ans = 0

for e in range(2, phi):
    if gcd(e, phi) == 1:
        min_ans = min(min_ans, cnt_p[e % (p - 1)] * cnt_q[e % (q - 1)])

for e in range(2, phi):
    if gcd(e, phi) == 1 and cnt_p[e % (p - 1)] * cnt_q[e % (q - 1)] == min_ans:
        ans += e

print(ans)


