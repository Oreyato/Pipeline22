from pprint import pprint

from manager.core.search.base_search import BaseSearchSystem


def get_entities(project_name_p, soft_programs_p=[""], selected_type_p='asset'):
    fs_entities = []
    sg_entities = []

    condition = "b"

    if condition == "a":
        from manager.core.search.sg_api.sg_search import ShotgridSearchSystem
        fs_entities = ShotgridSearchSystem.get_entities(project_name_p, soft_programs_p, selected_type_p)
    elif condition == "b":
        from manager.core.search.fs.file_search import FilesystemSearch
        sg_entities = FilesystemSearch.get_entities(project_name_p, soft_programs_p, selected_type_p)

    entities = fs_entities + sg_entities

    return entities


if __name__ == "__main__":
    entities = get_entities("micromovie", ["Maya"], "shots")

    pprint(entities)
