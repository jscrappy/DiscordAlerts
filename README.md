# DiscordAlerts
Run a command on a Linux machine to output text to a discord channel or DM.

To install the executable, while in the directory, use `sh install.sh`

This command installs by default to /usr/bin. To run it, use `dca`.

To start messaging channels, you must specify a token, the channel you want to send it to, and then the message.
Putting a "c" before each channel ID denotes that it is a channel ID.

`dca token cChannelID Message`

You can specify multiple channels and messages, simply repeat with a new channel ID and message

`dca token cChannelID Message cChannelID2 Message2`

DMs are currently not supported, but will be supported soon. 
Currently, you must specify the Token on every request.
