class ErrorCalculator:
    @staticmethod
    def relative_error(new_value, old_value):
        if old_value is None:
            return 0
        if new_value != 0:
            return abs((new_value - old_value) / new_value) * 100
        return 0