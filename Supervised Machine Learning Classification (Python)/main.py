#https://archive.ics.uci.edu/dataset/225/ilpd+indian+liver+patient+dataset

import pandas as pd
# Using ucimlrepo to fetch the dataset
from ucimlrepo import fetch_ucirepo

# Fetch dataset from UCI ML Repository by id 225 by name "ILPD (Indian Liver Patient Dataset)"
dataset = fetch_ucirepo(id=225) # This

X = dataset.data.features # This is the dataset in numpy array format
Y = dataset.data.targets # This is the target in numpy array format

# Create a DataFrame with the features by pandas
df = pd.DataFrame(X, columns=dataset.data.feature_names)

# Add the target as a new column
df['Selector'] = Y

# Print the first 5 rows of the dataset
print(df.head())



# First we need to preprocess the data
# Convert categorical data to numerical data (String to Integer)
# Convert Male to 0 and Female to 1 in the Gender column
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Fill the missing values with the mean of the column
df = df.fillna(df.mean())
df = df.infer_objects(copy=False)
#After this step, we have a clean dataset with no missing values and all the columns are in numerical format.
print(df.head())

# Scale the data so that all the features have the same scale.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop('Selector', axis=1))


# Splitting the dataset into training and testing sets after scaling
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, df['Selector'], test_size=0.2, random_state=42)


# We trained three different classifier models on the Indian Liver Patient Dataset (ILPD) to predict the presence of liver disease.
# The three models are:
# 1. Logistic Regression
# 2. Random Forest
# 3. Support Vector Machine (SVM)



# Logistic Regression
from sklearn.linear_model import LogisticRegression
logisticReg = LogisticRegression()
logisticReg.fit(X_train, Y_train)
logisticReg_score = logisticReg.score(X_test, Y_test)
print("Logistic Regression Score: ", logisticReg_score)

# Random Forest
from sklearn.ensemble import RandomForestClassifier
randomForest = RandomForestClassifier()
randomForest.fit(X_train, Y_train)
randomForest_score = randomForest.score(X_test, Y_test)
print("Random Forest Score: ", randomForest_score)

# Support Vector Machine (SVM)
from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train, Y_train)
svc_score = svc.score(X_test, Y_test)
print("SVM Score: ", svc_score)

