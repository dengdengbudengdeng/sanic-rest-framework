"""
  ____              _        ____  _____ ____ _____    __                                             _
 / ___|  __ _ _ __ (_) ___  |  _ \| ____/ ___|_   _|  / _|_ __ __ _ _ __ ___   _____      _____  _ __| | __
 \___ \ / _` | '_ \| |/ __| | |_) |  _| \___ \ | |   | |_| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
  ___) | (_| | | | | | (__  |  _ <| |___ ___) || |   |  _| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
 |____/ \__,_|_| |_|_|\___| |_| \_\_____|____/ |_|   |_| |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\

"""

__title__ = 'Sanic REST framework'
__version__ = '0.1.0'
__author__ = '等等不等等'
__license__ = 'MIT'
__copyright__ = 'Copyright 2025-present 等等不等等'

# Version synonym
VERSION: str = __version__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING: str = 'iso-8859-1'

# Default datetime input and output formats
ISO_8601: str = 'iso-8601'


class RemovedInSRF316Warning(DeprecationWarning):
    pass


class RemovedInSRF317Warning(PendingDeprecationWarning):
    pass
