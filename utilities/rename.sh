#!/bin/bash

COUNTER=1
for FILE in *.mp3; do
    mv "$FILE" "$COUNTER.mp3"
    if [ $? -eq 1 ]; then
        echo "Could not rename $FILE"
    fi
    let COUNTER=COUNTER+1
done
