import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', header = None,  sep = '\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.head()

import numpy as np 


class LinearRegressionGD(object):

	def __init__(self, eta = 0.001, n_iter = 20):
		self.eta = eta
		self.n_iter = n_iter

	def net_input(self, X):
		return np.dot(X, self.w_[1:]) + self.w_[0]

	def predict(self, X):
		return self.net_input(X)

	def fit(self, X, y):
		self.w_ = np.zeros(1 + X.shape[1])
		self.cost_ = []

		for i in range(self.n_iter):
			output = self.net_input(X)
			errors = (y - output)
			self.w_[1:] += self.eta * X.T.dot(errors)
			self.w_[0] += self.eta * errors.sum() 
			cost = (errors ** 2).sum() / 2.0
			self.cost_.append(cost)
		return self

# ----------------------------------------------------------

X = df[['RM']].values
y = df['MEDV'].values

from sklearn.preprocessing import StandardScaler		# estandarizamos las muestras

sc_x = StandardScaler()
sc_y = StandardScaler()

X_std = sc_x.fit_transform(X)
y_std = sc_y.fit_transform(y)

lr = LinearRegressionGD()

lr.fit(X_std, y_std)

import matplotlib.pyplot as plt 

def lin_regplot(X, y, model):
	plt.scatter(X, y, c = 'blue')
	plt.plot(X, model.predict(X), color = 'red')
	return None

lin_regplot(X_std, y_std, lr)

plt.xlabel('Average number of rooms [RM] (standarized)')
plt.ylabel('Prize in $1000\'s [MEDV] (standarized)')
plt.show()