import os

def showListFilesAndFolders(path):
    lst = os.listdir(path)
    for obj in lst:
        if os.path.isdir(f"{path}\\{obj}"):
            print(f"- Object {obj}, type folder")
        else:
            print(f"- Object {obj}, type file")

if __name__ == '__main__':
    path = ".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment05\\foo"
    showListFilesAndFolders(path)
    # - Object bar, type folder
    # - Object egg, type folder
    # - Object fileD.svg, type file
    # - Object fileE.tif, type file
    # - Object ham, type folder
