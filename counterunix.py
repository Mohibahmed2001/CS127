#Mohib Ahmed
#July 5th 2023
#write a script that counts the number of .py files in current working directory.
count=$(ls -1 *.py 2>/dev/null | wc -l)
echo "Number of .py files: $count"
