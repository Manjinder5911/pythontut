import requests
import pickle
r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

f = open("newfile.txt",'wb')
f.write(r.content)
f.close()

f = open("newfile.txt",'rb')
a = f.read().splitlines()
f.close()

fileobj = open("newfile.txt",'wb')
pickle.dump(a,fileobj)
fileobj.close()

fileobj = open("newfile.txt",'rb')
print(pickle.load(fileobj))
