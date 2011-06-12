===================================================
etsproxy: proxy modules for backwards compatibility
===================================================

This is the ETS proxy package, it contains the proxy modules for *all* ETS
projects which map the old enthought namespace imports to the
namespace-refactored ETS packages.  For exmaple:

    from enthought.traits.api import HasTraits

is now simply:

    from traits.api import HasTraits


This module will be removed in the future, and old-style (enthought.xxx)
imports should be converted (over time) to the new ones.
