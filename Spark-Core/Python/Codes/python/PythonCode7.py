UP2017data = sc.textFile("/project/UpAssembly").map(lambda line : line.split(","))
candidatesCount = UP2017data.map(lambda line: (line[1],1))
candidatesCountWithPhase = candidatesCount.reduceByKey(lambda a,b: a+b)
candidatesCountWithPhase.sortByKey().collect()