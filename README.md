# cs370-project
Final group project for CS370 or parallel processing at Cal Poly Pomona. 

##The Problem:
Our professor is lost in a park with only his laptop and connection to our lab.  We have already downloaded a map of the park which describes various landmarks in the park. Our objective is to find the professor and route him to the southern border where there is a roadway being as efficient as possible and not hurting or killing the professor.

Our map is a list of characters which represent a 0.3m x 0.3m squares of ‘T’ - Tree, ‘R’ - Roadway, ‘C’ - Cliff, or O’ - Open Terrain
We can tell the professor to do one of two things: Look in any direction and report is surroundings back to the lab (Forwards, Backwards, Left, Right) and move in any of the previously stated directions.

##Sample input:


##The Solution:
###Finding the Professor
First we must find the professor. We use a method of pattern matching where we generate a list of plausible locations for the professor given his current surroundings. These are represented in green.
#@#@@!$$@IMAGE HERE
###The Optimum Direction
We then tell the professor to move in an optimum direction. This direction is determined by a 'score' map that we generate before giving the professor any instructions. The information in this map yeilds the cost to move from any given location on the map to the finish and the best direction to do so. The direction we move the professor is determined by the direction which yeilds the most correct directions to the finish.

