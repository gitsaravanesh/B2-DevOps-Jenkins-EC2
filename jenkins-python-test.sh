#!/bin/bash

# Execute the Python program and store the output in a variable
output=$(python3 app.py 5 10 add)

# Remove newlines from the output, if any
output=$(echo $output | tr -d '\n')

# Verify if the output is correct
if [ "$output" == "Result: 15.0" ]; then
  echo "Addition Test Passed"
else
  echo "Addition Test Failed"
  exit 1
fi
