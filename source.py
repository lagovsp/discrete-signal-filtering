from prettytable import PrettyTable
from input import *
from sty import *
import random

fg.orange = Style(RgbFg(255, 150, 50))
bg.orange = Style(RgbBg(255, 150, 50))


def f_initial(x):
	return math.sin(x) + 0.5


def m_from(r):
	return int((r - 1) / 2)


def w(a):
	fk = get_f_harmony_list_with_fixed(a)
	print(len(fk))
	# return sum([(a[k] - a[k - 1]) ** 2 for k in range(1, K + 1)]) ** 0.5
	return sum([(fk[k] - fk[k - 1]) ** 2 for k in range(1, K + 1)]) ** 0.5


def delta(a):
	return sum([((a[k] - FN[k]) ** 2) / K for k in range(K + 1)]) ** 0.5


def rand_a(r):
	M = m_from(r)
	a = [random.random() for i in range(r)]
	a[M] = random.uniform(0, 1)
	for m in range(2, M + 1):
		val = 0.5 * random.uniform(0, 0.1 - sum([a[s - 1] for s in range(m + 1, r - m + 1)]))
		a[m - 1] = val
		a[r - m] = val
	val = 0.5 * (1 - sum([a[s - 1] for s in range(2, r)]))
	a[0] = val
	a[r - 1] = val
	return a


def dist(a):
	fh = get_f_harmony_list_with_fixed(a)
	return (w(fh) ** 2 + delta(fh) ** 2) ** 0.5


def get_f_harmony_list_with_fixed(a):
	M = m_from(len(a))
	print(len(a))
	print(len(FN))
	return [sum([a[j + M + 1 - k] / FN[j] for j in range(k - M, k + M + 1)]) ** (-1) for k in range(M, K - M + 1)]


def j(a, lam):
	fh = get_f_harmony_list_with_fixed(a)
	return lam * w(fh) + (1 - lam) * delta(fh)


X = [k * (X_MAX - X_MIN) / K for k in range(K + 1)]
Q = [random.uniform(-A, A) for k in range(K + 1)]
F = [f_initial(X_MIN + k * (X_MAX - X_MIN) / K) for k in range(K + 1)]
FN = [F[i] + Q[i] for i in range(K + 1)]
LAMBDAS = [l / L for l in range(L + 1)]


def passive_search(lambdas, r, e = 0.01):
	return [random_search(P, r, j, lam, e = e) for lam in lambdas]


def random_search(p, r, j, lam, e = 0.01):
	n = int(math.log(1 - p) / math.log(1 - e / (X_MAX - X_MIN)))
	best = [None, None, None, None, None]
	for it in range(n):
		a = rand_a(r)
		if it == 0:
			fh = get_f_harmony_list_with_fixed(a)

			best = [lam, dist(a), a, w(fh), delta(fh)]
		elif j(a, lam) < best[0]:
			fh = get_f_harmony_list_with_fixed(a)

			best = [lam, dist(a), a, w(fh), delta(fh)]
	return best


def stochastic_filtering(r, e = E):
	print(bg.orange + fg.black + 'Stochastic Filtering' + fg.rs + bg.rs)
	print(fg.orange + 'Euclidean' + fg.rs + ' metric used')
	print('r = ' + fg.orange + f'{r}' + fg.rs)
	results = passive_search(LAMBDAS, r, e = e)
	table = PrettyTable()
	table.add_column('h', LAMBDAS)
	table.add_column('dis', [item[1] for item in results])
	table.add_column('alpha', [item[2] for item in results])
	table.add_column('w', [item[3] for item in results])
	table.add_column('d', [item[4] for item in results])
	return 0
