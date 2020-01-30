dict_formalize.py 

input: pcmacLocale.json and cdLocale.json
output: generates three files inside /output directory
	     1. matchingKeyValues.txt - which has the list of key-value pairs with same key and values in both the locales
	     2. unmatchedValues.txt - which has the list of key-value pairs with same key but different values. The value is taken from the cdLocale file.
	     3. extraKeys.txt - which has the list of key-value pairs used only by pcmac
how to run: python dict_formalize.py

#######################################################################################################decodeValues.py

Need for this script: when the locale file has non-english string, the output of dict_formalize.py has 						 unicode characters.This script converts the file with unicode character to 						  respectivelanguage.

how to run:  python decodeValues.py inputFilewithUnicode.txt > final.txt

final.txt will have the required output in the sorted order of keys.

