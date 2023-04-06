#!/bin/bash

if [ $# != 3 ]
then 
	echo -e "Can't proceed! \n Please give three arguments to continue."
	exit 1
fi
echo "Creating directories according to your requirement:"

for (( i=$2; i<=$3; i++ ))
do
	mkdir $1$i
done

echo "Tada! Here are your directories:"

ls 
