import pickle

dbfilename = 'people-pickle'

dbfile = open(dbfilename, 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

dbfile = open(dbfilename, 'wb')
pickle.dump(db, dbfile)
dbfile.close()