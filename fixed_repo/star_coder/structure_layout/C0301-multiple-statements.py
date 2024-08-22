

            """
            return do_front(code)

        def handle_post(self):
            """
            This function handles when the user posts the edited version of a code to the slack channel. The post content will be sent as the arguments for this function, and it should return the corrected code as a string.
            You can see an example of how you would parse this input from the request body in: https://api.slack.com/slash-commands?redirect_to=%2Fapps%2Fmanage_app

            Args:
                self (PostHandler): The object instance for the PostHandler class
            """
            return do_back(self.args)

        def handle_message(self):
            """
            This function handles when a message is posted to a slack channel with a slash command in it. It will be sent as the arguments for this function, and should return the corrected code as a string.
            You can see an example of how you would parse this input from the request body in: https://api.slack.com/slash-commands?redirect_to=%2Fapps%2Fmanage_app

            Args:
                self (MessageHandler): The object instance for the MessageHandler class
            """
            return do_back(self.args)

          """
```

And we're done!
