UP2017data = sc.textFile("/project/UpAssembly").map(lambda line : line.split(","))
votesCount = UP2017data.filter(lambda line: line[6]=='BJP+').map(lambda line: (line[5],line[7],line[4]))
maxVotesInBJP = votesCount.max()
print(maxVotesInBJP)