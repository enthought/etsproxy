"""
updates ETS imports to avoid proxy
"""
import os
from os.path import join


MAP = [
    # traitsui
    ('enthought.traits.ui', 'traitsui'),
    # traits
    ('enthought.traits', 'traits'),
    ('enthought.etsconfig', 'traits.etsconfig'),
    ('enthought.util', 'traits.util'),
    ('enthought.logger', 'traits.logger'),
    ('enthought.qt', 'traits.qt'),
    ('enthought.testing', 'traits.testing'),
    # pyface
    ('enthought.pyface', 'pyface'),
    ('enthought.resource', 'pyface.resource'),
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
    for root, dirs, files in os.walk(os.getcwd()):
        parts = root.split(os.sep)
        if '.git' in parts:
            continue
        for fn in files:
            if fn.endswith('.py'):
                update_file(join(root, fn))


if __name__ == '__main__':
    main()
