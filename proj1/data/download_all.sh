#!/bin/bash

while read line
do
	echo curl -OL $line
done < data_requirements.txt
