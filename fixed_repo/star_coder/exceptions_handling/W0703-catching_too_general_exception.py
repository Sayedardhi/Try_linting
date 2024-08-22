 """
            self.logger.info(f"Starting fixer for file {self.filename}")

            with open(self.filename) as file:
                lines = file.readlines()
            
            # Parse and check for valid syntax before we can start linting. If there is an error, stop the linter and exit immediately.
            self.parse_and_check(lines)

            # Add a docstring to each function in the code. This is not strictly necessary for pylint but it helps with debugging.
            if self.docstring_missing:
                lines = add_docstrings(lines)
            
            # Remove unnecessarily indented blocks of code
            lines = remove_unindented_blocks(lines)

            # Add comments to explain why the code is indented so that we know what the user should expect when reading it. This is not strictly necessary for pylint but it helps with debugging.
            if self.docstring_missing:
                lines = add_comments(lines)
            
            # Lint the code and fix all the errors
            corrected, report = pylint_fixer(self.filename, lines)

            # Remove comments to explain why the code is indented so that we know what the user should expect when reading it. This is not strictly necessary for pylint but it helps with debugging.
            if self.docstring_missing:
                lines = remove_comments(lines)
            
            # Remove unnecessarily indented blocks of code
            lines = remove_unindented_blocks(lines)

            # Add a docstring to each function in the code. This is not strictly necessary for pylint but it helps with debugging.
            if self.docstring_missing:
                lines = add_docstrings(lines)

            response = ""
            for line in corrected:
                response += f"{line}\n"
            
            response += "\n" + report
            
            return response

"""


from ast import parse
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Tuple
import subprocess
import sys

class PylintResult(NamedTuple):
    code: str
    report_path: Path

    def __str__(self) -> str:
        return self.code


def do_front(front_filename: Path, back_filename: Path) -> None:
    if front_filename == back_filename:
        print("Original and corrected code are the same file, so can't fix it")

    with open(back_filename, "r") as f:
        corrected = f.read()

    try:
        report = subprocess.check_output(
            ["pylint", "--disable=all", back_filename], stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError:
        print("Linter failed to run on the code. Will not fix")
        return

    original_code = get_original_code(back_filename)

    report_path = Path(sys.argv[0]).parent / Path(front_filename).with_suffix(".report")
    with open(report_path, "w") as f:
        f.write(str(report))

    # Parse the pylint report and get the rationale for each fix
    original_to_fix = get_original_to_fixed()
    fixes = get_fixes(report_path)
    corrected_lines = add_line_corrections(corrected, original_code, original_to_fix, fixes)

    with open(front_filename, "w") as f:
        f.write(corrected_lines)

def get_original_to_fixed() -> Dict[Tuple[str], str]:
    """Get a dictionary of the original code to what it is fixed for"""
    original_to_fix = {}

    with open("original_code.txt", "r") as f:
        for line in f:
            if not line.startswith("#"):
                parts = line.split()
                # For each original, get a list of fixes that were made to it
                fix_parts = parts[-1].replace('"', "").split(",")
                # Store the original code and the fix to that specific original code as a key-value pair
                original_to_fix[tuple(parts[:-1])] = " ".join(fix_parts)

    return original_to_fix

def get_fixes(report_path: Path) -> List[str]:
    """Parse the pylint report for all of the fixes made to each function"""
    # A map of lines to the number of times they were changed by the linter. So if a line is changed 3 times, then it'll be 4 in this dict
    original_to_fix = {}

    with open(report_path, "r") as f:
        for line in f:
            if line.startswith("************ Module ") or not line.startswith("-"):
                continue

            # Parse the report line and get the function name and line number of the fix
            parts = line.split()
            function_name = parts[1]
            line_number = int(parts[-4])

            # Get the original code to that specific line number
            original_code = original_to_fix[(function_name, line_number)]

            # Parse the report line and get the fix message
            message = " ".join(parts[-2:])

            if len(original_code) > 0:
                original_code += f" - {message}"
            else:
                original_code = message

    return [original_code]

def add_line_corrections(
    corrected: str, 
    original_code: str, 
    original_to_fix: Dict[Tuple[str], str], 
    fixes: List[str]
) -> str:
    """Add the original code to each line in the corrected code"""
    lines = []

    for i, line in enumerate(corrected.splitlines()):
        if i == 0 and len(original_code) > 0:
            lines.append("# Original Code" + "\n")
            lines.append("###############\n")
            lines.append("# " + original_code + "\n")
            lines.append("###############\n")

        line = line.replace("\t", " ")
        if line == "# Original Code":
            pass
        elif len(line) > 0 and line[0] != "#":
            # Get the fix for this line number, if there is one
            fixed_line = original_to_fix[(original_code[:3], i+1)]

            if len(fixed_line) > 0:
                lines.append(fixed_line + "\n")

        lines.append(line + "\n")

    return "".join(lines)

def get_original_code(filename: Path) -> str:
    """Get the original code for a specific file"""
    with open("original_code.txt", "r") as f:
        lines = []
        for line in f:
            if not line.startswith("#"):
                parts = line.split()
                # For each original, get a list of fixes that were made to it
                fix_parts = parts[-1].replace('"', "").split(",")
                # Store the original code and the fix to that specific original code as a key-value pair
                if tuple(parts[:-1]) == (filename.stem, str(i+1)):
                    original_code = " ".join(fix_parts)

    return original_code

def main() -> None:
    """Run this script"""
    # Get the arguments
    front_filename = Path("front.py")
    back_filename = Path(sys.argv[1])

    do_front(front_filename, back_filename)


if __name__ == "__main__":
    main()
