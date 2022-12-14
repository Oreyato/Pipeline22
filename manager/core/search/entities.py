from manager.core.search.base_search import BaseSearchSystem
from manager.conf.conf_files import use_fs


def new_get_entities(filters_p):
    fs_entities = []
    sg_entities = []

    # Test if one of the filters key is equal to turn_point
    use_filesystem = False
    for part in filters_p.keys():
        for turn_point in use_fs:
            if part == turn_point:
                use_filesystem = True

    if use_filesystem:
        from manager.core.search.fs.file_search import FilesystemSearch
        fs_entities = FilesystemSearch.new_get_entities(filters_p)
    else:
        from manager.core.search.sg_api.sg_search import ShotgridSearchSystem
        sg_entities = ShotgridSearchSystem.new_get_entities(filters_p)

    fs_entities.extend(sg_entities)

    return fs_entities


if __name__ == "__main__":
    print("Test")
