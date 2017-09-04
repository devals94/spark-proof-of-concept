UP2017data = sc.textFile("/project/UpAssembly").map(lambda line : line.split(","))
candidatesCount = UP2017data.filter(lambda line: line[6] == 'INC').map(lambda line: ((line[3]),1))
assemblyCountofINC = candidatesCount.reduceByKey(lambda a,b: a+b)
assemblyCountofINC.sortByKey(False).collect()