import os
import glob

home = os.path.expanduser('~')
path = os.path.join(home, 'F:\Coding with Strangers\AutoYoutube')

# path_a = path +"/*mfa"
path_a = os.path.join(path, "*.m4a")
list_of_files = glob.glob(path_a)
latest_file = max(list_of_files, key=os.path.getctime)


new_file =  os.path.join(path, "podcast.m4a")
print(latest_file)
os.rename(latest_file, new_file)


#I still love you