from exceptions.Exception import Exception


class ExpectedCharException(Exception):

    def __init__(self, pos_start, pos_end, details=''):
        super().__init__(pos_start, pos_end, 'Expected Character', details)