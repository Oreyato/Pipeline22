import os

import lucidity
from manager import conf
from pathlib import Path

from manager.core.fs import file_search


# project_path = Path(conf.pipeline_path) / conf.projects.get(project_name)
project_path = Path(conf.pipeline_path) / "MMOVIE"
print(f"Project path: {project_path}")

# v Templates ===================================================
root = lucidity.Template('root', str(project_path).replace(os.sep, "/"))
resolver = {}
resolver[root.name] = root

general_template = lucidity.Template('general',
                                     '{@root}/{type}',
                                     template_resolver=resolver)

assets_template = lucidity.Template('asset',
                                    '{@root}/{type}/{category}/{name}/{task}/v{versionNb}/{name}_{state}.{ext}',
                                    template_resolver=resolver)
shots_template = lucidity.Template('shot',
                                   '{@root}/{type}/sq{sqNb}/sh{shNb}/{task}/v{versionNb}/sh{shNb}_{state}.{ext}',
                                   template_resolver=resolver)
# ^ Templates ===================================================

def parse(pathP):
    """
    From a path, identify a template and parse data

    :return: data
    """
    print('v======= INSIDE PARSE =======v')
    path = pathP

    type = general_template.parse(path)

    if type.get('type') == 'assets':
        data = assets_template.parse(path)
        return data
    elif type.get('type') == 'shots':
        data = shots_template.parse(path)
        return data

    print('^======= INSIDE PARSE =======^')
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
    fileAPath = 'D:/TD4/Paul/Pipeline/MMOVIE/assets/locations/desert/modeling/v001/desert_work.hipnc'
    print(fileAPath)

    fileAData = parse(fileAPath)
    print(fileAData)
    fileBData = parse('D:/TD4/Paul/Pipeline/MMOVIE/shots/sq010/sh010/animation/v001/sh010_work.ma')
    print(fileBData)

    fileAPath = format(fileAData)
    print(fileAPath)
    print(format(fileBData))

# ^ Tests                                                        ║
# ^ =============================================================╝