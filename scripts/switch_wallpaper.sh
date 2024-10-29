#!/bin/bash

IMAGEDIR=${HOME}/wallpapers

dbus_pid=$(ps aux | grep  dbus | grep -v root | grep -v message | head -1 | awk '{print $2}')
#echo $dbus_pid
session=`cat /proc/$dbus_pid/environ | grep -z DBUS_SESSION_BUS_ADDRESS | cut -d= -f2-`
#session=`grep -z DBUS_SESSION_BUS_ADDRESS /proc/${dbus_pid}/environ | cut -d= -f2-`
export DBUS_SESSION_BUS_ADDRESS=${session}

ls -C1 ${IMAGEDIR} > ~/.list.of.wallpapers.txt

wallpaper=`shuf  -n 1 ~/.list.of.wallpapers.txt`
#echo ${IMAGEDIR}/$wallpaper
gsettings set org.gnome.desktop.background picture-uri-dark file:///${IMAGEDIR}/${wallpaper}
