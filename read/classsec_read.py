import pickle

class_sec_store = {}

###### Add path according to your system.    #######
with open(r"classsec.dat", "rb") as f:
    try:
        while True:
            class_sec_store.update(pickle.load(f))
    except EOFError:
        pass

print(class_sec_store)

