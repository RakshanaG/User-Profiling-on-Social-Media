# Importing Python modules
import pandas as pd

def createTrainData(training_folder_path):
    relation = pd.read_csv(training_folder_path+"relation/relation.csv")
    relation['like_id'] = relation['like_id'].apply(str)
    relation = relation.groupby('userid')['like_id'].apply(' '.join).reset_index()
    relation['like_id'] = relation['like_id'].apply(str)
    profile = pd.read_csv(training_folder_path+"profile/profile.csv")
    profile['like_ids'] = ""
    profile['like_ids'] = profile['like_ids'].apply(str)
    for i in range(0, len(profile)):
        row = relation.loc[relation['userid'] == profile.loc[i, 'userid']]
        likeid = row['like_id'].item()
        profile.at[i, 'like_ids'] = likeid

    data = profile[['userid', 'like_ids', 'gender', 'age', 'ope', 'agr', 'ext', 'neu', 'con']]

    X = data[['userid', 'like_ids']]
    gender = data[['gender']]
    age = pd.DataFrame(columns=['age'])
    y1 = []
    age1 = data['age'].to_numpy()
    print(type(age1))
    for i in range(len(age1)):
        if 0 <= age1[i] <= 24:
            y1.append("xx-24")
        elif 25 <= age1[i] <= 34:
            y1.append("25-34")
        elif 35 <= age1[i] <= 49:
            y1.append("35-49")
        else:
            y1.append("50-xx")
    age['age'] = y1
    open = data[['ope']]
    agr = data[['agr']]
    ext = data[['ext']]
    neu = data[['neu']]
    con = data[['con']]
    return X, gender, age, open, agr, ext, neu, con


def createTestData (test_data_folder_path):
    relation1 = pd.read_csv(test_data_folder_path+"relation/relation.csv")
    relation1['like_id'] = relation1['like_id'].apply(str)
    relation1 = relation1.groupby('userid')['like_id'].apply(' '.join).reset_index()
    relation1['like_id'] = relation1['like_id'].apply(str)
    profile1 = pd.read_csv(test_data_folder_path+"profile/profile.csv")
    profile1['like_ids'] = ""
    profile1['like_ids'] = profile1['like_ids'].apply(str)
    for i in range(0, len(profile1)):
        row = relation1.loc[relation1['userid'] == profile1.loc[i, 'userid']]
        likeid = row['like_id'].item()
        profile1.at[i, 'like_ids'] = likeid
    data = profile1[['userid', 'like_ids']]
    return data
