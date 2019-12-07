'''Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extenntion.
Usage : DirectoryRename.py “Demo” “.txt” “.doc”'''
import sys
import os
from fileinput import filename
def Display(path,ext1,ext2):
    flag = os.path.isabs(path)
    if flag ==False:
        path=os.path.abspath(path)
        
    exists = os.path.isdir(path)
    if exists :
        for foldername,subfolder,filname in os.walk(path):
            for filen in filname:
                filen=os.path.join(foldername,filen)
                f,exten = os.path.splitext(filen)
                if(exten==ext1):
                    print("File name: "+filen)
                    new=f+ext2
                    print(new)
                    
                    os.rename(filen,new)
                    print("----------------------")
                    print("")
    else:
        print("Invalid path ")
def main():
    print("-----------Marvellous infosystems-------------")
    print("\n Application name:",sys.argv[0])
    
    if len(sys.argv)==1:
        print("Error :invalid number of arguments")
        exit()
    if(len(sys.argv)<=3):
        if(sys.argv[1]=='-h') or(sys.argv[1]=='-H'):
            print("This script which accept directory name and two file extensions from user.\
                    Rename all files with first file extension with the second file extenntion.")
            exit()
        if(sys.argv[1]=='-u') or (sys.argv[1]=='-U'):
            print("Usage : DirectoryFileSearch.py “Demo” “.txt” “.doc” ")
            exit()
        else:
            print("Error :invalid number of arguments")
            exit()
            
    
    try:
        Display(sys.argv[1],sys.argv[2],sys.argv[3])
    except ValueError:
        print("Error : Invalied datatype of input ")
    except Exception:
        print("Error : Invalid input ")
    finally:
        print("Thank You  !!!!!")


if __name__=="__main__":
    main()