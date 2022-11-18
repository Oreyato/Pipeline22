import lucidity
from manager import conf

# v =============================================================╗
# v Parse and format functions                                   ║


def parse(path_p):
    """
    From a path, identify a template and parse data

    :return: data
    """

    data = lucidity.parse(path_p, conf.templates)
    return data[0]


def format(data_p):
    """
    Format data into a filepath, while identifying the correct template

    :return: filepath (string)
    """

    path = lucidity.format(data_p, conf.templates)
    return path[0]


# v Parse and format functions                                   ║
# ^ =============================================================╝
# v =============================================================╗
# v Tests                                                        ║

if __name__ == '__main__':
    pass

# ^ Tests                                                        ║
# ^ =============================================================╝
