from Logger import Logger
class Tester:
    def __init__(self, verbose=False):
        self.logger = Logger()
        self.verbose = verbose
    
    def run_step(input, expected_output, function):
        pass