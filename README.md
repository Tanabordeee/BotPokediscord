# Pokebot README

## Overview

Pokebot is a Discord bot designed to "poke" users in voice channels by moving them to different voice channels and back a specified number of times. This bot allows you to call the command `/poke` to move a user between two channels repeatedly and `/stoppoke` to stop the action. It is a fun way to interact with members on your server.

## Features

- Move a user between voice channels for a set number of rounds.
- Option to stop the poke action anytime using the `/stoppoke` command.
- Error handling if a user isn't in a voice channel or the bot encounters an issue.

## Requirements

- Python 3.8 or higher
- Discord.py library (`discord.py==2.0.0`)
- A Discord bot token

## Installation

1. **Clone the repository** or copy the code into your project.

2. **Install dependencies**:
   If you're setting up a virtual environment, run the following commands:

   ```bash
   pip install discord.py
   ```

3. **Set up the bot token**:
   - Obtain your bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
   - Store the bot token in an `.env` file or set it as an environment variable. The bot expects the token to be in the environment as `DISCORD_TOKEN`.

4. **Run the bot**:
   To start the bot, simply run the following command:

   ```bash
   python bot.py
   ```

## Commands

### `/poke <member> <channel> <rounds>`
Moves the specified member to the provided voice channel for the specified number of rounds. The bot will move the member back to their original channel after each round.

**Parameters**:
- `member`: The Discord member you want to poke.
- `channel`: The voice channel you want to move the member to.
- `rounds`: The number of times to move the member between channels.

**Example**:
```/poke @User #general 5```
This will move `@User` to `#general` five times and then back to their original channel.

### `/stoppoke`
Stops any ongoing poke action and prevents the bot from moving members.

**Example**:
```/stoppoke```
This will stop any ongoing poking action immediately.

## How it Works

- The `/poke` command starts a loop where the bot moves the target user to a given voice channel and back to their original channel.
- The bot will repeat this action the specified number of times (rounds).
- If you want to stop the action before it finishes, you can use the `/stoppoke` command.

## Contributing

Feel free to fork this repository and submit issues and pull requests if you find bugs or want to add features.

## License

This project is licensed under the MIT License.
