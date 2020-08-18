#!/usr/bin/bash
# GET BODY RESPONSE
RES=$(curl -s -L -w "%{redirect_url}\n" $1)
printf "$RES"
