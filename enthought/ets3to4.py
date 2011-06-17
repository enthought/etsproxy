"""
updates ETS imports to avoid proxy
"""
import sys
import os
from os.path import join


# Please note that the order of items in this list matters.
MAP = [
    # pyface
    ('enthought.pyface', 'pyface'),
    ('enthought.qt', 'pyface.qt'),
    ('enthought.resource', 'pyface.resource'),
    ('enthought.util.guisupport', 'pyface.util.guisupport'),
    ('enthought.util.wx', 'pyface.wx'),
    # traitsui
    ('enthought.traits.ui', 'traitsui'),
    # traits
    ('enthought.traits', 'traits'),
    ('enthought.etsconfig', 'traits.etsconfig'),
    ('enthought.util', 'traits.util'),
    ('enthought.testing', 'traits.testing'),
    # enable
    ('enthought.enable', 'enable'),
    ('enthought.kiva', 'kiva'),
    ('enthought.savage', 'enable.savage'),
    # chaco
    ('enthought.chaco', 'chaco'),
    # envisage
    ('enthought.envisage', 'envisage'),
    ('enthought.plugins', 'envisage.plugins'),
    # graphcanvas
    ('enthought.graphcanvas', 'graphcanvas'),
    # scimath
    ('enthought.interpolate', 'scimath.interpolate'),
    ('enthought.physical_quantities', 'scimath.physical_quantities'),
    ('enthought.mathematics', 'scimath.mathematics'),
    ('enthought.units', 'scimath.units'),
    # blockcanvas
    ('enthought.block_canvas', 'blockcanvas'),
    ('enthought.greenlet', 'blockcanvas.greenlet'),
    ('enthought.numerical_modeling', 'blockcanvas.numerical_modeling'),
    ('enthought.model', 'blockcanvas.model'),
    # codetools
    ('enthought.blocks', 'codetools.blocks'),
    ('enthought.blocks2', 'codetools.blocks2'),
    ('enthought.contexts', 'codetools.contexts'),
    ('enthought.execution', 'codetools.execution'),
    # etsdevtools
    ('enthought.debug', 'etsdevtools.debug'),
    ('enthought.developer', 'etsdevtools.developer'),
    ('enthought.endo', 'etsdevtools.endo'),
    # apptools
    ('enthought.appscripting', 'apptools.appscripting'),
    ('enthought.help', 'apptools.help'),
    ('enthought.io', 'apptools.io'),
    ('enthought.logger', 'apptools.logger'),
    ('enthought.naming', 'apptools.naming'),
    ('enthought.permissions', 'apptools.permissions'),
    ('enthought.persistence', 'apptools.persistence'),
    ('enthought.preferences', 'apptools.preferences'),
    ('enthought.scripting', 'apptools.scripting'),
    ('enthought.sweet_pickle', 'apptools.sweet_pickle'),
    ('enthought.template', 'apptools.template'),
    ('enthought.type_manager', 'apptools.type_manager'),
    ('enthought.undo', 'apptools.undo'),
    # mayavi
    ('enthought.mayavi', 'mayavi'),
    ('enthought.tvtk', 'tvtk'),
]


def update_file(path):
    fi = open(path)
    data = fi.read()
    fi.close()

    for old, new in MAP:
        data = data.replace(old, new)

    fo = open(path, 'w')
    fo.write(data)
    fo.close()


def main():
    if len(sys.argv) > 1:
        print """usage: ets3to4

This utility, can be used to convert projects from ETS version 3 to 4.
It simply replaces old namespace strings (e.g. 'enthought.traits.api')
to new ones (e.g. 'traits.api'), in all Python files in the CWD
recursively.
Once the conversion of your project is complete, the etsproxy module
should no longer be necessary.  However, this tool is very simple and
does not catch all corner cases.
"""
        return

    for root, dirs, files in os.walk(os.getcwd()):
        parts = root.split(os.sep)
        if '.git' in parts or '.svn' in parts or 'etsproxy' in parts:
            continue
        for fn in files:
            if fn.endswith('.py'):
                update_file(join(root, fn))


if __name__ == '__main__':
    main()
