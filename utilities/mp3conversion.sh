#!/bin/bash

for f in *.flac; do ffmpeg -i "$f" -q:a 2 "${f%.flac}.mp3"; done
FOLDER_NAME=$(basename "$PWD")
mkdir ./"{$FOLDER_NAME}_mp3"
mv *.mp3 ./"{$FOLDER_NAME}_mp3"
cp *.jpg ./"{$FOLDER_NAME}_mp3"
mv ./"{$FOLDER_NAME}_mp3" ~/Music/TempConverted/"{$FOLDER_NAME}_mp3"
