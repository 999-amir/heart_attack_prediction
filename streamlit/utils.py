from sklearn.base import BaseEstimator, TransformerMixin


class PreProcessor(BaseEstimator, TransformerMixin):
    def fit(self, X, Y=None):
        return self
    def transform(self, X, Y=None):
        # encode (categorical to numerical)
        X.replace({'Gender': {'Male':0, 'Female':1}}, inplace=True)
        X.replace({'Smoker': {'Yes':1, 'No':0}}, inplace=True)
        # Blood Pressure to sistolic and diastolic
        X[['sistolic(mmHg)', 'diastolic(mmHg)']] = X['Blood Pressure(mmHg)'].str.split('/', expand=True)
        # drop unusefull data
        X.drop(['ID', 'Name', 'Blood Pressure(mmHg)'], inplace=True, axis=1)
        return X