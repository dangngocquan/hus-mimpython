''' 
Windows

cd X
mkdir foo
cd foo
code data.txt
copy data.txt ".\\newData.txt"
copy data.txt ".\\newData_2.txt"
cd ..
mkdir bar
move ".\\foo\\newData.txt" ".\\bar"
del ".\\foo\\newData_2.txt"

'''