#!/usr/bin/bash
# SEND DELETE REQUEST
RES=$(curl -s -XDELETE $1)
echo "$RES"
