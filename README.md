# Dream Game

A CLI board game inspired by a dream, developed in a single sitting upon waking up.

## Overview

Dream Game is a turn-based command-line interface (CLI) race game where players compete to reach the end of a customizable board. Built entirely in Python, the game incorporates dynamic board sizing, flexible dice configurations, immersive audio feedback, and rules directly translated from a dream sequence.

## Features

- **Customizable Gameplay Rules:** Dynamically adjust the number of players (1-4), dice count, and total board blocks before launching a session.
- **Realistic Turn Behaviors:** Implements a fallback "bounce back" system if a player overshoots the final block, requiring an exact landing to win.
- **Competitive Interaction Mechanics:** Landing on an opponent's occupied tile instantly punishes them by sending their piece back to the starting block.
- **Integrated Audio Engine:** Background music tracks and reactive sound effects play concurrently during menu navigation, rolling states, and penalty events.
- **Formatted Terminal Interface:** Styled with `colorama` to provide distinct colors for inputs, rule screens, and individual player indicators directly within the console.

## Tech Stack

- **Core Engine:** Python 3
- **Terminal Styling:** Colorama
- **Audio Output:** Internal sound execution libraries (via customized `AudioManager`)

## Project Structure

```bash
dream-game/
├── assets/
│   ├── music/       # Background soundtracks
│   └── sounds/      # Multi-event action sound effects
├── utils/
│   ├── audio_manager.py
│   ├── dice.py
│   ├── game.py
│   └── player.py
├── .gitignore
├── README.md
└── start.py         # Main game execution file
```

## Installation

- git clone https://github.com

- Install required terminal dependencies: `pip install -r requirements.txt`

- Ensure your local audio drivers are accessible for runtime `.mp3` playback

- Launch the game script: `python start.py`

## Author

H2SO4-1191 – Software Engineer
