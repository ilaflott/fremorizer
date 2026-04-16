"""
version info for fremorizer, isolated to avoid importing heavy dependencies at build time
"""

import os
version = os.getenv("GIT_DESCRIBE_TAG", "0.1.2")
__version__ = version
