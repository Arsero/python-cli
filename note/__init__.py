import os
from appdirs import *

__app_name__ = "note"
__company_name__ = "arsero"
__version__ = "0.0.3"
__filename__ = os.path.join(user_data_dir(
    __app_name__, __company_name__), "notes.txt")

(
    FILE_ERROR,
    ID_ERROR,
) = range(2)

ERRORS = {
    FILE_ERROR: "file error",
    ID_ERROR: "task not found",
}
