import os


def dotProduct(v, u):
    print(type(v), type(u))

    if (len(v) < 1 or len(u) < 1):
        print('> Usage: v and u must be a vector.')
        return 1
    elif (len(v) != len(u)):
        print('> v and u must be of the same dimension.')
        return 1

    # for range(i=0, len(v)):

    return


if __name__ == '__main__':
    dotProduct(argv[1], argv[2])
