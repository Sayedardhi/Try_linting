
"""

"""


    """
    Do front fix for file ``front_filename`` by fixing all the warnings present in the corresponding file ``back_filename``.
    
    This function will not overwrite any files. The original files are saved as ``<original filename>.orig``. 
    If there is a problem with reading/writing, then this function will report that and return False.

    :param str front_filename:
        Filename of the file which needs to be modified
    :param str back_filename:
        Filename for the file containing all the code to fix
    :return bool:
        True if files are successfully fixed, else false
    """
    # 1- Check if ``back_filename`` exists and is a regular file. Otherwise return False.
    # 2- If no errors detected in reading/writing original files, then do the following:
    #    - Get the file contents of back_filename as string.
    #    - Get the warnings present in that file (check if they are present at all) and save them in a list.
    #    - For each warning in list:
    #      - If no corresponding code exists for the warning, then add it to the front file and continue with next warning.
    #      - Else:
    #        - Get the function/method name from ``back_filename``.
    #        - Get the function's signature (def) by splitting on first whitespace, ignoring any space before def.
    #        - Split this signature on the left of = (if present) and right of : (if present). This will give the arguments.
    #        - For each argument in list:
    #          - If the corresponding argument is not present in function's signature, then add it to the front file and continue with next argument.
    #            This will be done only for args which are not present in both the ``back_filename`` and ``front_file``. 
    #        - Add the arguments to the function call if any. (This can be done later)
    #        - Get the function's body by splitting on first line after signature, ignoring space after def and new lines. 
    #          Ignore blank lines. 
    #        - Split this body into a list of strings. 
    #          Comment out all the comments in that body if present.
    #        - For each string in body:
    #          1- If the corresponding statement is not commented out, then add it to front file and continue with next line.
    #             This will be done only for statements which are not commented out in both ``back_filename`` and ``front_file``. 
    #          2- Else, if that particular statement is commented out:
    #             - Find the corresponding comment (the one preceding it).
    #             - Insert the line from back_filename as a replacement for the commented out code.
    #        - Add the function call to the front file.

    return True


def do_back(front_filename, back_filename):
    """
    Do back fix for file ``back_filename`` by fixing all the warnings present in the corresponding file ``front_filename``.
    
    This function will not overwrite any files. The original files are saved as ``<original filename>.orig``. 
    If there is a problem with reading/writing, then this function will report that and return False.

    :param str front_filename:
        Filename of the file which needs to be modified
    :param str back_filename:
        Filename for the file containing all the code to fix
    :return bool:
        True if files are successfully fixed, else false
    """
    
    # 1- Check if ``front_filename`` exists and is a regular file. Otherwise return False.
    # 2- If no errors detected in reading/writing original files, then do the following:
    #    - Get the file contents of front_filename as string. 
    #    - Find all function calls present in the file (in the format of <function_name>(<args>). They will be saved in a list. 
    #    - For each function call in the list:
    #      - Check if it is present in back_filename. If yes, then replace that with the corresponding code from ``front_filename``.
    
    return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="This script will fix all the pylint warnings for the front and back end of the given file.",
        epilog="""\
Example Usage:
    ./fix_pylint_file.py <filename>
        OR
    python3 ./fix_pylint_file.py <filename>""",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("file", help="The file to be fixed.")
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        raise FileNotFoundError(
            "File {} is either missing or cannot be accessed.".format(args.file)
        )

    original_filename, extension = os.path.splitext(os.path.basename(args.file))
    front_file = "{}_front{}.py".format(original_filename, extension)
    back_file = "{}_back{}.py".format(original_filename, extension)

    if not do_back(front_file, args.file):
        print(
            "Error while reading and writing back file: {}".format(
                os.path.abspath(back_file)
            )
        )
    else:
        with open(args.file, "r") as f:
            original = f.read()

        if not do_front(front_file, args.file):
            print(
                "Error while reading and writing front file: {}".format(
                    os.path.abspath(front_file)
                )
            )
        else:
            with open(back_file, "r") as f:
                back = f.read()

            diff = ""

            if original != back:
                diff += "\n\nDIFF:\n"

                # Get the lines from both the files
                lines1 = list(
                    map(lambda x: x.strip(), re.split("[^\n]+", original))
                )  # Remove blank spaces
                lines2 = list(
                    map(lambda x: x.strip(), re.split("[^\n]+", back))
                )

                diff += "Original:\n{}\n".format(original)
                diff += "Fixed:\n{}\n\n".format(back)
                diff += get_diff(lines1, lines2, "")

            with open(args.file + ".orig", "w") as f:
                f.write(original)

            if diff != "":
                print("\n\nFILE DIFF DETECTED:\n")
                print("{}\n".format(diff))


def get_diff(lines1, lines2, indent):
    """
    Get the line-by-line difference between two list of strings.
    Each element in first list will be followed by an '-' and then another newline (this function returns a string).
    The next line contains the corresponding difference.

    :param list[str] lines1:
        List of original code. 
    :param list[str] lines2:
        List of fixed code.
    :param str indent:
        Indentation to be added before each element in the outputted diff.
    :return str:
        String containing the difference between two lists of strings.
    """

    diff = ""
    for i, line1 in enumerate(lines1):
        if not lines2[i].startswith("#"):
            diff += indent + "- {}\n".format(line1)

            print print \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
