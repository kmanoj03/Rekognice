import pickle

details_store = {}

###### Add path according to your system.    #######
with open("student_details.dat", "rb") as f:
    try:
        while True:
            details_store.update(pickle.load(f))
    except EOFError:
        pass

print(details_store)
