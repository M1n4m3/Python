

# Base class for machine learning models
class MLModel:
    def __init__(self):
        self.model = None

    def train(self, X, y):
        raise NotImplementedError("Subclass must implement train method.")

    def predict(self, X):
        raise NotImplementedError("Subclass must implement predict method.")

    def evaluate(self, X, y):
        predictions = self.predict(X)
        mse = mean_squared_error(y, predictions)
        print("Mean Squared Error:", mse)

# Derived class for Linear Regression
class LinearRegressionModel(MLModel):
    def __init__(self):
        super().__init__()
        self.model = LinearRegression()

    
       
