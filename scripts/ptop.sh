#!/bin/bash

top -c -p $(pgrep -d',' -f $1)
