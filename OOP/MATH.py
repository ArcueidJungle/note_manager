class Math:
    @staticmethod
    def average(numbers):
        if not numbers:
            return 0

        try:
            return sum(numbers)/ len(numbers)
        except TypeError:
            raise ValueError('все должны быть чилсами')

print(Math.average([10, 20, 30]))  # 20.0
print(Math.average([]))            # 0

