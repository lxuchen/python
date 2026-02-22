# def count_up_to(n):
#     count = []
#     for i in range(1, n + 1):
#         count.append(i)
#     return count


def count_up_to(n):
    for number in range(1, n + 1):
        yield number


print(count_up_to(5))
