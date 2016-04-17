#!/bin/bash

ACTIVATE=env/bin/activate
DEACTIVATE=deactivate
PYTHON=/usr/bin/python
CONTROLLER_PATH=./controller.py

source $ACTIVATE

$PYTHON $CONTROLLER_PATH 2>./log/controller.log

$DEACTIVATE
