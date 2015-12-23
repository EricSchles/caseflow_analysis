This set of tools represents the analysis portion of the application.  The goal of this tool is to create a way to determine what pieces of CaseFlow need to be attacked next.  

We want to tell two stories - the case level story and the system level story.  This means being able to tell information about the system at a high level as well as figuring out how each case moves through the system.

Also, note that this is only how long a case has sat in the queue per department, not how long it took to complete.  To get a realistic sense of actual productivity challeneges:

* the size per department,
* and average productivity per unit will be needed.  

If possible getting a sense of:

* worker productivity, 
* skill level, 
* access level (what documents they can see/read/write), 
* what tools they have available   

__Definition__ := We'd call this the technology constant and it would be based on how many parts of their task they can do automatically.  

**Conjecture** : Some of this may be just giving workers access / teaching them how to use what they already have available to them.

Drilling down:

##Metrics to Track per Case Type

Below node means at the process level or the team level:

###Task Level information:

* total tasks 
* completed tasks 
* completed tasks per node 
* total tasks per node 
* ave tasks per node 
* std dev tasks per node 
* skew tasks per node 
* kurt tasks per node 

###Hours spent per task

* total hours per node 
* ave task hours per node 
* std dev task hours per node 
* skew task hours per node 
* kurtosis task hours per node 

#Days spent per task
* total days per node 
* ave task days per node 
* std dev task days per node 
* skew task days per node 
* kurtosis task days per node 

##How To Rank Cases 

* average hours spent, 
* variance in time spent, 
* by total time spent, 
* by number of tasks completed,
* by total number of nodes traversed, 
* by number of nodes traversed over time - if case goes between  A <-> B quickly but A <-> C slowly, then this must be documented and accounted for (for example)

## How To Rank Connections aka Departmental Interoperability

See which pairs of nodes performs the best on average.  So this analysis will focus on how long it takes to transition work from node A to node B (For example), where node is at the process and team level.

## Assess System Over Time
    
As new cases come in a base line should be established for how well the system is doing from time to time.  This is more or less measuring average productivity over time and looking at the first and second derivative over time.  

This metric is not very fleshed out but more or less we are looking at how long a case takes on average for each case type over time.  We are also looking at the average rate of processing (is this increasing? Decreasing?).  If it is increasing then we can say that our system performance is improving (we want to know when/how/why).  Increase or decrease is captured by the first derivative.  The second derivative captures how fast things are increasing or decreasing.  So if things are increasing based on the first derivative but only increasing a little (based on the second derivative) then we shouldn't be too excited.  

## Projected System Performance

When enough data has been added, we'll be able to assess how well the system performs on average and project how well it should perform if parts of the process are improved.  By understanding the productivity increases of new systems, we'll have a sense of what to work on next - assumes we can determine this ahead of time.

