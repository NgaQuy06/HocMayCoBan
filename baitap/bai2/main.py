import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("D:/laptrinh/pythonn/hocmay/baitap/bai2/SMSSpamCollection.csv", sep="\t", header=None, names=["label", "message"])
df

def count_char(message):
    letter_count = 0
    digit_count = 0
    for char in message:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
    return pd.Series([letter_count, digit_count])

df[["letter_count", "digit_count"]] = (df["message"].apply(count_char))

X = df[["letter_count", "digit_count"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=36, stratify=y)

knn = KNeighborsClassifier(n_neighbors=5, metric="euclidean")
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

#new_message = "Congratulations! You won 1000 dollars"
#new_features = count_char(new_message)
#new_X = pd.DataFrame([new_features.values], columns=["letter_count", "digit_count"])
#prediction = knn.predict(new_X)

#print("Tin nhắn:", new_message)
#print("Dự đoán:", prediction[0])

#print("Accuracy:", accuracy_score(y_test, y_pred))