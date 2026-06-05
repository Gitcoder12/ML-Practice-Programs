"""
K-Nearest Neighbours Classifier from Scratch
No sklearn — pure numpy to understand distance-based classification.
"""
import numpy as np
from collections import Counter

def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(np.sum((a - b) ** 2)))

class KNNClassifier:
    def __init__(self, k: int = 3):
        if k < 1:
            raise ValueError("k must be >= 1")
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        self.X_train = X
        self.y_train = y

    def predict_single(self, x: np.ndarray) -> int:
        distances = [euclidean_distance(x, xi) for xi in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_labels = [self.y_train[i] for i in k_indices]
        return Counter(k_labels).most_common(1)[0][0]

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.array([self.predict_single(x) for x in X])

    def accuracy(self, X: np.ndarray, y: np.ndarray) -> float:
        return float(np.mean(self.predict(X) == y))

if __name__ == "__main__":
    np.random.seed(42)
    # Two separable classes
    class0 = np.random.randn(30, 2) + np.array([0, 0])
    class1 = np.random.randn(30, 2) + np.array([4, 4])
    X = np.vstack([class0, class1])
    y = np.array([0] * 30 + [1] * 30)

    split = int(0.8 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    for k in [1, 3, 5, 7]:
        clf = KNNClassifier(k=k)
        clf.fit(X_train, y_train)
        acc = clf.accuracy(X_test, y_test)
        print(f"k={k}  accuracy={acc:.2%}")
