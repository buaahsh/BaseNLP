__author__ = 'hsh'



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


if __name__ == "__main__":
    ComputeCoverageOfSeed("seed", "/Users/hsh/Downloads/NLPCC-2015-OpenQA-TestSet/NLPCC-2015-OpenQA-Questions-Chinese-Formated")