#!/bin/bash
# Check content length
curl -o /dev/null -s -w "%{http_code}\n" $1
