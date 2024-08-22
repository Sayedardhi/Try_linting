
'''

 """

            if front_filename == back_filename:
                return f'{front_filename}'

            # Check if it is an empty file
            if os.stat(back_filename).st_size == 0:
                return None

            with open(front_filename, 'r') as f_fr:
                code = f_fr.readlines()
            with open(back_filename, 'r') as f_bk:
                expected_code = f_bk.readlines()

            # check if the files are exactly same
            if code == expected_code:
                return None

            corrected_code = []
            rationale = ""
            # check if the files are different and needs to be fixed
            for i, line in enumerate(expected_code):
                if "DO NOT MODIFY" in line or "FIX ME" in line or "INSERT ORIGINAL CODE HERE" in line:
                    # get the index of start
                    begin = line.find("DO NOT MODIFY")
                    end = line.find("FIX ME")
                    if begin == -1 and end != -1:
                        begin = line.find("INSERT ORIGINAL CODE HERE")

                    rationale = f'```\n{line}\n```'
                    if begin == -1 or (begin + 20) < len(line):
                        corrected_code.append(line[:begin])
                        corrected_code.append("")
                        corrected_code.append("DO NOT MODIFY")
                        corrected_code.append("")
                        corrected_code.append("FIX ME")
                    else:
                        corrected_code.append(line[:begin] + line[begin:])

                    # get the index of end and add it to rationale
                    for j in range(i, i+2):
                        if len(code) > j:
                            corrected_code.append(f"{j}: {code[j]}")
                else:
                    corrected_code.append(line)

            return '\n'.join(corrected_code) + f'\n\n{rationale}'

        # If the files are exactly same, just return the correct filename
        if front_filename == back_filename:
            return f'{front_filename}'
        
        response = await self._send_message(ctx, 'Please provide the path to the front file and the path to the back file')
        path_to_front = response.content

        response = await self._send_message(ctx, 'Please provide the path to the expected file')
        path_to_back = response.content
        
        # Get the pylint report from the file
        response = await self._send_message(ctx, f'Running pylint on {path_to_front}')
        report = await self.pylint(path_to_front)

        # If it is not a valid report, then just return None
        if not report:
            return None
        
        # Check if the expected code and the actual code are same or needs to be corrected
        if not check_files(path_to_front, path_to_back, report):
            return f'```\n{report}\n```'

        return None

    @commands.command()
    async def update_pylint_rules(self, ctx):
        """Update the pylint rules to their current version."""
        response = await self._send_message(ctx, 'Updating the pylint rules')
        report = subprocess.run('pylint --load-plugins=pylint_django', shell=True)

        # If it is not a valid report, then just return None
        if report.returncode != 0:
            return None
        
        await self._send_message(ctx, 'Updated the pylint rules')

    @commands.command()
    async def check_format(self, ctx):
        """Check whether there is any formatting errors in the code."""
        response = await self._send_message(ctx, 'Checking format of the files...')
        report = subprocess.run('black .', shell=True)

        # If it is not a valid report, then just return None
        if report.returncode != 0:
            return None
        
        await self._send_message(ctx, 'Checked successfully')
    
    @commands.command()
    async def update_format_rules(self, ctx):
        """Update the format rules to their current version."""
        response = await self._send_message(ctx, 'Updating formatting rules')
        report = subprocess.run('black --check .', shell=True)

        # If it is not a valid report, then just return None
        if report.returncode != 0:
            return None
        
        await self._send_message(ctx, 'Updated the formatting rules')

    @commands.command()
    async def update_all(self, ctx):
        """Update all of the above."""
        response = await self._send_message(ctx, 'Updating the pylint rules...')
        report = subprocess.run('pylint --load-plugins=pylint_django', shell=True)

        # If it is not a valid report, then just return None
        if report.returncode != 0:
            return None
        
        response = await self._send_message(ctx, 'Updating formatting rules...')
        report = subprocess.run('black --check .', shell=True)

        # If it is not a valid report, then just return None
        if report.returncode != 0:
            return None
        
        await self._send_message(ctx, 'Updated all the files')

    @commands.command()
    async def check_test(self, ctx):
        """Check whether there is any test related errors in the code."""
        response = await self._send_message(ctx, 'Checking test files...')

        # Check the test cases of the front and back end
        for file_name in os.listdir('backend/tests/'):
            if file_name != '__init__.py' and '.test' not in file_name:
                subprocess.run(f'pytest backend/tests/{file_name}', shell=True)

        # Check the test cases of the front end
        for file_name in os.listdir('frontend/tests/'):
            if file_name != '__init__.py' and '.test' not in file_name:
                subprocess.run(f'pytest frontend/tests/{file_name}', shell=True)

        # If it is not a valid report, then just return None
        response = await self._send_message(ctx, 'Checked successfully')

    @commands.command()
    async def update_test(self, ctx):
        """Update the test files to their current version."""
        response = await self._send_message(ctx, 'Updating test files...')

        # Check the test cases of the front and back end
        for file_name in os.listdir('backend/tests/'):
            if file_name != '__init__.py' and '.test' not in file_name:
                subprocess.run(f'pytest backend/tests/{file_name}', shell=True)

        # Check the test cases of the front end
        for file_name in os.listdir('frontend/tests/'):
            if file_name != '__init__.py' and '.test' not in file_name:
                subprocess.run(f'pytest frontend/tests/{file_name}', shell=True)

        # If it is not a valid report, then just return None
        response = await self._send_message(ctx, 'Updated successfully')

    @commands.command()
    async def update_all_test(self, ctx):
        """Update all of the above."""
        response = await self._send_message(ctx, 'Updating test files...')

        # Check the test cases of the front and back on of 10000000',
if __name__ == '__' == '__ '__ '__ '__ '__ '__ '__':
    print('You have to run this script with the root user (sudo or sudo)')')')')')')')')')')')')')')')')')')')')')')')')')')')')')')')')
