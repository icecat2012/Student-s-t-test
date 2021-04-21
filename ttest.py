import numpy as np

def unpaired_equal_variance(a, b):
	a, b = np.array(a), np.array(b)
	a_mean, b_mean = np.mean(a), np.mean(b)
	a_var, b_var = np.var(a), np.var(b)
	t = (a_mean-b_mean)/(np.sqrt((a_var/len(a))+(b_var/len(b))))
	df = ((a_var/len(a)+b_var/len(b))**2) / (((a_var/len(a))**2)/(len(a)-1) + ((b_var/len(b))**2)/(len(b)-1) )
	return t, df

def unpaired_not_equal_variance(a, b):
	a, b = np.array(a), np.array(b)
	a_mean, b_mean = np.mean(a), np.mean(b)
	a_var, b_var = np.var(a), np.var(b)
	sp = ((len(a)-1)*a_var+(len(b)-1)*b_var)/(len(a) + len(b) - 2)
	t = (a_mean-b_mean) / (np.sqrt((sp/len(a))+(sp/len(b))))
	df = len(a) + len(b) - 2
	return t, df

def paired(a, b):
	a, b = np.array(a), np.array(b)
	a_mean, b_mean = np.mean(a), np.mean(b)
	a_var, b_var = np.var(a), np.var(b)
	c, cc = list(), list()

	for i in range(len(a)):
		c.append(a[i]-b[i])
		cc.append((a[i]-b[i])*(a[i]-b[i]))
	c, cc = np.array(c), np.array(cc)

	t = np.sum(c) / (np.sqrt((len(c)*np.sum(cc)-(np.sum(c)**2))/(len(c)-1)))
	df = len(c)-1
	return t, df

def two_samples(a, b, isPaired):
	if isPaired:
		t, df = paired(a, b)
	else:
		if np.round(np.var(np.array(a)), 5) == np.round(np.var(np.array(b)), 5):
			t, df = unpaired_equal_variance(a, b)
		else:
			t, df = unpaired_not_equal_variance(a, b)
	return t, df

def one_sample(a, mu):
	a = np.array(a)
	a_mean = np.mean(a)
	s = np.sqrt(sum([ (i-a_mean)**2 for i in a])/(len(a)-1))
	t = (a_mean-mu)/(s/np.sqrt(len(a)))
	df = len(a)-1
	return t, df

def main():
	a = [26.3, 26.43, 26.28, 26.19, 26.49]
	b = [26.22, 26.32, 26.2, 26.11, 26.42]

	t, df = one_sample(a, mu=0.5)
	print(t, df)

	t, df = two_samples(a, b, isPaired=True)
	print(t, df)

	t, df = unpaired_not_equal_variance(a, b)
	print(t, df)

	t, df = unpaired_equal_variance(a, b)
	print(t, df)

if __name__ == '__main__':
	main()