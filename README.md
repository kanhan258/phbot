pybotgram
=========


[![](https://travis-ci.org/rockneurotiko/pybotgram.svg?branch=master)](https://travis-ci.org/rockneurotiko/pybotgram)

A Telegram Bot written in Python with plugins based in [yagop telegram-bot](https://github.com/yagop/telegram-bot) using [tg](https://github.com/vysheng/tg)


State
----------

Currently the bot is in development, feel free to contribute, it would be really appreciated!


Plugins
---------


| Name | Description | Usage |
| ---- | ----------- | ----- |
| calc.py | A calculator to evaluate expressions | !calc (expression) |
| channels.py | Plugin to manage channels.<br>Enable or disable channel. | !channel enable: enable current channel<br>!channel disable: disable current channel |
| clever.py | Cleverbot plugin. | !clever (text): Say the text to cleverbot and receive the answer |
| download_media.py | When bot receives a media msg, download the media to the file system. | This plugin is automatic when someone send a file. |
| echo.py | Simplest plugin ever! | !echo (text) |
| help.py | Help plugin.<br>Get info from other plugins. | !help: Show list of plugins.<br>!help all: Show all commands for every plugin.<br>!help [plugin name]: Commands for that plugin. |
| imgtosticker.py | Convert a photo to sticker! | !imgtosticker start: Next photo you send, as image or document, it will try to convert to sticker and send you.<br>!imgtosticker stop: Stop the service, won't convert the next image.<br>If you are in "start" mode, send a photo as document or image, and get the sticker! |
| media.py | When user sends media URL (ends with gif, mp4, pdf, etc.) download and send it to origin. | This plugin is automatic when you send an URL. |
| money.py | Currency converter | !money (from currency) (amount) (to currency) |
| plugins.py | Plugin to manage other plugins<br>Enable, disable or reload. | !plugins: list all plugins.<br>!plugins enable [plugin]: enable plugin.<br>!plugins disable [plugin]: disable plugin.<br>!plugins disable [plugin] chat: disable plugin only this chat.<br>!plugins reload: reloads all plugins. |


Installation
---------

In order to install it, you need some system dependencies.

- tg dependencies:
```
# Tested on Ubuntu 14.04, for other OSs check out https://github.com/vysheng/tg#installation
sudo apt-get install libreadline-dev libconfig-dev libssl-dev lua5.2 liblua5.2-dev libevent-dev libjansson-dev libpython-dev make
```

- bot dependencies:
```
sudo apt-get install git python3 libpython3-dev python-pip python3-pip
sudo pip3 install virtualenv
```

- Optional dependencies:
If you want to have all the plugins, you will have to install some more dependencies:
```
sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev
./launch.sh optdeps
```

To install in other OS, see this are the libraries that need extra dependencies:
- [https://pypi.python.org/pypi/Pillow/2.1.0](https://pypi.python.org/pypi/Pillow/2.1.0)

Plugins that you'll can't use if you don't install this optional dependencies:
- `imgtosticker`: Use PIL (pillow)



Once you have all dependencies, and the optional if you want, install the bot and run it:

- bot:
```
cd $HOME
git clone https://github.com/rockneurotiko/pybotgram/
cd pybotgram
./launch.sh install
./launch.sh # Will ask you for a phone number & confirmation code
# (The number is like +cc00000000 where cc is the country code)
```


Enable more [`plugins`](https://github.com/rockneurotiko/pybotgram/tree/master/plugins)
-------------
See the plugins list with `!plugins` command.

Enable a disabled plugin by `!plugins enable [name]`.

Disable an enabled plugin by `!plugins disable [name]`.

Those commands require a privileged user, privileged users are defined inside `data/config.json` (generated by the bot), stop de bot and edit if necessary.

The privileged users are identified with his telegram ID, and you can write all you want in `data/config.json`, in the list `sudo_users`, like this:
```
"sudo_users": [00000000, 11111111, 22222222, 33333333]
```

Contact me
------------
You can contact me [via Telegram](https://telegram.me/rock_neurotiko) but if you have an issue please [open](https://github.com/rockneurotiko/pybotgram/issues) one.
