# LAB 3 - INFORMED SEARCH IN PAC-MAN
# Copy the command and run it in the terminal or command prompt

## Exercise 1

### With nullHeuristic:
```python
python pacman.py -l tinyMaze -p SearchAgent -a fn=befs
```

```python
python pacman.py -l mediumMaze -p SearchAgent -a fn=befs
```

```python
python pacman.py -l bigMaze -p SearchAgent -a fn=befs -z .5
```

### With manhattanHeuristic:
```python
python pacman.py -l tinyMaze -p SearchAgent -a fn=befs,heuristic=manhattanHeuristic
```

```python
python pacman.py -l mediumMaze -p SearchAgent -a fn=befs,heuristic=manhattanHeuristic
```

```python
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=befs,heuristic=manhattanHeuristic
```

## Exercise 2

### With nullHeuristic:
```python
python pacman.py -l tinyMaze -p SearchAgent -a fn=astar
```

```python
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar
```

```python
python pacman.py -l bigMaze -p SearchAgent -a fn=astar -z .5
```

### With manhattanHeuristic:
```python
python pacman.py -l tinyMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

```python
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

```python
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```