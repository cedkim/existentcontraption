#!/usr/bin/python3
"""
Existent Contraption Tool
------
Convert Fantastic Contraption design XML to
SVG files that can be used for cutting out
little desk toys.
"""

import svgwrite
import xml.etree.ElementTree as ET

class ECConstants:
    """Existent Contraption constant definition class
    This class simply contains constants used in Existent Contraption.
    """
    LASERTOLERANCE = 0.03
    FDMTOLERANCE = 0.5

class ExistentContraption:
    """The main ExistentContraption class

    Constructor arguments:
    designXml -- the XML save/retrieve data of the FC design to convert
    scale (default=1) -- an integer to multiply the physical size of the SVG with
    """
    def __init__(self, designXml='', scale=1):
        """Constructor function for the main ExistentContraption class
        (arguments are listed in class definition)
        """
        self.designXml = designXml
        self.scale = scale
    def convertToSvg(self, tolerance=0.03):
        """A function to convert an ExistentContraption class
           that has valid XML to a list of SVGs that can be
           used for manufacturing.
        
        Keyword arguments:
        tolerance (default=0.03) -- the tolerance value in mm, recommended
                                    values are in the ECConstants class
        
        Returns a list of SVG strings
        """
        if (len(self.designXml) > 0):
            xmlRoot = ET.fromstring(self.designXml)
            dwgList = []
            for child in xmlRoot.find('level').find('playerBlocks'):
                if child.tag == 'SolidRod':
                    newDwg = svgwrite.drawing.Drawing(size=(str((int(child.find('width')) / (2 / this.scale)) + 2) + 'mm', str((int(child.find('height')) / (2 / this.scale)) + 2) + 'mm'))
                    newDwg.add(newDwg.rect(insert=(this.scale, this.scale), size=(int(child.find('width') / (2 / this.scale))), int(child.find('height') / (2 / this.scale)))), stroke='black', stroke-width=this.scale))
                    dwgList.append(newDwg)
            svgOutputs = []
            for dwg in dwgList:
                svgOutputs.append(dwg.toString())
            return svgOutputs
        else:
            return '<!-- Error: No level XML provided -->'

if __name__ == '__main__':
    """The main entrypoint for the EC CLI tool"""
    pass # to-do
