"""
Linear Regression from Scratch
Implements gradient descent without sklearn to understand the math.
"""
import numpy as np

def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))

def train(X: np.ndarray, y: np.ndarray, lr: float = 0.01, epochs: int = 1000):
    m, n = X.shape
    weights = np.zeros(n)
    bias = 0.0
    history = []

    for epoch in range(epochs):
        y_pred = X @ weights + bias
        error = y_pred - y

        dw = (2 / m) * (X.T @ error)
        db = (2 / m) * np.sum(error)

        weights -= lr * dw
        bias -= lr * db

        if epoch % 100 == 0:
            loss = mean_squared_error(y, y_pred)
            history.append(loss)

    return weights, bias, history

if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10
    y = 3.5 * X.squeeze() + 7 + np.random.randn(100) * 1.5

    X_norm = (X - X.mean()) / X.std()
    weights, bias, history = train(X_norm, y, lr=0.01, epochs=1000)

    print(f"Learned weight: {weights[0]:.4f}, bias: {bias:.4f}")
    print(f"Final MSE: {history[-1]:.4f}")
    print(f"Loss trajectory: {[f'{l:.2f}' for l in history]}")
