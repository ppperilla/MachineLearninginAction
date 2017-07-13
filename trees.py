#ID3
#
from math import log
import operator

#
#计算给定数据集的香浓熵
#
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob * log(prob,2)
	return shannonEnt
	pass

#
#创建数据集
#
def createDataSet():
	dataSet = [
			[1,1,'yes'],
			[1,1,'yes'],
			[1,0,'no'],
			[0,1,'no'],
			[0,1,'no']]
	labels = ['no surfacing','flippers']
	return dataSet,labels
	pass

#
#按照给定特征划分数据集
#
def splitDataSet(dataSet,axis,value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet 
	pass

#
#选择最好的数据集划分方式
#
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0; bestFeature = -1
	for i in range(numFeatures);
		featlist = [example[i] for example in dataSet]
		uniqueVals = set(featlist)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet,i,value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature
	pass

#
#多数表决
#
def majorityCnt(class_list):
	class_count = {}
	for vote in class_list:
		if vote not in class_count.keys(): class_count[vote] = 0
		class_count[vote] += 1
	sorted_class_count = sorted(class_count.iteritems(), key = operator.itemgetter(1) , reverse = True)
	return sorted_class_count[0][0]
	pass

#
#创建决策树
#
def createTree(data_set, labels):
	class_list = [example[-1] for example in data_set]
	if class_list.count(class_list[0]) == len(class_list):
		return class_list[0]
	if len(data_set[0]) == 1:
		return majorityCnt(class_list)
	best_feat = chooseBestFeatureToSplit(data_set)
	best_feat_label = labels[best_feat]
	my_tree = {best_feat_label:{}}
	del(labels[best_feat])
	feat_values = [example[best_feat] for example in data_set]
	unique_vals = set(feat_values)
	for value in unique_vals:
		sub_labels = labels[:]
		my_tree[best_feat_label][value] = createTree(splitDataSet(data_set,best_feat,value),sub_labels)
	pass