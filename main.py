import matplotlib.pyplot as mpl
from source import *
from weighing_combining_criteria import weigh_combine_criteria


def main():
	stochastic_filtering(R1)
	mpl.plot(X, FN, label = 'noisy')
	mpl.plot(X, F, label = 'f(x) = sin(x) + 0.5', )
	mpl.legend()
	mpl.show()
	return 0


if __name__ == '__main__':
	main()
