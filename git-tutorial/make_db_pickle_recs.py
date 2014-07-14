from initdata import bob, sue, tom
import pickle

for record in [bob, tom, sue]:
    recfile = open(record['name'].split()[0] + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()
    
