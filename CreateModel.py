# Importing Python modules
from sklearn.feature_extraction.text import CountVectorizer
# Importing class files
import GenerateOutput
import ProcessData
import Train_Test

def createModel(training_folder_path,test_data_folder_path,output_path) :
    # Create a dataframe to train the model
    X, gender, age, open, agr, ext, neu, con = ProcessData.createTrainData(training_folder_path)
    count_vect = CountVectorizer()
    X_1 = count_vect.fit_transform(X['like_ids'])
    # Create a dataframe to test the model
    Xp_test = ProcessData.createTestData(test_data_folder_path)
    Xp_test1 = count_vect.transform(Xp_test['like_ids'])
    # Create a Machine Learning model
    classifier_model = "LR"
    regression_model = "LR"
    gender_predicted, age_predicted = Train_Test.classificationModel(classifier_model, X_1, Xp_test1, gender, age)
    ope_predicted, agr_predicted, ext_predicted, neu_predicted, con_predicted = Train_Test.regressionModel(regression_model, X_1, Xp_test1, open, agr, ext, neu, con)
    GenerateOutput.generateXml(Xp_test, gender_predicted, age_predicted, ope_predicted, agr_predicted, ext_predicted, neu_predicted, con_predicted, output_path)