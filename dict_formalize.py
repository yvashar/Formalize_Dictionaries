import sys
import json,ast
# print ast.literal_eval(json.dumps(matchingKeyValues)) => will remove 'u' in "u'DIC_KEY"
import io
import os
dirpath = './output'
def readFile(filename):
	fileReader = open(filename,'r')
	fileContent = json.loads(fileReader.read())
	fileReader.close()
	return fileContent


pcmacFileName = sys.argv[1]
compFileName = sys.argv[2]
pcmacFile = readFile(pcmacFileName)
compFile = readFile(compFileName)
matchingKeyValues = {}
extraKeys = {}
unmatchedValues = {}
for key in pcmacFile:
	if key in compFile.keys():
		if(pcmacFile[key] == compFile[key]):
			matchingKeyValues[key] = pcmacFile[key]
		else:
			unmatchedValues[key] = compFile[key]
	else:
		extraKeys[key] = pcmacFile[key]

# print (json.dumps(unmatchedValues,ensure_ascii=False).encode('utf-8'))
if(os.path.isdir(dirpath) == False):
	os.mkdir(dirpath)
with open('output/matchingKeyValues.txt', 'w') as outfile:
	json.dump(matchingKeyValues, outfile)
with open('output/unmatchedValues.txt', 'w') as outfile:
	json.dump(unmatchedValues, outfile)
with open('output/extraKeys.txt', 'w') as outfile:
	json.dump(extraKeys,outfile)

# f = open('listJson.txt', 'w')
# f.write((' '.join(unmatchedValues)).encode('utf-8'))
# f.close
    



