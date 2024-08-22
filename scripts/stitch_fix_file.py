import json
import re

def parse_diff(diff):
    changes = []
    lines = diff.split('\n')
    in_hunk = False
    for line in lines:
        if line.startswith('@@'):
            in_hunk = True
            hunk_info = re.search(r'@@ -(\d+),(\d+) \+(\d+),(\d+) @@', line)
            if hunk_info:
                old_start, old_len, new_start, new_len = map(int, hunk_info.groups())
                changes.append({
                    'type': 'hunk',
                    'old_start': old_start,
                    'old_len': old_len,
                    'new_start': new_start,
                    'new_len': new_len,
                    'old_lines': [],
                    'new_lines': []
                })
        elif in_hunk:
            if line.startswith('-'):
                changes[-1]['old_lines'].append(line[1:])
            elif line.startswith('+'):
                changes[-1]['new_lines'].append(line[1:])
            elif line:
                changes[-1]['old_lines'].append(line)
                changes[-1]['new_lines'].append(line)
    return changes

def apply_changes(original_code, changes):
    original_lines = original_code.split('\n')
    fixed_lines = original_lines.copy()

    for change in changes:
        if change['type'] == 'hunk':
            old_start = change['old_start'] - 1
            old_end = old_start + change['old_len']
            new_lines = change['new_lines']
            fixed_lines[old_start:old_end] = new_lines

    return '\n'.join(fixed_lines)

def stitch_fixed_file(original_file, diff_output_file, output_file):
    with open(original_file, 'r') as f:
        original_code = f.read()

    with open(diff_output_file, 'r') as f:
        diff_output = f.read()

    # Debugging output
    print(f"Content of diff_output: {diff_output}")

    try:
        diffs = json.loads(diff_output)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    fixed_code = original_code

    for key, diff in diffs.items():
        changes = parse_diff(diff['diff'])
        fixed_code = apply_changes(fixed_code, changes)

    with open(output_file, 'w') as f:
        f.write(fixed_code)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python stitch_fixed_file.py <original_file> <diff_output_file> <output_file>")
        sys.exit(1)
    
    original_file = sys.argv[1]
    diff_output_file = sys.argv[2]
    output_file = sys.argv[3]
    
    stitch_fixed_file(original_file, diff_output_file, output_file)

