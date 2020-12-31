import random
import string
import pickle


def getID(name, path):
    IDs = pickle.load(open(path, "rb"))
    if name in IDs:
        return IDs[name]
    else:
        print(name + " not in IDs, generating new ID")
        newID = generateNewID(name, IDs)
        pickle.dump(IDs, open(path, "wb"))
        return newID


def generateNewID(name, dict):
    newID = ""
    while newID not in dict.values():
        newID = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        if newID not in dict.values():
            dict.update({name: newID})
        else:
            print("ID already taken!")
    return newID
