import os
import shutil

def renameDir(src_folder, dest_folder = None, renameFunction=None):
    if dest_folder is None:
        print("Please supply a destination folder, TERMINATING")
        return 1
    if renameFunction is None:
        print("You did not specify a renaming function, TERMINATING")
        return 1
    if os.path.exists(dest_folder):
        pass
    else:
        os.mkdir(dest_folder)
    file_list = os.listdir(src_folder)
    errors=[]
    for file in file_list:
        new_file = renameFunction(file)
        print(new_file)
        src = os.path.join(src_folder,file)
        dest = os.path.join(dest_folder,new_file)
        try:
            shutil.copy(src,dest)
        except:
            print(f"failed to copy {file}")
            errors.append(file)
    if len(errors) > 0:
        print("Writting Errors")
        with open("renameDirLog.txt","w") as f:
            [f.write(i + "\n") for i in errors]
    return 0
if __name__ == "__main__":
    pass
