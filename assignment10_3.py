'''Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.
Usage : DirectoryCopy.py “Demo” “Temp”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files from Demo to Temp.'''

import sys
import os
import shutil
def Display(path,temp):
    flag = os.path.isabs(path)
    flag1=os.path.isabs(temp)
    if flag1==False:
        temp=os.path.abspath(temp)
    if flag ==False:
        path=os.path.abspath(path)
        
    exists = os.path.isdir(path)
    exists1 = os.path.isdir(temp)
    
    if exists==True and exists1==True :
        for folder,subfolder1,filename1 in os.walk(temp):
            print(folder)
            
        for foldername,subfolder,filname in os.walk(path):
            foldername=os.path.join(path,foldername);
            for file in filname:
                file=os.path.join(foldername,file)
                shutil.copy(file,folder);
    else:
        print("Invalid path ")
def main():
    print("-----------Marvellous infosystems-------------")
    print("\n Application name:",sys.argv[0])
            
    if len(sys.argv)==1:        
        print("Error :invalid number of arguments")
        exit()
    if(len(sys.argv)<=2):
        if(sys.argv[1]=='-h') or(sys.argv[1]=='-H'):
            print("This Script Copy all files from first directory into second directory")
            exit()
        if(sys.argv[1]=='-u') or (sys.argv[1]=='-U'):
            print("Usage : DirectoryFileSearch.py “Demo” “temp")
            exit()
        else:
            print("Error :invalid number of arguments")
            exit()
    
    try:
        Display(sys.argv[1],sys.argv[2])
    except ValueError:
        print("Error : Invvalied datatype of input ")
    except Exception:
        print("Error : Invalid input ")
    finally:
        print("Thank You  !!!!!")


if __name__=="__main__":
    main()