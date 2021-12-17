# Copyright New York University and the TUF contributors
# SPDX-License-Identifier: MIT OR Apache-2.0

"""
Define TUF exceptions used inside the new modern implementation.
The names chosen for TUF Exception classes should end in 'Error' except where
there is a good reason not to, and provide that reason in those cases.
"""


class LengthOrHashMismatchError(Exception):
    """An error while checking the length and hash values of an object."""


#### Repository errors ####


class RepositoryError(Exception):
    """An error with a repository's state, such as a missing file."""


class UnsignedMetadataError(RepositoryError):
    """An error about metadata object with insufficient threshold of
    signatures."""


class BadVersionNumberError(RepositoryError):
    """An error for metadata that contains an invalid version number."""


class ExpiredMetadataError(RepositoryError):
    """Indicate that a TUF Metadata file has expired."""


#### Download Errors ####


class DownloadError(Exception):
    """An error occurred while attempting to download a file."""


class DownloadLengthMismatchError(DownloadError):
    """Indicate that a mismatch of lengths was seen while downloading a file."""


class SlowRetrievalError(DownloadError):
    """Indicate that downloading a file took an unreasonably long time."""


class FetcherHTTPError(DownloadError):
    """
    Returned by FetcherInterface implementations for HTTP errors.

    Args:
        message: The HTTP error messsage
        status_code: The HTTP status code
    """

    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.status_code = status_code
