**Task:**

You are an expert in video games and gamer culture. I am building a trivia game where players guess the video game based on the desperate, funny, or weird Google search history of a frustrated player.

I need you to generate a new level for my game containing 15 popular video games and automatically write the files to my project.

**Rules for the Search History:**
- Write a sequence of 2-3 funny Google searches that a player of this game would absolutely make (e.g., "How to cure zombie villager", "Why did a green thing blow up my house?" for Minecraft, or "How to pay off raccoon debt" for Animal Crossing).
- Do NOT mention the game title in the search history.
- Make sure the games are very famous and recognizable to gamers.

**Execution Steps (Follow exactly in order):**

1. **Determine the next album name:** Look at `guess_game_data/allLevelDetails_v2.json`. Find the last "Gamer Search History" album (e.g., "Gamer Search History 1") and increment the number to create the new album name (e.g., "Gamer Search History 2"). If it doesn't exist yet, start with "Gamer Search History 1".
2. **Update `allLevelDetails_v2.json`:** Append a new JSON object for this new album to the end of the array. Use this exact structure:
```json
{
    "name": "[New Album Name]",
    "lvls": [Number of levels],
    "cost": 150,
    "star": null,
    "is_text": true,
    "cover": 0,
    "type": "Gamer Search History",
    "des": "Guess the game from the player's search history"
}
```
3. **Create the Folder:** Create a new directory at `guess_game_data/[New Album Name]/`.
4. **Write `units.json`:** Generate an array of 15 video game names (ALL CAPS) and write it to `guess_game_data/[New Album Name]/units.json`:
```json
[
  [
    "how to cure zombie villager",
    "why did a green thing blow up my house",
    "is herobrine real"
  ],
  [
    "how to pay off raccoon debt",
    "can I evict an ugly neighbor",
    "turnip prices calculator"
  ]
]
```
5. **Write `questions.json`:** Generate an array of 15 search histories matching the exact order of `units.json`, and write it to `guess_game_data/[New Album Name]/questions.json`.

Please proceed with generating and writing the files!
