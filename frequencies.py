def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        item = str(item)
        if item not in frequencies:
            frequencies[item] = 1
        else:
            frequencies[item] += 1
    print(frequencies)
    return frequencies
