val SampleData = SplitData.map( x => (x(5),(x(11))) )
val FilteredByRuns = SampleData.filter( x => (x._2 != "by wickets" && x._2 != "Tie" && x._2 !="No Result"))
val ReduceByRuns = FilteredByRuns.map( x => (x._1,1)).reduceByKey(_+_)
val SwapByRuns = ReduceByRuns.map( item => item.swap)
val SortByRuns = SwapByRuns.sortByKey( ascending = false)
val CountByRuns = SortByRuns.collect.foreach(println)
