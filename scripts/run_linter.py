import os
import json
import subprocess
import argparse

def run_pylint(target_dir):
    print(f"Running pylint on {target_dir}")
    pylint_output = {}
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                result = subprocess.run(['pylint', file_path, '--output-format=json'], capture_output=True, text=True)
                pylint_output[file_path] = json.loads(result.stdout)
    
    # Pretty-print the JSON output
    formatted_output = json.dumps(pylint_output, indent=4)
    
    with open('output/pylint_output.json', 'w') as f:
        f.write(formatted_output)
    
    print(f"Pylint output saved to output/pylint_output.json")

def clone_repo(repo_url, clone_dir):
    print(f"Cloning repository from {repo_url} into {clone_dir}")
    subprocess.run(['git', 'clone', repo_url, clone_dir])

def run_linter(file_path):
    result = subprocess.run(['pylint', file_path, '--output-format=json'], capture_output=True, text=True)
    pylint_output = json.loads(result.stdout)
    return pylint_output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Pylint on a GitHub repo")
    parser.add_argument('repo_url', help="URL of the GitHub repo to clone and lint")
    args = parser.parse_args()
    
    clone_dir = 'cloned_repo'
    if os.path.exists(clone_dir):
        subprocess.run(['rm', '-rf', clone_dir])
    
    clone_repo(args.repo_url, clone_dir)
    
    target_dir = clone_dir
    os.makedirs('output', exist_ok=True)
    run_pylint(target_dir)
