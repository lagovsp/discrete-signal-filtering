import math
import random
import copy
from input import *
from weighing_combining_criteria import weigh_combine_criteria

X = [k * (X_MAX - X_MIN) / K for k in range(K + 1)]
Q = [random.uniform(-A, A) for k in range(K + 1)]
F = [f(X_MIN + k * (X_MAX - X_MIN) / K) for k in range(K + 1)]
FN = [F[i] + Q[i] for i in range(K + 1)]
LAMBDA = [l / L for l in range(L + 1)]


def m_from(r):
	return int((r - 1) / 2)


def w(f):
	return (sum([(f[k] - f[k - 1]) ** 2 for k in range(1, K + 1)])) ** 0.5


def delta(f, fn):
	return sum([((f[k] - fn[k]) ** 2) / K for k in range(K + 1)]) ** 0.5


def dist(f, fn):
	return (w(f) ** 2 + delta(f, fn) ** 2) ** 0.5


def random_a(r):
	M = m_from(r)
	a = [None for i in range(r)]
	a[M] = random.uniform(0, 1)
	for m in range(2, M + 1):
		val = 0.5 * random.uniform(0, 0.1 - sum([a[s - 1] for s in range(m + 1, r - m + 1)]))
		a[m - 1] = val
		a[r - m] = val
	val = 0.5 * (1 - sum([a[s - 1] for s in range(2, r)]))
	a[0] = val
	a[r - 1] = val
	return a

def avg_harmony(k, r):
	M = m_from(r)
	return math.pow(sum([a[j + M + 1 - k] / FN[j] for j in range(k - M, k + M + 1)]), -1)


def random_search(q, p, l, r, f):
	n = math.ceil(math.log(1 - p) / math.log(1 - q))
	f_min = math.inf
	for it in range(n):
		val = f(random.uniform(l, r))
		f_min = val if val < f_min else f_min
	return f_min


def main():
	a = random_a(R1)
	print(a)
	return 0


if __name__ == '__main__':
	main()
