**Task:**

You are an expert in video games and gamer culture. I am building a trivia game where players guess the video game based on a funny, exaggerated, or painfully accurate 1-star or 5-star app store/play store review.

I need you to generate a new level for my game containing 15 popular video games and automatically write the files to my project.

**Rules for the Game Reviews:**
- Write a funny or relatable fake review that perfectly describes the game's mechanics, player base, or overall vibe (e.g., "I just spent 4 hours crushing candies, and my mom keeps sending me lives on Facebook." for Candy Crush Saga, or "Kept running on train tracks and eventually hit a wall. Great game." for Subway Surfers).
- Do NOT mention the game title or main character names in the review.
- Make sure the games are very famous and recognizable to gamers.

**Execution Steps (Follow exactly in order):**

1. **Determine the next album name:** Look at `guess_game_data/allLevelDetails_v2.json`. Find the last "Game Reviews" album (e.g., "Game Reviews 1") and increment the number to create the new album name (e.g., "Game Reviews 2"). If it doesn't exist yet, start with "Game Reviews 1".
2. **Update `allLevelDetails_v2.json`:** Append a new JSON object for this new album to the end of the array. Use this exact structure:
```json
{
    "name": "[New Album Name]",
    "lvls": [Number of levels],
    "cost": 150,
    "star": null,
    "is_text": true,
    "cover": 0,
    "type": "Game Reviews",
    "des": "Guess the game from its funny store review"
}
```
3. **Create the Folder:** Create a new directory at `guess_game_data/[New Album Name]/`.
4. **Write `units.json`:** Generate an array of 15 video game names (ALL CAPS) and write it to `guess_game_data/[New Album Name]/units.json`:
```json
[
  "POKEMON GO",
  "Among Us",
  "MARIO KART TOUR",
  ...
]
```
5. **Write `questions.json`:** Generate an array of 15 game reviews matching the exact order of `units.json`, and write it to `guess_game_data/[New Album Name]/questions.json`.

Please proceed with generating and writing the files!
