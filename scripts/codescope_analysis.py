import subprocess
import json
import re

def run_codescope(target_dir):
    result = subprocess.run(['codescope', target_dir, '--inspection', '--output-filepath', 'codescope_output.json'], capture_output=True, text=True)
    print(result.stdout)

    with open('codescope_output.json', 'r') as f:
        codescope_output = f.read()

    # Process markdown to extract relevant data
    project_structure = re.search(r'Project Structure:\n(.+?)\n---', codescope_output, re.DOTALL)
    functions_classes = re.search(r'Key Functions and Classes:\n(.+?)\n---', codescope_output, re.DOTALL)

    return {
        'project_structure': project_structure.group(1).strip() if project_structure else '',
        'functions_classes': functions_classes.group(1).strip() if functions_classes else ''
    }