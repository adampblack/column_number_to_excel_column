# Converts a column number into the column cell reference used in Microsft Excel.

This is useful when using libraries which read and write data to excel spreadsheets, such as **openpyxl**.

* 1-26 is a-z
* 27-52 is aa-az
* 53-78 is ba-bz
 
 etc

The column number zero starts with A (zero-indexed).

This code is written in **python 3**.

## Testing

for n in range(0, 100):
  column_number_to_excel_column(n)
  
### Output

'A'
'B'
'C'
'D'
'E'
'F'
'G'
'H'
'I'
'J'
'K'
'L'
'M'
'N'
'O'
'P'
'Q'
'R'
'S'
'T'
'U'
'V'
'W'
'X'
'Y'
'Z'
'AA'
'AB'
'AC'
'AD'
'AE'
'AF'
'AG'
'AH'
'AI'
'AJ'
'AK'
'AL'
'AM'
'AN'
'AO'
'AP'
'AQ'
'AR'
'AS'
'AT'
'AU'
'AV'
'AW'
'AX'
'AY'
'AZ'
'BA'
'BB'
'BC'
'BD'
'BE'
'BF'
'BG'
'BH'
'BI'
'BJ'
'BK'
'BL'
'BM'
'BN'
'BO'
'BP'
'BQ'
'BR'
'BS'
'BT'
'BU'
'BV'
'BW'
'BX'
'BY'
'BZ'
'CA'
'CB'
'CC'
'CD'
'CE'
'CF'
'CG'
'CH'
'CI'
'CJ'
'CK'
'CL'
'CM'
'CN'
'CO'
'CP'
'CQ'
'CR'
'CS'
'CT'
'CU'
'CV'
