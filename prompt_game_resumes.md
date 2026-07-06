**Task:**

You are an expert in video games and gamer culture. I am building a trivia game where players guess the video game based on a hilarious in-universe resume or job description of the main character.

I need you to generate a new level for my game containing 15 popular video games and automatically write the files to my project.

**Rules for the Resumes:**
- Write a short, funny job description or resume summary for the main character (e.g., "Skills include: Punching trees with bare hands, building mansions out of dirt, and surviving explosive green monsters." for Minecraft, or "Lawyer. Excellent at pointing fingers aggressively, screaming 'OBJECTION!', and cross-examining parrots." for Phoenix Wright: Ace Attorney).
- Do NOT mention the game title or the character's exact name.
- Make sure the games are very famous and recognizable to gamers.

**Execution Steps (Follow exactly in order):**

1. **Determine the next album name:** Look at `guess_game_data/allLevelDetails_v2.json`. Find the last "Game Resumes" album (e.g., "Game Resumes 1") and increment the number to create the new album name (e.g., "Game Resumes 2"). If it doesn't exist yet, start with "Game Resumes 1".
2. **Update `allLevelDetails_v2.json`:** Append a new JSON object for this new album to the end of the array. Use this exact structure:
```json
{
    "name": "[New Album Name]",
    "lvls": [Number of levels],
    "cost": 150,
    "star": null,
    "is_text": true,
    "cover": 0,
    "type": "Game Resumes",
    "des": "Guess the game from the character's resume"
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
5. **Write `questions.json`:** Generate an array of 15 resume summaries matching the exact order of `units.json`, and write it to `guess_game_data/[New Album Name]/questions.json`.

Please proceed with generating and writing the files!
