# Ban Purchase Bots - Streamlabs Twitch bot script

This package contains a script for the Streamlabs chatbot that can
automatically ban the annoying bots that make you want to buy viewers and
followers. It currently has a configurable list of textboxes that can be filled
with common sentences they use in order to automatically ban them.

## Installation

In order to download the latest version of this script, go to the 
(releases of this package)[https://github.com/mfrankruijter/BanPurchaseBots/releases/latest] 
and click on the `Source code (zip)` button. This will download the codebase 
of the script. Unpack this ZIP. Go into the unpacked folder, there should be a 
`README.md` file. In that same folder there should be a `BanPurchaseBots` 
folder. This folder should be zipped again. On Windows 10 the following steps
can be done: 
- Right click on the folder.
- Open the menu, copy to.
- Click on the Zipped folder option.

The resulting ZIP is the package that needs to be imported in the following 
step.

In order to use this script, Python (2.7) must be installed on the same system
that the bot is running on. For the exact documentation please see
[the original documentation](https://cdn.streamlabs.com/chatbot/Documentation_Twitch.pdf)
Import the ZIP file from this repository under the `Scripts` section of your
chatbot. If the scripts section is not available, try to reconnect
`Twitch Streamer` and `Twitch Bot` under the connection tab, under the profile
icon in the bottom left corner.

## Usage

When the script is installed, click on the entry in the scripts tab and fill in
the common sentences the bots are using. When filling in these sentences, use
lowercase, without carets etc. and the same punctuation. The script will decode
all unicode characters to their respective letters. E.g. `é` will become `e`
when the script interprets it.

In the info panel of the script, a log will be kept of all ban actions taken 
with a reason.

## Feedback

Feedback for this package can be provided through issues, or by creating a pull
request with a fix or improvement.

## References

- [StreamLabs Chatbot](https://streamlabs.com/chatbot)
- [Unidecode](https://pypi.org/project/Unidecode/)