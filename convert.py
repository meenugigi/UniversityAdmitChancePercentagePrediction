import pickle
file_name='my_file.pkl'
f = open(file_name,'wb')
pickle.dump(my_data,f)
f.close()