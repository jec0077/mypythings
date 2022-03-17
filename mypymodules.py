# TODO: Header
__author__ = 'Josh Campbell'
__email__ = 'adm.jec0077@gmail.com'
__version__ = '1.0.0'
__status__ = 'Production'

import os

# File and Directory Handling
class fileDirectoryHandling(object):
  """File and Directory Handling py class
  
  list of methods:
	- create_dir()
	- read_text_file()
	- append_text_file()
	- write_text_file()
	- remove_text_file()
  
  This class contains methods for create, alter, and remove files and directories in Python"""
  def create_dir(file_dir: str):
    """CREATE DIRECTORY

    arguments:
    - file_dir: string
    
    method create target directory"""
    try:
        os.mkdir(file_dir)
        print(" #directory ", file_dir, " created") 
    except FileExistsError:
        print(" #directory ", file_dir, " already exists")
  
  def read_text_file(file_dir: str, file_name: str):
    """READ TEXT FILE

    arguments:
    - file_dir: string
    - file_name: string
    
    method opens and reads an existing file"""
    try:
      file_name_ext = file_dir + file_name
      f = open(file_name_ext, 'rt')
      print(f.read())
      f.close()
    except FileNotFoundError:
      print(" #" + file_name, " does not exist in directory")
    
  def append_text_file(file_dir: str, file_name: str):
    """APPEND TEXT FILE

    arguments:
    - file_dir: string
    - file_name: string
    
    method opens a file in write-only mode. Then, the file is kept intact if it already exists, and the data you write is appended to what’s already in the file. The file is created if it does not exist in the directory"""
    try:
      file_name_ext = file_dir + file_name
      f = open(file_name_ext, 'at')
      f.write(input("Append to file: \n"))
      f.write("\n")
      f.close()
    except FileNotFoundError:
      print(" #" + file_name, " does not exist in directory")

  def write_text_file(file_dir: str, file_name: str):
    """WRITE TEXT FILE

    arguments:
    - file_dir: string
    - file_name: string
    
    method opens a file in write-only mode. Then, the file is truncated to zero length and overwritten if it already exists, or created if it does not exist in the directory"""
    try:
      file_name_ext = file_dir + file_name
      f = open(file_name_ext, 'wt')
      f.write(input("Write to file: \n"))
      f.write("\n")
      f.close()
    except FileNotFoundError:
      print(" #" + file_name, " does not exist in directory")

  def create_text_file(file_dir: str, file_name: str):
    """CREATE TEXT FILE

    arguments:
    - file_dir: string
    - file_name: string
    
    method creates a new empty file in directory"""
    try:
      file_name_ext = file_name_ext = file_dir + file_name
      f = open(file_name_ext, 'xt')
      f.close()
      print(" #" + file_name, " created")
    except FileExistsError:
      print(" #" + file_name, " already exists")

  def remove_text_file(file_dir: str, file_name: str):
    """REMOVE TEXT FILE

    arguments:
    - file_dir: string
    - file_name: string
    
    method removes a file in directory"""
    try:
      file_name_ext = file_name_ext = file_dir + file_name
      os.remove(file_name_ext)
    except FileNotFoundError:
      print(" #" + file_name, "does not exist in directory")



def main():
  pass

if __name__ == '__main__':
  main()
