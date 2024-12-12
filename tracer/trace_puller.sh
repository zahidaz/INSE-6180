#!/bin/bash

# Accept a package name as argument and an optional flag for extraction

pkg=$1
where_to_pull=$2
# Exit immediately if any command exits with a non-zero status
set -e

# Define the file directory path
file_dir="/sdcard/Android/data/$pkg/files"
out_file="/data/local/tmp/trace_$pkg.tar.gz"

# Compress the directory on the device
adb shell "su 0 sh -c 'tar -czf $out_file $file_dir'"

# Adjust permissions and ownership of the archive
adb shell "su 0 sh -c 'chmod 777 $out_file'"
adb shell "su 0 sh -c 'chown shell:shell $out_file'"

# Pull the archive to the local machine and remove it from the device
adb pull $out_file $where_to_pull/trace_$pkg.tar.gz
# remove the archive from the device
adb shell "su 0 sh -c 'rm $out_file'"

echo "Done"

