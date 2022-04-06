from sklearn import linear_model 
from joblib import dump, load

class AnomalyDetector:

    def __init__(self) -> None:
        self.clf = linear_model.SGDOneClassSVM()
        self.path = "model/anomaly_detector.joblib"
        self.load_model(self.path)

    def fit(self, X):
        self.clf.fit(X)
    
    def load_model(self, path):
        self.clf = load(self.path)

    def predict(self, X):
        return self.clf.predict(X)

    def save_model(self):
        dump(self.clf, self.path)

    def update_model(self, X):
        self.fit(X)
        self.save_model(self.path)