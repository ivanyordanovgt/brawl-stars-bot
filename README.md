# Tutorial 
Download at https://discord.gg/pylaai

### Only 1920x1080!
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
Start it and press the middle button on the top right (Which maximizes the window). Do not press F11, tabs on the bottom left should be visible.

### How to start
1. Write the name of the brawler and click on the autocomplete to select it
2. Write your goal of trophies
3. Click "set"
4. After you've done that for all the brawlers you want **Open brawl stars**
5. After you are in the brawl stars lobby, click start and don't touch anything else

### How to use for 5v5 horizontal maps (vertical are same as 3v3)
Go into the folder cfg, open the file game_mode.toml with any text editor. Change the "type" to 3 or 5.<br>
- 3 For vertical
- 5 for horizontal


### Key setup
1. "e" on super the super button
2. "q" on the middle of "play" btn

### Only masteries
If you want the bot to only farm masteries on only one brawler, select your brawler the usual way and select the trophy count to be 799. The bot will never reach those trophies on that brawler so it will farm masteries only for it.

### How to stop the bot
Move your mouse to any corner of the screen and the bot will stop.

### Auto login
Go into ./cfg folder and into login.toml and add your key to the "key" value. Example:
```key = "testkey123"```

# Common errors
If the bot doesn't click correctly on the brawlers button or other things do the following:
1. Go into cfg folder
2. Open lobby_config.toml with any text editor you want
3. Edit the coords with the correct ones for your case.
Coords are in format ```[x1, y1]``` and ```[x1, y1, x2, y2]```<br><br>

How to find coords:
[VIDEO](https://www.youtube.com/watch?v=EgZSjCiKvIQ)
### Example
The bot clicks above the brawlers button. Here is what you do:
Edit ```brawlers_btn = [130, 450]```. Since it clicks above, increase y1 value to go down. 
