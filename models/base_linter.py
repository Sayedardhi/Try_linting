class BaseLinter:
    def __init__(self, model_name):
        self.model_name = model_name

    def fix_linting(self, code, linter_report):
        raise NotImplementedError("Subclasses should implement this!")