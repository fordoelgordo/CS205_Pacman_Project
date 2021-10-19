# CS205 Pacman Project
Ford St. John 862125078
Matthew Duc Nguyen

## Question 1
#### Screenshots of successful runs:
```python
python pacman.py -l tinyMaze -p SearchAgent
```
![Q1_tinymaze_success](https://user-images.githubusercontent.com/11414055/138003625-cc982f44-3af3-443b-a755-cea5e05249af.png)
```python
python pacman.py -l mediumMaze -p SearchAgent
```
![](https://user-images.githubusercontent.com/11414055/138004166-03f9bafc-165d-4180-8d42-380ad06d5925.png)
```bash
$ python pacman.py -l mediumMaze -p SearchAgent
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 130 in 0.0 seconds
Search nodes expanded: 144
Pacman emerges victorious! Score: 380
Average Score: 380.0     
Scores:        380.0     
Win Rate:      1/1 (1.00)
Record:        Win  
```
```python
python pacman.py -l bigMaze -z .5 -p SearchAgent
```
![Q1_bigmaze_success](https://user-images.githubusercontent.com/11414055/138004726-fd081c22-98a3-47ec-afe6-f932f5084540.png)
#### Answers to questions posted in ![Question 1](http://ai.berkeley.edu/search.html#Q1):
The exploration of the board using DFS is slightly surprising in that in general, PacMan searches along the desired parth, ignoring a series of states (e.g. positions on the board) that would never lead him to the goal state.  The return from DFS is the path Pacman must take to reach the goal state, so he does not actually move to the explored states on his path to the goal, although the board provides an overlay of the states that were explored.

DFS provides a sub-optimal solution (e.g. not the shortest path), in that it returns the "first" path it encounters that reaches the goal state.  If this path is at the very bottom of the search tree, but happens to be the first path explored, then this path is returned, regardless of the path depth. 

## Question 2
#### Screenshots of successful runs:
```python
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```
![Q2_mediummaze_success](https://user-images.githubusercontent.com/11414055/138005250-bc1097b9-b5d6-40ef-af6c-342890d63b8b.png)
```bash
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
[SearchAgent] using function bfs
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 68 in 0.0 seconds
Search nodes expanded: 269
Pacman emerges victorious! Score: 442
Average Score: 442.0     
Scores:        442.0     
Win Rate:      1/1 (1.00)
Record:        Win     
```
```python
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```
![Q2_bigmaze_success](https://user-images.githubusercontent.com/11414055/138005394-d79821e8-9f27-400d-b7a9-4bb9fcd20dee.png)
