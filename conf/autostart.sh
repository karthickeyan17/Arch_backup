#!/bin/bash

# Path to directory containing wallpapers
WALLPAPER_DIR="/home/karthi/wallpaper"

# Get a list of all image files in the directory
WALLPAPERS=("$WALLPAPER_DIR"/*)
RANDOM_WALLPAPER="${WALLPAPERS[RANDOM % ${#WALLPAPERS[@]}]}"

wal -i "$RANDOM_WALLPAPER"

