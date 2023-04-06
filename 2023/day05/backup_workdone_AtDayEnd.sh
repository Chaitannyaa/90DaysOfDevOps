#!/bin/bash

BACKUP_FILENAME="backup_$(date +%Y-%m-%d).tar.gz"

# Create backup archive
tar czf "$BACKUP_FILENAME" /home/krishiva/90DaysOfDevOps/2023/day05

if [ $? -eq 0 ]; then
  echo "Backup successful!"
else
  echo "Backup failed."
fi

