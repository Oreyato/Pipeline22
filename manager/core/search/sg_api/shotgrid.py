from shotgun_api3 import shotgun
from manager import conf

from pprint import pprint

sg = None


def get_shotgun():
    global sg

    if not sg:
        sg = shotgun.Shotgun(conf.sg_link,
                             script_name=conf.sg_login,
                             api_key=conf.sg_key)
    return sg


def get_shotgun_files(current_project_id_p, current_type_p, filters_p=[]):
    sg = get_shotgun()

    filters = filters_p
    project_filter = ['project', 'is', {'type': 'Project', 'id': current_project_id_p}]
    filters.append(project_filter)

    fields = ["code", "sg_status_list", "sg_asset_type"]  # get "Asset Name", "Status" and "Type" columns

    return sg.find(current_type_p, filters, fields)


# v =============================================================╗
# v Tests                                                        ║

if __name__ == '__main__':
    sg = get_shotgun()
    print(sg)

    project_id = conf.projects.get("micromovie").get("sg_id")

    sg_files = get_shotgun_files(project_id, "Asset")
    pprint(sg_files)

    pass

# ^ Tests                                                        ║
# ^ =============================================================╝