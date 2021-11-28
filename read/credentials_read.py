import pickle

uname_pswd_store = {}

###### Add path according to your system.    #######
with open("credentials.dat", "rb") as f:
    try:
        while True:
            uname_pswd_store.update(pickle.load(f))
    except EOFError:
        pass

print(uname_pswd_store)
