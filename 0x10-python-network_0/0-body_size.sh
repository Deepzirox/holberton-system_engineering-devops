#!/bin/bash
# GET THE BYTES SIZE OF A RESPONSES
curl "$1" -s -w '%{size_download}' | tr -d -c 0-9 && echo ""
