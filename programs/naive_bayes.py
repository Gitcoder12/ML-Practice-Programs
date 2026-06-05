"""
Gaussian Naive Bayes from Scratch
Assumes features are normally distributed per class.
"""
import numpy as np

class GaussianNaiveBayes:
    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        self.classes = np.unique(y)
        self.priors = {}
        self.means = {}
        self.vars = {}

        for c in self.classes:
            X_c = X[y == c]
            self.priors[c] = len(X_c) / len(X)
            self.means[c] = X_c.mean(axis=0)
            self.vars[c] = X_c.var(axis=0) + 1e-9  # smoothing

    def _log_likelihood(self, x: np.ndarray, c: int) -> float:
        mean, var = self.means[c], self.vars[c]
        log_prob = -0.5 * np.sum(np.log(2 * np.pi * var) + ((x - mean) ** 2) / var)
        return log_prob + np.log(self.priors[c])

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.array([
            max(self.classes, key=lambda c: self._log_likelihood(x, c))
            for x in X
        ])

    def accuracy(self, X: np.ndarray, y: np.ndarray) -> float:
        return float(np.mean(self.predict(X) == y))

if __name__ == "__main__":
    np.random.seed(0)
    X0 = np.random.randn(50, 2) + [1, 1]
    X1 = np.random.randn(50, 2) + [5, 5]
    X = np.vstack([X0, X1])
    y = np.array([0] * 50 + [1] * 50)

    split = 80
    clf = GaussianNaiveBayes()
    clf.fit(X[:split], y[:split])
    print(f"Accuracy: {clf.accuracy(X[split:], y[split:]):.2%}")
