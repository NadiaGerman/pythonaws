# Quiz Quest - Professional Version

Welcome to the **Professional Version** of **Quiz Quest**!  
This version provides a clean, interactive, and user-friendly multiple-choice quiz experience.

---

##  Features

- **Multiple-Choice Questions**: Each question provides four possible answers.
- **Answer by Number**: Players select their answer by entering the number (1-4).
- **Category Selection**: Players choose a category (science, history, pop culture) by number, shortcut letter, or full name.
- **Input Validation**: 
  - Ensures users enter a valid answer number (1-4).
  - Retries if users enter an invalid category.
- **Scoring System**: Players earn points for each correct answer.
- **Leaderboard**: Displays players' scores at the end of each round.
- **Tie Handling**: If players tie, a tie is correctly announced with all winners congratulated.
- **Polished Interface**: Centered welcome title, clean round separation.

---

##  How to Play

1. **Register Players**: Enter player names (type `'done'` when finished).
2. **Category Selection**: 
   - Enter **number** (`1`, `2`, `3`), **letter** (`s`, `h`, `p`), or **full name** (`science`, `history`, `pop culture`).
3. **Answer Questions**: 
   - Each player gets a random multiple-choice question.
   - Enter the number of the correct answer (1-4).
4. **Rounds**: 
   - The game consists of 3 rounds.
5. **Winner Declaration**:
   - After 3 rounds, scores are displayed.
   - A winner (or winners if tied) is declared.

---

##  Available Categories

| Number | Shortcut | Full Name |
|:------:|:--------:|:---------:|
| 1 | s | science |
| 2 | h | history |
| 3 | p | pop culture |

---

##  How to Run

In your terminal, inside the project folder:

```bash
python3 quiz_quest_pro.py
