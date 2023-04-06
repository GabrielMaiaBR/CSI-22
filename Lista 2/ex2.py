def tuple_means(tuples):

    means = []

    for tup in tuples:
        avg = sum(tup) / len(tup)
        means.append(avg)

    return tuple(means)