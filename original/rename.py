import os
os.getcwd()
collection = 'C:/Users/l03002903/Downloads/copy_org'

format = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']

for i, filename in enumerate(os.listdir(collection)):
    
    if filename.endswith(tuple(format)):
        print ("Valid", filename)
        exit_name = filename[:5]  + filename[-4:]
        print(exit_name)
        os.rename(collection + '/' + filename, collection + '/' + exit_name)
    else:
        print ("InValid", filename)        



