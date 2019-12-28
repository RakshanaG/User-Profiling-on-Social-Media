# Importing python modules
from sys import argv
# Importing class files
import CreateModel

# Input path
test_data_folder_path = str(argv[1])
training_folder_path = str('/data/training/')
# Output path
output_path = str(argv[2])
CreateModel.createModel(training_folder_path, test_data_folder_path, output_path)
