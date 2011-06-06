#  Copyright (c) 2011 by Enthought, Inc.
#  All rights reserved.

import warnings

warnings.warn("enthought namespace imports are deprecated",
              DeprecationWarning)


try:
    __import__('pkg_resources').declare_namespace(__name__)
except:
    pass

