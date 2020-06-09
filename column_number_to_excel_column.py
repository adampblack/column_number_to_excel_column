# converts a column number into an alphabetical column format
# 1-26 is a-z
# 27-52 is aa-az
# 53-78 is ba-bz
# etc
def column_number_to_excel_column(intColumnCounter):
    # first letter in two letter cell references
    intFirstLetterCounter = -1 # zero indexed tuple
    # second letter in two letter cell references
    intSecondLetterCounter = intColumnCounter
    
    # tuple with alphabet A-Z
    tplAlphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    
    # for two letter cell references
    # find out the first letter of cell reference
    while intSecondLetterCounter > 25:
         intFirstLetterCounter += 1
         intSecondLetterCounter -= 26
         
    # check if one letter cell reference
    if intColumnCounter < 26:
        # one letter cell reference
        strOutput = tplAlphabet[intColumnCounter]
    else:     
        # two letter cell reference
        strOutput = tplAlphabet[intFirstLetterCounter] + tplAlphabet[intSecondLetterCounter]
    
    return strOutput
