
## How not to lose at tic tac toe

Michael Gracie

October 2019

---

### Apply game theory to beat your friends!


![Rage](https://media.giphy.com/media/s0FsE5TsEF8g8/giphy.gif)

---

### Basics of concepts of a game

- *Agent* - The people making decisions within a game
- *State* - Information about who's decision it is within the game
- *Payoff* - The reward the agent receives for winning the game

---

### Minimax Algorithm

Minimax is an algorithm that you can apply to two player *zero-sum* games with *perfect information*. Within the game you have a:

| Maximizer     | Minimizer    |
| :-------------: | :-------------: |
| Assumed to make optimal moves to maximizer their payoff | Assumed to make optimal moves to minimize the payoff of the maximizer |
|<img src="https://media.giphy.com/media/D2LspqlvLIXK0/giphy.gif" height="100"/>|<img src="https://i.pinimg.com/originals/6c/e4/45/6ce445a5b3d6bc9217963ce2402f49f7.gif" height="100"/>|

---

### Implementation looks like this


<img src="img/minimax.png" height="500"/>


---

### In pseudo-code

```python
def minimax(game, maximizingPlayer):
    if game.done:
        return payoff
    if maximizingPlayer:
        value = -10000
        for move in game:
            value = max(value, minimax(move(game), FALSE))
        return value
    else:
        value = 10000
        for move in game:
            value = min(value, minimax(move(game), True))
        return value
```

---

### Alpha Beta Pruning

>  Implementation that stops searching a branch when a worse payoff is guaranteed

![pruning](https://media.geeksforgeeks.org/wp-content/uploads/MIN_MAX3.jpg)

---

### What else is there

- **Expectiminimax** - `Minimax` with chance included
- **Multi Agent Utility** - A game where we assume each agent wants to maximize their payoff
- **Monte Carlo Tree Search** - Pruning algorithm specializing in complex trees

---

### Camelup

This is the game I modelled to beat my friends in

<img src="img/game_screen.png" height="300"/>

###### `https://github.com/michael-gracie/camelup`
