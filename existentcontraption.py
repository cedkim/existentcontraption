#!/usr/bin/python3
"""
Existent Contraption Tool
------
Convert Fantastic Contraption level XML to
SVG files that can be used for cutting out
little desk toys.
"""

import svgwrite

class ExistentContraption:
    def __init__(self, levelXml, scale=1):
        self.levelXml = levelXml
        self.scale = scale
    def convertToSvg(self):
        dwg = svgwrite.Drawing('existentcontraption.svg', size=(str(100 * self.scale) + 'mm', str(100 * self.scale) + 'mm'), profile='tiny')
        return dwg.toString()

if __name__ == '__main__':
    pass
