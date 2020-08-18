#!/usr/bin/env bash
# GET THE BYTES SIZE OF A RESPONSE
curl $1 -s -w '%{size_download}' -o tmpfile
BYTES=$(cat tmpfile | tr -d -c 0-9)
echo "$BYTES"
rm -rf tmpfile
