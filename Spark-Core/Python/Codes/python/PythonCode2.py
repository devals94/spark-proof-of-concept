UP2017data = sc.textFile("/project/UpAssembly").map(lambda line : line.split(","))
candidatesMinVotes = UP2017data.map(lambda line: ((int(line[7])),line[5]))
candidatesMinVotes.sortByKey(True).take(5)