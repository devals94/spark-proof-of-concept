val MatchData = sc.textFile("/project/MatchNew")
val SplitData = MatchData.map(line => line.split(","))
val SampleData = SplitData.map( x => (x(5),1) )
val ReduceData = SampleData.reduceByKey(_+_)
ReduceData.collect()
val SwapData = ReduceData.map( item => item.swap )
val SortData = SwapData.sortByKey(ascending = false)
val TotalMatchesAtStadium = SortData.collect.foreach(println)
