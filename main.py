# import os
# import json
# import subprocess
# import argparse
# from scripts.codescope_analysis import run_codescope
# from scripts.run_linter import run_linter
# from scripts.apply_fixes import apply_fixes

# def main(file_path=None):
#     repo_url = 'https://github.com/Sayedardhi/test-linting.git'
#     clone_dir = 'cloned_repo'

#     if os.path.exists(clone_dir):
#         subprocess.run(['rm', '-rf', clone_dir])

#     clone_repo(repo_url, clone_dir)
    
#     codescope_output = run_codescope(clone_dir)
#     print(f"CodeScope output: {codescope_output}")

#     if file_path:
#         files_to_process = [os.path.join(clone_dir, file_path)]
#     else:
#         files_to_process = [os.path.join(clone_dir, f) for f in os.listdir(clone_dir) if f.endswith('.py')]

#     for file in files_to_process:
#         lint_output = run_linter(file)
#         lint_output_json = json.dumps(lint_output)
#         print(f"Lint output for {file}: {lint_output_json}")

#         apply_fixes(file, lint_output_json, codescope_output)

# def clone_repo(repo_url, clone_dir):
#     print(f"Cloning repository from {repo_url} into {clone_dir}")
#     subprocess.run(['git', 'clone', repo_url, clone_dir])

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Run Linter on a specific file in a GitHub repo")
#     parser.add_argument('--file', help="File to lint and fix", required=False)
#     args = parser.parse_args()
#     main(args.file)

import os
import json
import subprocess
import argparse
from scripts.codescope_analysis import run_codescope
from scripts.run_linter import run_linter
from scripts.apply_fixes import apply_fixes

def main(file_path=None, model_name='llama3', generate_diff_only=False):
    repo_url = 'https://github.com/Sayedardhi/violations'
    clone_dir = 'cloned_repo'

    if os.path.exists(clone_dir):
        subprocess.run(['rm', '-rf', clone_dir])

    clone_repo(repo_url, clone_dir)
    
    codescope_output = run_codescope(clone_dir)
    print(f"CodeScope output: {codescope_output}")

    if file_path:
        files_to_process = [os.path.join(clone_dir, file_path)]
    else:
        # Modified to recursively find all Python files
        files_to_process = []
        for root, dirs, files in os.walk(clone_dir):
            for file in files:
                if file.endswith('.py'):
                    files_to_process.append(os.path.join(root, file))

    for file in files_to_process:
        lint_output = run_linter(file)
        lint_output_json = json.dumps(lint_output)
        print(f"Lint output for {file}: {lint_output_json}")

        apply_fixes(file, lint_output_json, codescope_output, model_name, generate_diff_only)

def clone_repo(repo_url, clone_dir):
    print(f"Cloning repository from {repo_url} into {clone_dir}")
    subprocess.run(['git', 'clone', repo_url, clone_dir])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Linter on a specific file in a GitHub repo")
    parser.add_argument('--file', help="File to lint and fix", required=False)
    parser.add_argument('--model', help="Model to use for linting", choices=['llama3', 'llama3_1', 'deep_seek_coder', 'star_coder', 'gemma'], default='llama3')
    parser.add_argument('--diff-only', action='store_true', help="Generate only diff JSON files without fixing the files")
    args = parser.parse_args()
    main(args.file, args.model, args.diff_only)
