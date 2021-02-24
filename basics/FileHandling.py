import os
#allows user to handle files i.e, to read and write files along with many other operations.
#open(): allows open the file,takes two parameter(fileName, mode(default "rt")).
# 4 different modes for opening a file.
# "r": read a file
# "a": append items to file, if doesn't exists it will create.
# "w": write into file,create if doesn't exist.
# "x": create new file, return error if file already exist.

# 2 Additional modes.
#1 "t": for txt files,Text mode. by default.
#2 "b": for binary, Binary Mode (e.g image)


#Reading data from file.

file_ = open("demo.txt","at");


# a: Appending data to the list.
#file_.write(" good. Thanks for asking ");
#file_.close();
file_read = open("demo.txt","r");
print(file_read.read());

# r: read(n) # n: no of characters.
#print(read_file.read(5));

#readline(): return one line of the file.
print(file_read.readline());

# w: overwrite the entire file again, also create file if doesn't exist.
file_write = open("demo.txt","w")
file_write.write("Sorry previous content removed!!")
file_write.close();
print(file_read.read());

file_write1 = open("write_mode.txt","w");
file_write1.write("writing some content..");
file_write1.close();

file_read1 = open("write_mode.txt", "r");
print(file_read1.read());

#Removing files.
# os.path.exists() and os.remove() : check and remove file if exist in directory.
os.remove("write_mode.txt") if os.path.exists("write_mode.txt") else print("file doesn't exist");
  
#os.rmdir(dir_name) : delete only empty folders.  
if os.path.exists("abc"):
  os.rmdir("abc")
else:
  print("dir. Not Exist!!!!")

