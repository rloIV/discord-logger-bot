# discord-logger-bot
A discord bot that logs most of the events happening on the discord server.

This bot tracks activities such as user joins, leaves, voice status changes, message activity, role changes, and more. It also provides an easy-to-use menu for selecting which events you want to log.

## Features

- **Log user activity**: Track events like user joins, leaves, message sends/deletes, and more.
- **Track voice status**: Log events such as voice channel joins, leaves, mutes, unmutes, deafens, and undeafens.
- **Role changes**: Track when roles are added or removed from members.
- **Nickname changes**: Keep track of when members change their nicknames.
- **Timeouts and bans**: Log ban, unban, kick, and timeout events.
- **Customizable logging**: Use a simple `/log` command to choose which events you want to log in a specific channel.
- **Image and file logging**: The bot will log when users send images, GIFs, and other media types.

## Installation

To install and run the bot, you need to have Python 3.8+ installed on your machine.

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rloIV/discord-logger-bot.git
    cd discord-logger-bot
    ```

2. **Set up your bot token**:
    - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    - Create a new bot and copy its token.
    - Create a `config.py` file in the root directory of the project with the following contents:
      ```python
      DISCORD_BOT_TOKEN = 'your-bot-token'
      APPLICATION_ID = 'your-application-id'
      ```

3. **Run the bot**

## Commands

- **`/log`**: Display a menu to select which events you want to log.
  - Options include: Join, Leave, Voice Join, Voice Leave, Message, Message Delete, Role Add, Role Remove, Nickname Change, Ban, Unban, Kick, Timeout, and more.

## Example Logs

When an event occurs, the bot will log it in the designated channel. Each log will include an embed with the details of the event and will be color-coded based on the event type.

