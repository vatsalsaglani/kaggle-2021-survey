import json
import pickle

def save_json(object, filepath):
    with open(filepath, 'w') as fp:
        json.dump(object, fp)

def load_json(filepath):
    with open(filepath, 'r') as fp:
        return json.load(fp)

def save_pickle(object, filepath):
    with open(filepath, 'wb') as fp:
        pickle.dump(object, fp)

def load_pickle(filepath):
    with open(filepath, 'rb') as fp:
        return pickle.load(fp)

def add_log(log, filepath, mode="a"):
    with open(filepath, mode) as fp:
        fp.writelines([
            f"""\n{log}\n"""
        ])

flatten = lambda lst: [item for sublist in lst for item in sublist]
