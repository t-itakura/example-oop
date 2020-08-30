# Context
class Report():
    def __init__(self, formatter):
        self.formatter = formatter
    
    def output(self):
        print(self.formatter.create_format())

# Strategy
class Formatter:
    def create_format(self):
        pass

# Concrete Strategy html
class HTMLFormatter(Formatter):
    def create_format(self):
        return "html format"

# Concrete Strategy markdown
class MarkdownFormatter(Formatter):
    def create_format(self):
        return "markdown format"

if __name__ == '__main__':
    report = Report(HTMLFormatter())
    report.output()
