'''Design automation script which accept directory name and file extension from user. Display all
files with that extension.
Usage : DirectoryFileSearch.py “Demo” “.txt”
Demo is name of directory and .txt is the extension that we want to search.'''
import sys
import os
def Display(path,ext):
    flag = os.path.isabs(path)
    if flag ==False:
        path=os.path.abspath(path)
        
    exists = os.path.isdir(path)
    
    if exists :
        for foldername,subfolder,filname in os.walk(path):
            for filen in filname:
                f,exten = os.path.splitext(filen)
                if(exten==ext):
                    print("File name: "+f)
                    print("----------------------")
            print("")
    else:
        print("Invalid path ")
def main():
    print("-----------Marvellous infosystems-------------")
    print("\n Application name:",sys.argv[0])
    
    if(len(sys.argv)==1):
        print("Error :invalid number of arguments")
        exit()
    if(len(sys.argv)<=2):
        if(sys.argv[1]=='-h') or(sys.argv[1]=='-H'):
            print("This Script is used to in directory Display all files with that extension")
            exit()
        if(sys.argv[1]=='-u') or (sys.argv[1]=='-U'):
            print("Usage : DirectoryFileSearch.py “Demo” “.txt”\
              Demo is name of directory and .txt is the extension that we want to search")
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