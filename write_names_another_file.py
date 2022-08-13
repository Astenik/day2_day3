'''this projec reads all names from the file.txt file and write them in another file 
changed all first letters of names uppercasees.'''
my_file = open('file.txt', 'r')
my_file = my_file.read()
nums = my_file.split()
new_file = open('file2', 'w')
new_file = new_file.write(my_file.title())
