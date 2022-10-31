import lucidity

general_template = lucidity.Template('general', '/{type}')

assets_template = lucidity.Template('asset', '/{type}/{category}/{name}/{task}/v{versionNb}/{name}_{state}.{ext}')
shots_template = lucidity.Template('shot', '/{type}/sq{sqNb}/sh{shNb}/{task}/v{versionNb}/sh{shNb}_{state}.{ext}')

def parse(pathP):
    """
    From a path, identify a template and parse data

    :return: data
    """
    type = general_template.parse(pathP)

    if type.get('type') == 'assets':
        data = assets_template.parse(pathP)
        return data
    elif type.get('type') == 'shots':
        data = shots_template.parse(pathP)
        return data

    pass


def format(dataP):
    """
    Format data into a filepath, while identifying the correct template

    :return: filepath (string)
    """

    if dataP.get('type') == 'assets':
        path = assets_template.format(dataP)
        return path
    elif dataP.get('type') == 'shots':
        path = shots_template.format(dataP)
        return path

    pass

# v =============================================================╗
# v Tests                                                        ║

if __name__ == '__main__':
    fileAPath = '/assets/locations/desert/modeling/v001/desert_work.hipnc'
    print(fileAPath)

    fileAData = parse(fileAPath)
    print(fileAData)
    fileBData = parse('/shots/sq010/sh010/animation/v001/sh010_work.ma')
    print(fileBData)

    fileAPath = format(fileAData)
    print(fileAPath)
    print(format(fileBData))

# ^ Tests                                                        ║
# ^ =============================================================╝