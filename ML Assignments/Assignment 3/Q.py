import pandas as pd
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv('./USA_Housing.csv')
features = data.drop('Price', axis=1)
target = data['Price']

scaler = StandardScaler()
featuresScaled = scaler.fit_transform(features)

kf = KFold(n_splits=5, shuffle=True, random_state=42)

bestCoefficients = None
highestR2 = -float('inf')
for trainIdx, testIdx in kf.split(featuresScaled):
    XTrain, XTest = featuresScaled[trainIdx], featuresScaled[testIdx]
    yTrain, yTest = target.iloc[trainIdx], target.iloc[testIdx]
    
    model = LinearRegression()
    model.fit(XTrain, yTrain)
    predictions = model.predict(XTest)
    r2 = r2_score(yTest, predictions)
    
    if r2 > highestR2:
        highestR2 = r2
        bestCoefficients = model.coef_

splitPoint = int(0.7 * len(featuresScaled))
XTrain, XTest = featuresScaled[:splitPoint], featuresScaled[splitPoint:]
yTrain, yTest = target.iloc[:splitPoint], target.iloc[splitPoint:]

finalModel = LinearRegression()
finalModel.fit(XTrain, yTrain)
finalModel.coef_ = bestCoefficients

testPredictions = finalModel.predict(XTest)
finalR2 = r2_score(yTest, testPredictions)
print('R2 score for 30% test data:', finalR2)
