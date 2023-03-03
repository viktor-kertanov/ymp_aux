
def print_squares(nums):
    for idx, num in enumerate(range(1, nums+1), start=1):
        print(f"{idx}. {num}^2={num**2}\n")


def two_plus_two():
    return 2+2


def exp_func(i, num):
    for el in range(i):
        print(f"{num}^{el} = {num**el}")


if __name__ == '__main__':
    exp_func(5, 7)
    print('Hello world')
