#!/bin/bash

mkdir ${HOME}/.config/greyline
cp ${HOME}/git/configfiles/greyline/config.tomp ${HOME}/.config/greyline

pipx install greyline
greyline init
