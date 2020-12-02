This package is no longer maintained, and no current Enthought Tool Suite
projects should rely on it. If you encounter projects that still depend
on etsproxy, please open issues against those projects.


===================================================
etsproxy: proxy modules for backwards compatibility
===================================================

This is the ETS proxy package, it contains the proxy modules for *all* ETS
projects which map the old enthought namespace imports (version 3) to the
namespace-refactored ETS packages (version 4).  For example::

   from enthought.traits.api import HasTraits

is now simply::

   from traits.api import HasTraits

For convenience this package also contains a refactor tool to convert
projects to the new namespace (such that the don't rely on the proxy)::

   $ ets3to4 -h
   usage: ets3to4 DIRECTORY

   This utility, can be used to convert projects from ETS version 3 to 4.
   It simply replaces old namespace strings (e.g. 'enthought.traits.api')
   to new ones (e.g. 'traits.api'), in all Python files in DIRECTORY
   recursively.
   Once the conversion of your project is complete, the etsproxy module
   should no longer be necessary.  However, this tool is very simple and
   does not catch all corner cases.

This module will be removed in the future, and old-style (enthought.xxx)
imports should be converted (over time) to the new ones.
