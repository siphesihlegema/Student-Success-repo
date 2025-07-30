from sklearn.ensemble import RandomForestRegressor

def train_model(X, y):
    """Train a simple baseline RandomForest model."""
    model = RandomForestRegressor()
    model.fit(X, y)
    return model
