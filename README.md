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
    Make sure to create a new file named however you want that you will later run via `main.py` or other root file.

2. **Run the bot**

## Commands

- **`/log`**: Display a menu to select which events you want to log.
  - Options include: Join, Leave, Voice Join, Voice Leave, Message, Message Delete, Role Add, Role Remove, Nickname Change, Ban, Unban, Kick, Timeout, and more.

## Example Logs

When an event occurs, the bot will log it in the designated channel. Each log will include an embed with the details of the event and will be color-coded based on the event type.

- Message Event (Blue)
When a user sends a message, the bot will log it with a blue color.

**Event**: Message Sent  
**User**: @username  
**Message**: "Hello, world!"  
**Sent At**: 2024-10-01 14:50:00 UTC

`I'm currently working on the function to log all files the users share`
