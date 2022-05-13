# Lyft_SWE_Apprenticeship_2022

Welcome and thank you for reading my submission!

This repository comtains a file that performs two functions:
  1. Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
  2. Return a JSON object with the key “return_string” and a string containing every third letter from the original string

The tested inputs for the file were:
  1. curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
  2. curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "ia"}' -H 'Content-Type: application/json'

The returned outputs were:
  1. {"return_string":"muydv"}
  2. {"return_string":"error, string length less than 3"}
