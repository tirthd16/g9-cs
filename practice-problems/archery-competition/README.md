# Archery Competition Program

The scores for each competitor in an archery competition are recorded.

- The one-dimensional (1D) array `CompetitorName[]` is used to store the names of the competitors.
- The maximum number of competitors is **30**.
- There are **10 rounds** in the competition with a maximum score of **30** per round.
- The two-dimensional (2D) array `CompetitorScore[][]` stores the score in each of the 10 rounds for each competitor.
- The first index of the array `CompetitorScore[][]` is the same as the index of the competitor in `CompetitorName[]`.

After the 10 rounds have been completed:

- The **highest** score and the **lowest** score for each competitor are discarded.
- The **overall score** for each competitor is the total of the remaining **8 scores** (after discarding the highest and lowest scores).

A competitor with:

- an overall score of **210 or more** moves onto the **next competition**
- an overall score between **180 and 209 inclusive** becomes a **reserve competitor**
- an overall score **below 180** does **not qualify**

## Write a program that meets the following requirements:

- Inputs the total score (out of 30) for each competitor in each round.
- Validates each input is between **0** and **30** inclusive.
- Calculates the overall score for each competitor, discarding the highest and lowest scores.
- Outputs the name of each competitor and whether they:
  - move onto the next competition
  - are a reserve competitor
  - do not qualify
- Calculates and outputs the number of competitors who:
  - have qualified for the next competition
  - are reserve competitors
  - do not qualify

## Additional Instructions

- You **must** use **pseudocode** or **program code**.
- Add **comments** to explain how your code works.
- You **do not** need to declare any arrays or variables; assume these have already been done.
- All inputs and outputs must contain suitable messages.
