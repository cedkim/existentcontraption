from svgnest import nest
def mergeFiles(filesToMerge=[],outputFilename='merged.svg',sheetSize=(140,140)):
    """Merge SVG files
    This function is for merging SVG files from EC
    into one SVG file.

    Parameters:
    filesToMerge -- a list of the original SVG file paths
    outputFilename -- the output file name (default='merged.svg')
    sheetSize -- a two-element tuple for the size of a material sheet in mm (default=(140,140))
    """
    currentFileNum = 0
    files = {}
    for fileToMerge in filesToMerge:
        currentFileNum += 1
        files.update(fileToMerge, currentFileNum)
    nest(outputFilename, files, 600, 300)
