# PortUpdater
Updates port from ProtonVPN to qBitTorrent
*Only tested on Windows*

You will need to install "qBitTorrent Cli" found here on GitHub:
https://github.com/fedarovich/qbittorrent-cli

Inside the script, update the two locations where I've left a comment.
You may need to call qbt from the cli & set your username, password & server IP
Follow his own guide for this and you'll be golden: https://github.com/fedarovich/qbittorrent-cli/wiki/Getting-Started

I just setup task manager to run the script every hour while the PC is idle, so whenever
the port is updated it should only be an hour at most before the script is run, and updated in the client.

No this script isn't pretty, and may break under some conditions. But it's
been working for me without fail for quite a while. I just jumbled this together from random documentation pages.
Fight me.
