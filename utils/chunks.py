def chunks(data, chunk):
    for i in range(0, len(data), chunk):
        yield data[i:i + chunk]


def grouped(iterable, chunk):
    return zip(*[iter(iterable)] * chunk)
