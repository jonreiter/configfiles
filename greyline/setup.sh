#!/bin/bash

pipx install greyline
greyline init

mkdir ${HOME}/.config/greyline
cp ${HOME}/git/configfiles/greyline/config.tomp ${HOME}/.config/greyline
