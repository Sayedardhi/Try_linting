# import json
# import difflib
# import os
# import re
# from models.llama3 import LLAMA3_linter

# def apply_fixes(file_path, lint_output, codescope_output):
#     lint_issues = json.loads(lint_output)
#     diffs = {}

#     for issue in lint_issues:
#         start_line = issue.get('line')
#         end_line = issue.get('endLine', start_line)
#         code_section = get_code_section(file_path, start_line, end_line)
#         if code_section:
#             diff = generate_diff(code_section, issue)
#             if diff:
#                 diffs[f"{issue['message-id']} - {issue['message']}"] = {
#                     "diff": diff,
#                     "start_line": start_line,
#                     "end_line": end_line
#                 }

#     save_diffs(file_path, diffs)
#     stitch_fixed_file(file_path, diffs)

# def get_code_section(file_path, start_line, end_line):
#     with open(file_path, 'r') as f:
#         lines = f.readlines()
#     return ''.join(lines[start_line - 1:end_line])

# def generate_diff(code_section, issue):
#     linter = LLAMA3_linter()
#     corrected_code = linter.fix_linting(code_section, issue['message'])
#     if corrected_code:
#         diff = difflib.unified_diff(code_section.splitlines(), corrected_code.splitlines(), lineterm='')
#         return '\n'.join(diff)
#     return ""

# def save_diffs(file_path, diffs):
#     output_file = f"output/fixed_code_diffs_{file_path.replace('/', '_')}_diffs.json"
#     with open(output_file, 'w') as f:
#         json.dump(diffs, f, indent=4)
#     print(f"Diffs saved to {output_file}")

# def stitch_fixed_file(file_path, diffs):
#     with open(file_path, 'r') as f:
#         original_lines = f.readlines()

#     fixed_lines = original_lines.copy()

#     for issue, diff_data in diffs.items():
#         if diff_data:
#             diff_lines = diff_data['diff'].split('\n')
#             start_line = diff_data['start_line'] - 1
#             end_line = diff_data['end_line']
#             corrected_lines = [line[1:] + '\n' for line in diff_lines if line.startswith('+') and not line.startswith('+++')]
#             fixed_lines[start_line:end_line] = corrected_lines

#     fixed_file_path = file_path.replace('cloned_repo', 'fixed_repo')
#     os.makedirs(os.path.dirname(fixed_file_path), exist_ok=True)
#     with open(fixed_file_path, 'w') as f:
#         f.writelines(fixed_lines)

#     print(f"Fixed file saved to {fixed_file_path}")
import json
import difflib
import os
import re
from models.llama3 import LLAMA3_linter
from models.ds_coder import DeepSeekCoder_linter
from models.star_coder import StarCoder_linter
from models.gemma import Gemma_linter
from models.llama3_1 import LLAMA3_1_linter

def apply_fixes(file_path, lint_output, codescope_output, model_name, generate_diff_only=False):
    lint_issues = json.loads(lint_output)
    diffs = {}
    
    model_class = {
        'llama3': LLAMA3_linter,
        'llama3_1': LLAMA3_1_linter,
        'deep_seek_coder': DeepSeekCoder_linter,
        'star_coder': StarCoder_linter,
        'gemma': Gemma_linter,
    }[model_name]

    linter = model_class()

    # Filter lint issues to include only those related to the current file
    file_lint_issues = [issue for issue in lint_issues if issue.get('path') == file_path]

    for issue in file_lint_issues:
        start_line = issue.get('line')
        end_line = issue.get('endLine', start_line)
        code_section = get_code_section(file_path, start_line, end_line)
        if code_section:
            diff = generate_diff(code_section, issue, linter)
            if diff:
                diffs[f"{issue['message-id']} - {issue['message']}"] = {
                    "diff": diff,
                    "start_line": start_line,
                    "end_line": end_line
                }

    save_diffs(file_path, diffs, model_name)

    if not generate_diff_only:
        stitch_fixed_file(file_path, diffs, model_name)

def get_code_section(file_path, start_line, end_line):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return ''.join(lines[start_line - 1:end_line])

def generate_diff(code_section, issue, linter):
    corrected_code = linter.fix_linting(code_section, issue['message'])
    if corrected_code:
        diff = difflib.unified_diff(code_section.splitlines(), corrected_code.splitlines(), lineterm='')
        return '\n'.join(diff)
    return ""

def save_diffs(file_path, diffs, model_name):
    output_dir = f"output/{model_name}"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/fixed_code_diffs_{os.path.basename(file_path).replace('.py', '')}.json"
    with open(output_file, 'w') as f:
        json.dump(diffs, f, indent=4)
    print(f"Diffs saved to {output_file}")

def stitch_fixed_file(file_path, diffs, model_name):
    with open(file_path, 'r') as f:
        original_lines = f.readlines()

    fixed_lines = original_lines.copy()

    for issue, diff_data in diffs.items():
        if diff_data:
            diff_lines = diff_data['diff'].split('\n')
            start_line = diff_data['start_line'] - 1
            end_line = diff_data['end_line']
            corrected_lines = [line[1:] + '\n' for line in diff_lines if line.startswith('+') and not line.startswith('+++')]
            fixed_lines[start_line:end_line] = corrected_lines

    fixed_file_path = file_path.replace('cloned_repo', f'fixed_repo/{model_name}')
    os.makedirs(os.path.dirname(fixed_file_path), exist_ok=True)
    with open(fixed_file_path, 'w') as f:
        f.writelines(fixed_lines)

    print(f"Fixed file saved to {fixed_file_path}")
