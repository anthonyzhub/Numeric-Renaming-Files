#! /bin/bash

# Get parameter
DIR=$1

# Ask for name name and starting value
read -p "New name: " NEW_NAME
read -p "Start value: " VALUE

rename_all_files()
{
    # OBJECTIVE: Rename all files in directory

    # Iterate all files inside of directory
    for FILE in "$DIR"/*
    do
        # Change name
        mv $FILE ${NEW_NAME/"#"/$VALUE}

        # Increment value
        ((VALUE++))
    done
}

rename_some_files()
{
    # OBJECTIVE: Rename files specified in parameter

    ARR=($@)

    # Iterate files
    for FILE in "${ARR[@]}"
    do
        # Replace name
        mv $FILE ${NEW_NAME/"#"/$VALUE}

        # Increment value
        ((VALUE++))
    done
}

# Check if directory exists
if [ $DIR == "." ]
then

    # Get current working directory
    DIR=${DIR/"."/$PWD}

elif [ $DIR == "~" ]
then

    # Get home directory
    DIR=${DIR/"~"/$HOME}

fi

# If directory was only specified and exist, send it to rename_all_files()
if [ -d $DIR ]
then
    rename_all_files
else
    rename_some_files "$@"
fi

echo "Done!"