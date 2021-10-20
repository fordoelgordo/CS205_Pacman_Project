# CS205 Pacman Project
Ford St. John 862125078<br/>
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
#### Answers to questions posted in [Question 1](http://ai.berkeley.edu/search.html#Q1):
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


## Question 3
#### Screenshots of successful runs:
```python
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```
![Q3_mediummaze_success](https://user-images.githubusercontent.com/11414055/138021564-0b30f2c7-7a64-4d11-8fb2-0f39a0a3d4a2.png)
```bash
$ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
[SearchAgent] using function ucs
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
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
```
![Q3_mediumdottedmaze_success](https://user-images.githubusercontent.com/11414055/138021789-9146d8e4-7b14-412e-ac58-736a50183597.png)
```bash
$ python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
Path found with total cost of 1 in 0.0 seconds
Search nodes expanded: 186
Pacman emerges victorious! Score: 646
Average Score: 646.0     
Scores:        646.0     
Win Rate:      1/1 (1.00)
Record:        Win 
```
```python
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```
![Q3_mediumscarymaze_success](https://user-images.githubusercontent.com/11414055/138021994-34bbaae3-b872-4526-a22a-83d33d32aef9.png)
```bash
$ python pacman.py -l mediumScaryMaze -p StayWestSearchAgent --frameTime 0
Path found with total cost of 68719479864 in 0.0 seconds
Search nodes expanded: 108
Pacman emerges victorious! Score: 418
Average Score: 418.0
Scores:        418.0     
Win Rate:      1/1 (1.00)
Record:        Win 
```

## Question 4
#### Screenshots of successful runs:
```python
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
![Q4_bigmaze_success](https://user-images.githubusercontent.com/11414055/138022285-d200b3c7-e1a0-4930-8d9d-72c1ae895f88.png)

