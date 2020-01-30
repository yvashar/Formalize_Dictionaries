import sys
import json
import ast

# fileReader = open(sys.argv[1],'r')
# content = json.dumps(json.loads(fileReader.read()),ensure_ascii=False,sort_keys=True).encode('utf-8')
# print content
#===========================================================================
baseDic={}
def createDictFile(fileName):
	fileReader = open(fileName,'r')
	content = json.loads(fileReader.read())
	return content

#below method remove the duplicates from dictionary
def removeDuplicate(dict1):
	finalDic = {}
	for key in dict1:
		if key not in finalDic:
			finalDic[key] = dict1[key]
	return finalDic

dict1 = createDictFile('output/matchingKeyValues.txt')
dict2 = createDictFile('output/unmatchedValues.txt')
dict3 = createDictFile('output/extraKeys.txt')
baseDic.update(dict1)
baseDic.update(dict2)
baseDic.update(dict3)
finalDict = removeDuplicate(baseDic)
finalDict = json.dumps(finalDict,ensure_ascii=False,sort_keys=True).encode('utf-8')
print finalDict
