class CalcUtils:
    @staticmethod
    def calculateAverage(*args):
        return sum(args) / len(args)

    @staticmethod
    def filterPositives(lst: list):
        return [i for i in lst if i > 0]

    @staticmethod
    def percent(number, percent):
        return round(number * percent / 100, 2)


print(CalcUtils.calculateAverage(10, 20, 5, 4))
my_list = [11, -21, 0, 45, 66, -93]
print(CalcUtils.filterPositives(my_list))
print(CalcUtils.percent(94.8, 19))
