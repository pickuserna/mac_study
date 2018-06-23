#!/bin/bash
backup_dir="/opt/mrepo/"
if [ ! -d backup_dir ]
then
	mkdir -p $backup_dir
fi
