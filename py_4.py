import scipy.special
n = float(input())  # white balls
m = float(input())  # black balls
k = float(input())    # number of balls drawn
if k == 1:   # always 1, we draw 1 ball
    print(1)
elif k > n and k > m:   # if we want to draw more balls then we have
    print(0)
elif n < k <= m:    # if there is less white balls than we want to draw
    print((scipy.special.binom(m, k)) / (scipy.special.binom((n + m), k)))
elif m < k <= n:    # if there is less black balls then we want to draw
    print((scipy.special.binom(n, k)) / (scipy.special.binom((n + m), k)))
else:
    print((scipy.special.binom(m, k) + scipy.special.binom(n, k)) / (scipy.special.binom((n + m), k)))




