import numpy as np

def weighted_mae(y_true, y_pred, weights=None):
    """Compute Weighted Mean Absolute Error."""
    if weights is None:
        weights = np.ones_like(y_true)
    return np.sum(weights * np.abs(y_true - y_pred)) / np.sum(weights)
