# Treasure Hunt — Python Console Game

A beginner-friendly console game where you must find hidden treasures on a grid while avoiding traps — all in limited moves.

---

## How to Play

- You are the **Player (P)** starting at position `(0, 0)`
- Move using:
  - `W` = up
  - `A` = left
  - `S` = down
  - `D` = right
- The grid is 10x10:
  - You must find **5 treasures (T)**
  - Avoid **5 traps (X)**
  - Win by finding all treasures before running out of **20 moves**

---

## Game Features

- Random placement of treasures and traps
- Tracks player movement and prevents wall hits
- Real-time board rendering (showing only visited cells)
- Win/Lose conditions
- Fully object-oriented Python implementation

---

## Run the Game

```bash
cd TreasureHunt
python3 treasure_hunt.py
