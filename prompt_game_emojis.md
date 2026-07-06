**Task:**

You are an expert in video games and emoji puzzles. I am building a trivia game where players guess the video game based entirely on a sequence of emojis representing its title, mechanics, or plot.

I need you to generate a new level for my game containing 15 popular video games and automatically write the files to my project.

**Rules for the Emoji Puzzles:**
- Use a sequence of 3 to 5 emojis to represent the game (e.g., ⛏️ 🟩 🧟‍♂️ 💎 for Minecraft, or 🚗 💨 🚓 💰 for Grand Theft Auto).
- The question must ONLY contain emojis. Do NOT include any text, letters, or numbers.
- Make sure the emojis cleverly but clearly point to a very famous and recognizable video game.

**Execution Steps (Follow exactly in order):**

1. **Determine the next album name:** Look at `guess_game_data/allLevelDetails_v2.json`. Find the last "Game Emojis" album (e.g., "Game Emojis 1") and increment the number to create the new album name (e.g., "Game Emojis 2"). If it doesn't exist yet, start with "Game Emojis 1".
2. **Update `allLevelDetails_v2.json`:** Append a new JSON object for this new album to the end of the array. Use this exact structure:
```json
{
    "name": "[New Album Name]",
    "lvls": [Number of levels],
    "cost": 150,
    "star": null,
    "is_text": true,
    "cover": 0,
    "type": "Game Emojis",
    "des": "Guess the game from the emojis"
}
```
3. **Create the Folder:** Create a new directory at `guess_game_data/[New Album Name]/`.
4. **Write `units.json`:** Generate an array of 15 video game names (ALL CAPS) and write it to `guess_game_data/[New Album Name]/units.json`:
```json
[
  "Candy Crush Saga",
  "PUBG Mobile",
  "Minecraft",
  "Temple Run",
  ...
]
```
5. **Write `questions.json`:** Generate an array of 15 emoji sequences matching the exact order of `units.json`, and write it to `guess_game_data/[New Album Name]/questions.json`.

Please proceed with generating and writing the files!
