# Importing Python modules
import sys
from keras import Sequential
from keras.layers import Dense
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


def classificationModel(gender_clf_model, train_data, test_data, gender, age):
    if gender_clf_model == "LR":
        gender_clf = LogisticRegression()
        gender_clf.fit(train_data, gender.values.ravel())
        age_clf = LogisticRegression(solver='sag',multi_class='multinomial')
        age_clf.fit(train_data, age.values.ravel())
    elif gender_clf_model == "NB":
        gender_clf = MultinomialNB()
        gender_clf.fit(train_data, gender.values.ravel())
        age_clf = MultinomialNB()
        age_clf.fit(train_data, age.values.ravel())
    elif gender_clf_model == "SVM":
        gender_clf = SVC(kernel='linear')
        gender_clf.fit(train_data, gender.values.ravel())
        age_clf = SVC(kernel='linear')
        age_clf.fit(train_data, age.values.ravel())
    elif gender_clf_model == "KNN":
        gender_clf = KNeighborsClassifier(n_neighbors=15)
        gender_clf.fit(train_data, gender.values.ravel())
        age_clf = KNeighborsClassifier(n_neighbors=9)
        age_clf.fit(train_data, age.values.ravel())
    elif gender_clf_model == "MLP":
        gender_clf = Sequential()
        gender_clf.add(Dense(500, activation='relu', kernel_initializer='random_normal', input_dim=train_data.shape[1]))
        gender_clf.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))
        gender_clf.compile(optimizer ='adam', loss='binary_crossentropy', metrics =['accuracy'])
        gender_clf.fit(train_data, gender, batch_size=32, epochs=1)
        age_clf = Sequential()
        age_clf.add(Dense(150, activation='relu', kernel_initializer='random_normal', input_dim=train_data.shape[1]))
        age_clf.add(Dense(4, activation='softmax', kernel_initializer='random_normal'))
        age_clf.compile(optimizer ='adam', loss='sparse_categorical_crossentropy', metrics =['accuracy'])
        age_clf.fit(train_data, age, batch_size=32, epochs=2)
    else:
        print("No model found")
        sys.exit()
    gender_predicted = gender_clf.predict(test_data)
    age_predicted = age_clf.predict(test_data)
    return gender_predicted, age_predicted

def regressionModel(regression_model, train_data, test_data, open, agr, ext, neu, con):
    if regression_model == "LR":
        ope_clf = LinearRegression()
        agr_clf = LinearRegression()
        ext_clf = LinearRegression(normalize=True)
        neu_clf = LinearRegression(normalize='True')
        con_clf = LinearRegression(normalize=True)
        ope_clf.fit(train_data, open.values.ravel())
        agr_clf.fit(train_data, agr.values.ravel())
        ext_clf.fit(train_data, ext.values.ravel())
        neu_clf.fit(train_data, neu.values.ravel())
        con_clf.fit(train_data, con.values.ravel())
    elif regression_model == "RFRT":
        ope_clf = RandomForestRegressor(n_estimators = 30, random_state = 100)
        agr_clf = RandomForestRegressor(n_estimators = 30, random_state = 100)
        ext_clf = RandomForestRegressor(n_estimators = 30, random_state = 100)
        neu_clf = RandomForestRegressor(n_estimators = 30, random_state = 100)
        con_clf = RandomForestRegressor(n_estimators = 30, random_state = 100)
        ope_clf.fit(train_data, open.values.ravel())
        agr_clf.fit(train_data, agr.values.ravel())
        ext_clf.fit(train_data, ext.values.ravel())
        neu_clf.fit(train_data, neu.values.ravel())
        con_clf.fit(train_data, con.values.ravel())
    else:
        print("No model found")
        sys.exit()
    ope_predicted = ope_clf.predict(test_data)
    agr_predicted = agr_clf.predict(test_data)
    ext_predicted = ext_clf.predict(test_data)
    neu_predicted = neu_clf.predict(test_data)
    con_predicted = con_clf.predict(test_data)
    return ope_predicted, agr_predicted, ext_predicted, neu_predicted, con_predicted