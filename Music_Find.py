# Author:Chris Rios
# Finds the specified file type, either .mp3, .flac, .wav, or all 3, and copies it to a speicfied folder.

import sys
import re
import os
import shutil

music_list={}

def folder_crawler(dir_name,file_type):
    '''Explores all folders and sub folders for the speicified file type, composes a dictionary of all files names, 
       sizes and paths'''
    paths = os.listdir(dir_name)
    
    for path in paths:
        path = os.path.basename(path)         
        abs_path = os.path.abspath(os.path.join(dir_name,path))
        
        if path.endswith(file_type):
            if  not path in music_list:
              music_list[path] = (abs_path,os.path.getsize(abs_path)) 
            elif not os.path.getsize(abs_path) == music_list[path][1]:
                print("already have %s" %path)
                music_list[path] = (abs_path,os.path.getsize(abs_path))
            else:
                print("i will figure it out")
        
        elif os.path.isdir(os.path.join(dir_name,path)) and not path.startswith("."):
            folder_crawler(os.path.join(dir_name,path),file_type)

def copy_list(to_dir):
    for song in music_list:
      print(os.path.basename(song))
      #shutil.copy(song, os.path.join(to_dir, fname))


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
    print(music_list)
    copy_list(destination_folder)

if __name__ == "__main__":
  main()
	 
