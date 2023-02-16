from typing import Any

import pkg_resources  # type: ignore

from .api import (
    download,
    get_fsspec_https_session,
    get_requests_https_session,
    get_s3_credentials,
    get_s3fs_session,
    login,
    open,
    search_data,
    search_datasets,
)
from .auth import Auth
from .search import DataCollections, DataGranules
from .store import Store

__all__ = [
    "login",
    "search_datasets",
    "search_data",
    "get_requests_https_session",
    "get_fsspec_https_session",
    "get_s3fs_session",
    "get_s3_credentials",
    "open",
    "download",
    "DataGranules",
    "DataCollections",
    "Auth",
    "Store",
]

__auth__ = Auth()
__store__: Any = None

__version__ = pkg_resources.get_distribution("earthaccess").version
