def count_to(count):
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    iterator = zip(range(count), numbers_in_german)

    for _, number in iterator:
        yield number


for num in count_to(3):
    print(num)
