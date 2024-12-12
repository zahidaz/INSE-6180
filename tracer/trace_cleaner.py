import os
import sys
import re
import argparse
import logging
from pathlib import Path

def clean_trace(trace_dir, output_file):
    with open(output_file, 'w') as out_file:
        for trace_file in os.listdir(trace_dir):
            if not trace_file.endswith('.trace'):
                continue
            trace_file_path = os.path.join(trace_dir, trace_file)
            with open(trace_file_path, 'rb') as in_file:
                flat_method_section_reached = False
                for line in in_file:
                    try:
                        line = line.decode('utf-8')
                    except UnicodeDecodeError:
                        break
                    if line.startswith('*end'):
                        break
                    if not flat_method_section_reached:
                        if line.startswith('*method'):
                            flat_method_section_reached = True
                        continue
                    if line.startswith('0x'):
                        line = line.split(maxsplit=1)[1]
                    line = re.sub(r'\s+', ' ', line)

                    out_file.write(line)





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Trace Cleaner')
    parser.add_argument('trace_dir', type=str, help='Directory containing trace files')
    parser.add_argument('output_file', type=str, help='Output file')
                    # regex for 0x1234abcd followed by space
    args = parser.parse_args()

    trace_dir = Path(args.trace_dir)
    output_file = Path(args.output_file)
    clean_trace(trace_dir, output_file)

