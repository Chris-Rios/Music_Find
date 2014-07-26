# Chris Rios
# Finds the specified file type, either .mp3, .flac, .wav, or all 3, and copies it to a speicfied folder.

import sys
import re
import os
import shutil


def folder_crawler(dir_name,file_type):
    '''Explores all folders and sub folders for the speicified file type'''
    paths = os.listdir(dir_name)
    print(paths)
    for path in paths:
        if path.endswith(file_type):
            print("found an mp3 called %s in %s" %(path,dir_name))
        elif os.path.isdir(os.path.join(dir_name,path)) and not path.startswith("."):
            print("found a directory %s" %path)
            folder_crawler(os.path.join(dir_name,path),file_type)
            print("finished with %s" %path)
        else:
            print("%s is not an %s or a directory" %(path,file_type))    




def main():
    file_type= input('Please enter file type,"mp3","."flac" or "wav", or "all"\n')
    if (not file_type=='mp3' and not file_type=='flac'
        and not file_type=='wav' and not file_type=='all'):
    	print ("%s is not a proper option" % file_type)
    	sys.exit(1)
    
    source_folder=input('Please enter a folder to search\n')
    if not os.path.exists(source_folder):
        print ('Folder %s does not exist' % source_folder)
        sys.exit(1)
    
    destination_folder= input('Please enter a destination folder\n')
    if not os.path.exists(destination_folder):
        create_folder = input('Folder %s does not exist, create new folder, yes or no\n' %destination_folder)
        if not create_folder =='yes' and not create_folder =='y':
            print('Aborting program')
            sys.exit(1)
        else:
            os.mkdir(destination_folder)
            print('folder %s created' %destination_folder)
            folder_crawler(source_folder,file_type)
    else:
        folder_crawler(source_folder,file_type)


if __name__ == "__main__":
  main()
	 
