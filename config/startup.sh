#!/usr/bin/env bash

# Kill any existing polybar instances
killall -q polybar

# Wait a bit to ensure polybar has time to stop
sleep 1

# Set wallpaper
wal -i "$(find ~/wallpaper/ -type f | shuf -n 1)" &

# Start polybar
polybar -q example -c ~/.config/polybar/config.ini &
