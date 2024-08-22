

    """
    # read file 
    with open(file_path) as f:
        src = f.read()
    
    # remove comments
    src = py_comments.remove_comments(src)

    # run pylint on source and get report
    linter_report = run_pylint(file_path, src)

    # check for exceptions 
    if 'Exception' in linter_report or 'except Exception as e:' in linter_report:
        return [src], linter_report
    
    # find lines to be deleted, and fix them
    # TODO: make a function to do this
    code_lines = src.split('\n')

    # find the line number of the first occurrence of "return"
    try:
        start_line = src[src.index("def") + 4 :].index('return')
        end_line = start_line + 1
    except ValueError:
        return [src], linter_report
    
    for index, code in enumerate(code_lines):
        if 'return' in code and index >= start_line and index <= end_line:
            new_line = re.search('(?<=return)\s*([a-zA-Z0-9_]*),', src).group() 
            new_code = py_comments.add_comment(src, 
                                            'This code was added by the post fixer.',
                                            index=index)
            if 'print' in new_line:
                return [new_code], linter_report
            else:
                return [py_comments.replace_text(new_code, src)], linter_report


def get_response(file_path):
    """
        This is the function where we will execute all of the post fixers and return their results
        in a single list. If an exception occurs inside any post fixer then it should be handled by this method. 
        The code here is inspired by stack overflow: https://stackoverflow.com/questions/4065728/how-to-catch-exception-inside-try-except
    """

    try:
        with open(file_path) as f:


        # remove comments
        src = py_comments.remove_comments(src)

        # run pylint on source and get report
        linter_report = run_pylint(file_path, src)
        
        # check for exceptions 
        if 'Exception' in linter_report or 'except Exception as e:' in linter_report:
            return [src], linter_report
        
        # find lines to be deleted, and fix them
        # TODO: make a function to do this
        code_lines = src.split('\n')

        # get the number of post-fixers that have been implemented
        # we will use this to know whether or not we should return results as a list
        num_post_fixers = len(POST_FIXERS)
 """
        return ""

    @staticmethod
    def get_linter() -> Linter:
        return LinterPylintFixerLinter()
        # find the line number of the first occurrence of "return"
        try:
            start_line = src[src.index("def") + 4 :].index('return')
            end_line = start_line + 1
        except ValueError:
            return [src], linter_report

        for index, code in enumerate(code_lines):
            # if the post-fixer has not been implemented then just return the source
            if index >= start_line and index <= end_line:
                continue

            try:
                # execute post fixers and get results
                post_fixer = POST_FIXERS[index]

                fixed_src, linter_report = post_fixer(file_path, src, code)
                
                # check for exceptions 
                if 'Exception' in linter_report or 'except Exception as e:' in linter_report:
                    return [src], linter_report
                else:
                    return fixed_src, linter_report

            except KeyError:
                # if the post-fixer has not been implemented then just return the source
                return [src], linter_report
            finally:
                if num_post_fixers == 1:
                    continue

                # decrement the number of post-fixers left to run
                num_post_fixers -= 1

    except FileNotFoundError as e:
        raise ValueError(f"File {file_path} not found!")
        raise e


def generate_response(file_paths):
    """
        This is a utility function that takes in a list of file paths and returns the response for each 
        file. If any exception occurs then it should be handled by this method. 
    """
    # execute all post-fixers on all files
    responses = [get_response(f) for f in tqdm(file_paths)]

    # flatten all responses
    flat_responses = [item for sublist in responses for item in sublist]

    return flat_responses


def main():
    parser = argparse.ArgumentParser(description="This is a utility that can be used to lint source files and execute post-fixers on them.")

    parser.add_argument("-f", "--file-path", nargs='+', help="Provide the paths for the file or files you want to lint. This argument will only work if all of the file paths are in the same folder as this script.")
    args = parser.parse_args()
    
    # generate responses for each source file and then return their list
    srcs, _ = generate_response(args.file_path)

    with open('fixed_sources.txt', 'w') as f:
        for src in srcs:
            f.write(src + '\n\n')


if __name__ == "__main__":
    main()
