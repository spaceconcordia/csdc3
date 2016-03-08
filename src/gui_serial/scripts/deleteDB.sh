#!/bin/bash
# file: deleteDB.sh

copies=( copy1 copy2 copy3 )
for i in "${copies[@]}"
do
    rm /root/csdc3/src/logs/data_logs/$i/*
    rm /root/csdc3/src/logs/system_logs/$i/*
done
