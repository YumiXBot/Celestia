import glob
from os.path import basename, dirname, isfile


def __list_all_modules():
    mod_paths = glob.glob(dirname(__file__) + "/*.py")

    games_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return games_modules


GAMES_MODULES = sorted(__list_all_modules())
__all__ = GAMES_MODULES + ["GAME_MODULES"]

