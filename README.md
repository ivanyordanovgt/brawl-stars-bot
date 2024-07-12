# Tutorial 
Download at https://discord.gg/pylaai

### Only 1920x1080 screen settings!
Make sure you are 1920x1080 in windows display settings.

### Only LDPLayer! Support for BlueStacks will be added in the following 2-3 days.

### Bot currently only works on the "ranged" playstyle
Which means it will be only able to play these brawlers:
```py
["8bit", "barley", "bea", "belle", "bo", "bonnie",
"brock","byron", "carl", "charlie", "colette",
"colt","crow", "penny", "piper","poco", "rico",
"rt", "ruffs","dynamike", "emz", "eve", "gale",
"gene","grom", "gray", "jessie", "larry_lawrie",
"leon","griff", "gus", "lola", "lou", "mandy", "maisie",
"mrp", "nani","otis", "pam", "spike", "sprout",
"stu", "squeak""tara", "tick", "willow"]
```
Ranges are defined in the file 
```
ranges.toml
```
If you experience the bot trying to shoot enemies too far or letting enemies getting to close, you can edit it with any text editor or message me.
Other playstyles are currently worked on!

### How LDPlayer should look
Start it and press the middle button on the top right (Which maximizes the window). Do not press F11, tabs on the top left should be visible. (so LDPlayer is fullscreen windowed)

### How to start
1. Click the brawler you want the bot to play
2. Select if you want it to farm mastery or trophies
3. Write the brawler current trophies and mastereis under "trophies" and "masteries
4. Write the goal for the brawler under "push until". If you have selected "trophies" at step 2 it will play till the amount of trophies given in "push until"
5. Open Brawl stars on LDPlayer, be in the lobby and click start on the bot menu. Do not move anything else from that point.

### How to use for 5v5 horizontal maps (vertical are same as 3v3)
Go into the folder cfg, open the file game_mode.toml with any text editor. Change the "type" to 3 or 5.<br>
- 3 For vertical
- 5 for horizontal
! Warning ! Some 5v5 maps are vertical like normal 3v3. They should be set to "3"


### Key setup
1. "e" on super the super button
2. "q" on the middle of "play" btn


### How to stop the bot
Move your mouse to any corner of the screen and the bot will stop.


# Common errors
If the bot doesn't click correctly on the brawlers button or other things do the following:
1. Go into cfg folder
2. Open lobby_config.toml with any text editor you want
3. Edit the coords with the correct ones for your case.
Coords are in format ```[x1, y1]``` and ```[x1, y1, x2, y2]```<br><br>

How to find coords:
[Tool download](https://www.mediafire.com/file/weq2zklef8h5hv8/Mofiki%2527s_Coordinate_Finder.zip/file) <br>
Video how to change coords:
[VIDEO](https://youtu.be/Pxo7WgfcvwM)
<br>
To change a region in format ```[x1, y1, x2, y2]```, get the coords for both corners of the region instead the center like in the video.

### Example
The bot clicks above the brawlers button. Here is what you do:
Edit ```brawlers_btn = [130, 450]```. Since it clicks above, increase y1 value to go down. 
