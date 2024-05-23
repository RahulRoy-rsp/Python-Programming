- ### [2ndInningsNRR.ipynb](https://github.com/RahulRoy-rsp/Mine_Algorithms/blob/main/NET%20RUN%20RATE/2ndInningsNRR.ipynb)
  - I've Considered the Matches as follows:
      | Match No. | Home Team | Runs Scored (Overs faced) | Away Team | Runs Scored (Overs faced) | Winner |
      |-------|--------|--------------|--------|--------------|--------|
      | 1     | **A**      | 35 (4)       | **B**      | 32 (4)       | **A**      |
      | 2     | **C**      | 28 (4)       | **A**      | 30 (3.3)     | **A**      |
      | 3     | **B**      | 45 (4)       | **C**      | 38 (4)       | **B**      |
      | 4     | **A**      | 19 (3)       | **B**      | 20 (2.3)     | **B**      |
      | 5     | **A**      | 26 (3.2)     | **C**      | 27 (3.4)     | **C**      |
  - After 5 matches, the Points Table will look like this:
      | Team  | Matches | Points | Runs Given | Balls Bowled | Runs Scored | Balls Faced | NRR      |
      |-------|---------|--------|------------|--------------|-------------|--------------|-----------|
      | team2 | 3       | 4      | 92         | 66           | 97          | 63           | 0.145743  |
      | team1 | 4       | 4      | 107        | 88           | 110         | 83           | 0.109392  |
      | team3 | 3       | 2      | 101        | 65           | 93          | 70           | -0.225275 |

    **NOTE: (team1 is A, team2 is B, team3 is C)**
  - Now, its the final match of the round and its between **team2** and **team3**.
  - **team3 must win the match** to achieve 4 points in the Overall Points Table.
  - team2 has won the toss and have opted to bat first and they scored 25 in 3.4 overs, team3 needs to score 26 in 4 overs to win the match.
  - But, **just winning doesn't guarantee their spot to the Top 2**.
  - So, how many balls should they take to achieve the target in order to cement their place in the Top2?
  - [This file](https://github.com/RahulRoy-rsp/Mine_Algorithms/blob/main/NET%20RUN%20RATE/2ndInningsNRR.ipynb) gives us the solution for the above problem.
