# Stubs for galaxy.objectstore.s3 (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .s3_multipart_upload import multipart_upload as multipart_upload
from ..objectstore import convert_bytes as convert_bytes, ObjectStore as ObjectStore

boto = ...  # type: Any
NO_BOTO_ERROR_MESSAGE = ...  # type: str
log = ...  # type: Any

class S3ObjectStore(ObjectStore):
    staging_path = ...  # type: Any
    transfer_progress = ...  # type: int
    bucket = ...  # type: Any
    cache_size = ...  # type: Any
    sleeper = ...  # type: Any
    cache_monitor_thread = ...  # type: Any
    use_axel = ...  # type: bool
    def __init__(self, config, config_xml) -> None: ...
    def file_ready(self, obj, **kwargs): ...
    def exists(self, obj, **kwargs): ...
    def create(self, obj, **kwargs): ...
    def empty(self, obj, **kwargs): ...
    def size(self, obj, **kwargs): ...
    def delete(self, obj, entire_dir: bool = ..., **kwargs): ...
    def get_data(self, obj, start: int = ..., count: int = ..., **kwargs): ...
    def get_filename(self, obj, **kwargs): ...
    def update_from_file(self, obj, file_name: Optional[Any] = ..., create: bool = ..., **kwargs): ...
    def get_object_url(self, obj, **kwargs): ...
    def get_store_usage_percent(self): ...

class SwiftObjectStore(S3ObjectStore): ...
