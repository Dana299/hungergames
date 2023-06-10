#!/bin/bash

echo "_____Waiting for container with httbin to be running on localhost 80_____"

docker run -p 80:80 -d kennethreitz/httpbin

while ! nc -z localhost 80; do
  sleep 0.1
done

echo "Httpbin launched on port 80"

echo "_____Installing dependencies_____"

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "_____Running main.py_____"

python3 main.py