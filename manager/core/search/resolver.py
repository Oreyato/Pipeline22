import lucidity
from manager import conf

# v =============================================================╗
# v Parse and format functions                                   ║


def parse(pathP):
    """
    From a path, identify a template and parse data

    :return: data
    """

    data = lucidity.parse(pathP, conf.templates)
    return data[0]


def format(dataP):
    """
    Format data into a filepath, while identifying the correct template

    :return: filepath (string)
    """

    path = lucidity.format(dataP, conf.templates)
    return path[0]


# v Parse and format functions                                   ║
# ^ =============================================================╝
# v =============================================================╗
# v Tests                                                        ║

if __name__ == '__main__':
    pass

# ^ Tests                                                        ║
# ^ =============================================================╝
