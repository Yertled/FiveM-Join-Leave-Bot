# FiveM Discord Bot

This is a Discord bot that interacts with a FiveM server. It provides a command to list the current players on the server and a task that checks the server for player joins and leaves every minute.

![image](https://github.com/Yertled/FiveM-Join-Leave-Bot/assets/12172847/34bb4615-ee9d-4494-931b-e9cb44c112ec)


## Features

- **Player List Command**: The `!playerlist` command lists the current players on the FiveM server. Only users with their IDs in the `allowed_user_ids` list can use this command.
- **Join/Leave Notifications**: The bot sends a message to a specified Discord channel whenever a player joins or leaves the FiveM server.
- **Player Count**: The bot's Discord Status updates every minute with the amount of players currently online on the server.

## Setup

1. **Discord Bot Token**: Replace the `bot_token` variable with your Discord Bot token.
2. **Discord Channel ID**: Replace the `join_leave_channel_id` variable with the ID of the Discord channel where you want the bot to send join/leave messages.
3. **Allowed User IDs**: Replace the `allowed_user_ids` list with the Discord User IDs that are allowed to use the `!playerlist` command.
4. **FiveM Server IP and Port**: Replace the `ip` and `port` variables with the IP and port of your FiveM server.

## Usage

Run the script and the bot will start. It will begin checking the FiveM server for player joins and leaves every minute. Users with their IDs in the `allowed_user_ids` list can use the `!playerlist` command to get a list of the current players on the server.

## Dependencies

- discord
- async-fivem

Please ensure you have these dependencies installed before running the bot. You can install them using pip:

```bash
pip install discord async-fivem
```

## Note

This bot uses the `async-fivem` Python package to interact with the FiveM server. 
https://github.com/makupi/async-fivem

Make sure your FiveM server is set up to allow connections from your bot. Also, ensure that your Discord bot has the necessary permissions to send messages to the specified channel. 

Remember to keep your bot token and other sensitive information secure. Do not share this information or publish it in a public repository. 

## License

This project is open source. You are free to modify and distribute it under the terms of the license provided. 

## Contributing

Contributions are welcome. Please open an issue or submit a pull request if you have any improvements or features you would like to see added. 

## Contact

If you have any questions or need further assistance, please open an issue and I will be happy to help. 


Enjoy using the bot!
