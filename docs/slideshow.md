
# How not to lose at tic tac toe

Michael Gracie

October 2018

---
## Have you ever lost?

<div class="image12">
    <div style="float:left;margin-right:5px;">
        <img src="img/loss.png" height="200"/>
    </div>
    <div style="float:left;margin-right:5px;">
        <img class="middle-img" src="img/sad.png"/ height="200"/>
</div>

---

## Apply game theory to beat your friends at games


![Rage](https://media.giphy.com/media/s0FsE5TsEF8g8/giphy.gif)

Lets use **tic tac toe** as an example

---

## Basics of concepts of a game

- *Agent* - The people making decisions within a game
- *State* - Information about who's decision it is within the game
- *Payoff* - The reward the agent receives for winning the game

---

## Minimax Algorithm

Minimax is an algorithm that you can apply to two player *zero-sum* games with *perfect information*. Within the game you have


<div class="image12">
    <div style="float:left;margin-right:5px;">
        <img src="https://media.giphy.com/media/D2LspqlvLIXK0/giphy.gif" height="200"/>
    <p style="text-align:center;">Maximizer</p>
    </div>
    <div style="float:left;margin-right:5px;">
        <img class="middle-img" src="https://i.pinimg.com/originals/6c/e4/45/6ce445a5b3d6bc9217963ce2402f49f7.gif"/ height="200" width="200"/>
    <p style="text-align:center;">Minimizer</p>
</div>


The maximizer is assumed to make optimal moves to maximizer their payoff. The minimizer is assumed to make optimal moves to minimize the payoff of the maximizer.

---

## Implementation looks like this


<img src="img/minimax.png" height="300"/>


---

## In pseudo-code

```python
def minimax(game, maximizingPlayer):
    if game.done:
        return payoff
    if maximizingPlayer:
        value = −∞
        for move in game:
            value = max(value, minimax(move(game), FALSE))
        return value
    else:
        value = +∞
        for move in game:
            value = min(value, minimax(move(game), True))
        return value
```

---

## Alpha Beta Pruning

>  Implementation that stops searching a branch when a worse payoff is guaranteed

![pruning](https://media.geeksforgeeks.org/wp-content/uploads/MIN_MAX3.jpg)

---

## What else is there

- **Expectiminimax** - `Minimax` with chance included
- **Multi Agent Utilit** - A game where we assume each agent wants to maximize their payoff
- **Monte Carlo Tree Search** - Algorithim specializing in complex trees

---

## Camelup

> This is the game I modelled to beat my friends in

<img src="img/game_screen.png" height="300"/>


`https://github.com/michael-gracie/camelup`
