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
        # Adds arguments to object
        self.designXml = designXml
        self.scale = scale
    def convertToSvg(self, tolerance=0.03, materialThickness=5):
        """A function to convert an ExistentContraption class
           that has valid XML to a list of SVGs that can be
           used for manufacturing.
        
        Keyword arguments:
        tolerance (default=0.03) -- the tolerance value in mm, recommended
                                    values are in the ECConstants class
        materialThickness (default=5) -- the thickness of a material sheet in
                                         millimeters

        Returns a list of SVG strings
        """
        if (len(self.designXml) > 0): # checks if design XML actually exists
            xmlRoot = ET.fromstring(self.designXml) # parse XML from string
            dwgList = [] # create list of drawings
            thickness = 0 # create variable to store thickness in layers
            for child in xmlRoot.find('level').find('playerBlocks'): # iterate through all design blocks
                if (child.tag == 'SolidRod') or (child.tag == 'HollowRod'): # check if block is a rod
                    for _ in range(2): # repeat adding rods two times to prevent model from collapsing
                        newDwg = svgwrite.drawing.Drawing(size=(str((int(child.find('width')) / (2 / self.scale)) + 2) + 'mm', str((10 * self.scale) + 2) + 'mm')) # create a drawing with the appropriate size
                        newDwg.add(newDwg.rect(insert=(1, 1), size=(int(child.find('width')) / (2 / self.scale), 10 * self.scale), stroke='black', stroke_width=self.scale*0.8)) # add the rod to the drawing
                        newDwg.add(newDwg.circle(center=(8 * self.scale, 5 * self.scale), r=2.5*self.scale, stroke='black', stroke_width=self.scale*0.8)) # add the first hinge slot
                        newDwg.add(newDwg.rect(insert=(2 * self.scale, materialThickness / 2), size=(4 * self.scale, materialThickness), stroke='black', stroke_width=self.scale*0.8)) # add hole in first hinge slot
                        newDwg.add(newDwg.circle(center=((int(child.find('width')) / (2 / self.scale)) - 8, 5 * self.scale), r=2.5*self.scale, stroke='black', stroke_width=self.scale*0.8)) # add the second hinge slot
                        newDwg.add(newDwg.rect(insert=(int(child.find('width')) - (2 * self.scale), materialThickness / 2), size=(4 * self.scale, materialThickness), stroke='black', stroke_width=self.scale*0.8)) # add hole in second hinge spot
                        dwgList.append(newDwg) # add the drawing to the list of drawings
                        thickness += 1 # increment the thickness (in layers)
            for _ in range(thickness): # iterate through layers
                newDwg = svgwrite.drawing.Drawing(size=(str((thickness * materialThickness) + 2) + 'mm', str(((4 * self.scale) - tolerance) + 2) + 'mm')) # create a drawing for the joint connector
                newDwg.add(newDwg.rect(insert=(1, 1), size=(int(thickness * materialThickness), int((4 * self.scale) - tolerance)), stroke='black', stroke_width=self.scale*0.8)) # add the joint connector to the drawing
                dwgList.append(newDwg) # add the joint connector drawing to the list of drawings
            svgOutputs = [] # define a list for SVG string outputs
            for dwg in dwgList: # iterate over all drawings
                svgOutputs.append(dwg.toString()) # convert the drawings to SVG strings and add them to the output list
            return svgOutputs # return the output values
        else: # runs if design XML is an empty string
            return '<!-- Error: No design XML provided -->' # returns an error in case no XML is provided

if __name__ == '__main__':
    """The main entrypoint for the EC CLI tool"""
    pass # to-do
