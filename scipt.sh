#!/bin/sh

CWD=$PWD
newdir=$HOME/".details.txt"
if [ -f "$newdir" ]
then
	username=$(grep -i "usr" $newdir)
	username=${username:3}
	password=$(grep -i "pwd" $newdir)
	password=${password:3}
	id=$(grep -i "id" $newdir)
	id=${id:2}
else
	read -p "Enter your canvas username: " username
	read -p "Enter your canvas password: " password
	read -p "Enter your UBC student id: " id
	echo "usr${username}\npwd${password}\nid${id}" >> $newdir
fi
read -p "Enter your assignment number: " n

echo "Turning file into zip..."
filepath=$HOME/"eclipse-workspace/COSC 111/src"
cd "$filepath"
name="A${n}"
filename="${id}_${name}"
zip -r "$filename".zip "$1"

location=$HOME/"Desktop/COSC 111 Assignments"
if [ ! -d $location ]
then
	mkdir $location
	echo "Creating a folder called COSC 111 Assignments on Desktop"
fi
mv "$filename".zip "$location" 
cd $CWD

echo "Zipped file successfully!"

python3 $CWD/upload.py ${1:1} "${location}/${filename}".zip $username $password
