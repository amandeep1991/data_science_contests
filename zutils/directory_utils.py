import os

def get_data_directory():
    print("Old Directory was:: " + os.getcwd())
    directory_1 = os.getcwd() + "/data"
    condition_1 = os.getcwd().endswith("data_science_contests")
    directory_2 = "./data/"
    condition_2 = os.getcwd().endswith("data")
    directory_3 = os.getcwd() + "/../data"
    absolute_input_data_path = directory_1 if condition_1 else directory_2 if condition_2 else directory_3
    return absolute_input_data_path