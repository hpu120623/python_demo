import os


def create_path(filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, r'work_data\%s' % filename)
    return DATA_PATH
