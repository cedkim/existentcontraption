#!/usr/bin/python3
import sys
import os
from existentcontraption import *
import ecmanufacture
import fire
def convertFromXmlFile(path='',outputfolder='',combine=True,materialthickness=5,scale=1,machine=''):
    """
    Converts an XML file to several SVG files
    :param path: the path to your XML file
    :param outputfolder: a folder to save outputs to
    :param combine: whether or not to combine outputs into one SVG file (default: True)
    :param machine: which type of machine you're using ('laser' for laser cutter and 'fdm' for FDM 3D printer)
    :param materialthickness: the thickness in mm of a sheet of material (default: 5)
    :param scale: how many times larger than usual your output should be (default: 1)
    :return: some info
    """
    toleranceToUse = 0
    if machine == 'laser':
        toleranceToUse = ECConstants.LASERTOLERANCE
    elif machine == 'fdm':
        toleranceToUse = ECConstants.FDMTOLERANCE
    else:
        return "Please specify a machine type ('laser' or 'fdm')"
    openedFile = open(path, 'rt')
    ec = ExistentContraption(designXml=openedFile.read(), scale=scale)
    openedFile.close()
    outputSvgData = ec.convertToSvg(tolerance=toleranceToUse, materialThickness=materialthickness)
    if (outputfolder[-1] == "/") or (outputfolder[-1] == "\\"):
        outputfolder = outputfolder[:-1]
    sfIncrement = 0
    for svgFile in outputSvgData:
        sfIncrement += 1
        f = open(outputfolder + "/" + str(sfIncrement) + ".svg", "wt")
        f.write(svgFile)
        f.close()
    if combine:
        files = []
        for _ in range(sfIncrement)
            files.append(outputfolder + "/" + str(sfIncrement + 1))
        ecmanufacture.mergeFiles(filesToMerge=files,outputFilename=outputfolder + "/merged.svg")
        for f in range(sfIncrement):
            os.remove(outputfolder + "/" + str(sfIncrement + 1))
    return 'SVG generation complete!'
if __name__ == '__main__':
    fire.Fire(convertFromXmlFile)
