__author__ = 'hsh'
# -*- coding:utf-8 -*-

import codecs

class SeedManager():

    def __init__(self, seedFile):
        self.seeds = self.BuildSeed(seedFile)

    def BuildSeed(self, seedFile):
        if not seedFile:
            assert "seedFile is none"
        seeds = []
        reader = open(seedFile, "r")
        for line in reader:
            seeds.append(line.strip())
        seeds = set(seeds)
        return seeds

    def HasSeed(self, query):
        for seed in self.seeds:
            if seed in query:
                return seed
        return None

def ComputeCoverageOfSeed(seedFile, queryFile):
    seedManager = SeedManager(seedFile)
    c = 0
    reader = open(queryFile, "r")
    for line in reader:
        query = line.strip().split(">")[1]
        if seedManager.HasSeed(query):
            c += 1
        else:
            print query
    print c

def FindQuestion(seedFile, querySet, outputFile):
    seedManager = SeedManager(seedFile)
    writer = open(outputFile, "w")
    reader = open(querySet, "rb")
    #f = codecs.open(querySet, "r", encoding="utf-8")
    lineNum = 0
    for line in reader:
        query = line.strip().split("\t")[0]

        lineNum += 1
        if lineNum % 100000 == 0:
            print lineNum
        seed = seedManager.HasSeed(query)
        if seed:
            writer.write(str.format("{0}\t{1}\n", line.strip(), seed))
    writer.close()

def FindHighFre(inputFile, outputFile, threshold=1000):
    reader = open(inputFile, "rb")
    writer = open(outputFile, "w")
    for line in reader:
        freq = int(line.split("\t")[1])
        if freq > threshold:
            writer.write(line.strip() + "\n")

if __name__ == "__main__":
    seedFile = "seed"
    querySet = "F:\\query.tsv"
    outputFile = "F:\\query.tsv.question"
    outputFile_2 = "F:\\query.tsv.head.question"
    # ComputeCoverageOfSeed("seed", "/Users/hsh/Downloads/NLPCC-2015-OpenQA-TestSet/NLPCC-2015-OpenQA-Questions-Chinese-Formated")
    # FindQuestion(seedFile, querySet, outputFile)
    FindHighFre(outputFile, outputFile_2)