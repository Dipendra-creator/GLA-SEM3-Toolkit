import math


def scheduleProblem():
    transactions = int(input("Input the Number Of Transactions: "))
    sum_operations, denominator = 0, 1

    for i in range(1, transactions + 1):
        number = int(input(f"Enter No. of Operations {i}: "))
        sum_operations += number
        denominator *= math.factorial(number)

    numerator = math.factorial(sum_operations)
    total_schedule = numerator / denominator
    total_serial = math.factorial(transactions)
    total_non_serial = total_schedule - total_serial
    print(f"Schedules: {total_schedule}\n"
          f"Serial Schedules: {total_serial}\n"
          f"Non-Serial Schedules: {total_non_serial}")


scheduleProblem()
