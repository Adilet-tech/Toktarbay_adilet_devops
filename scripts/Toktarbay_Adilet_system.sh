#!/bin/bash

echo "=============================="
echo "Student Information"
echo "=============================="
echo "Name: Adilet"
echo "Surname: Toktarbay"
echo "Group: IT2-2306"
echo "Student ID: 37629"
echo "=============================="
echo "System Information"
echo "=============================="

echo "Username:$(whoami)"

echo "Hostname:$(hostname)"

echo "Current Date:$(date)"

echo "Operating System:$(uname -s)"

echo "Disk Usage:"
df -h /
echo "Memory Usage:"
free -h

if [ -f "Toktarbay_Adilet_info.txt" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi 
