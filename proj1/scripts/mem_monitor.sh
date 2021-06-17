#!/bin/bash
while true
do
    ps -o rss $(pidof $1) | tail -n +2
    sleep $2
done