#!/usr/bin/python3
"""
Existent Contraption Tool
------
Convert Fantastic Contraption level XML to
SVG files that can be used for cutting out
little desk toys.
"""

import svgwrite
import xml.etree.ElementTree as ET

class ExistentContraption:
    def __init__(self, levelXml='', scale=1):
        self.levelXml = levelXml
        self.scale = scale
    def convertToSvg(self):
        if (len(self.levelXml) > 0):
            xmlRoot = ET.fromstring(self.levelXml)
            dwg = svgwrite.Drawing('existentcontraption.svg', size=(str(100 * self.scale) + 'mm', str(100 * self.scale) + 'mm'), profile='tiny')

            return dwg.toString()
        else:
            return '<!-- Error: No level XML provided -->'

if __name__ == '__main__':
    pass
