# MCLightningFarmer
A small concept and code I created for a server with my friends.

## How it works
A tamed cat is struck by lightning when a thunderstorm starts and a chat message is displayed to the server when it dies. The script reads your minecraft log file and stops the server (only if you have permissions) or closes your singleplayer world when it reads this message. Then when the world/server is restarted, you will have lightning, meaning you can afk overnight and have a storm in the morning. It does NOT increase the speed at which storms are generated.

## Usage
You need:

- A tamed cat ontop of a lightning rod
- A python install
- The module pyautogui
> pip install pyautogui

Note: Your log file persists even when your chat is cleared. Restart your game before using a second time to clear the old message or the script will continue trying to disconnect you if you rerun it.

## Config
The program uses the default path your vanilla minecraft log file. If you are using a different launcher, you will need to configure this.
Singleplayer is enabled by default. It can be disabled by changing the variable singleplayer to False (only works if you have server permissions)

## Sorry kitty
![image](https://github.com/user-attachments/assets/f66a8485-cafd-4865-8963-1bdc32ae8aa1)
