# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    play music "audio/music/deep server.mp3" fadeout 2.0 fadein 2.0

    jump prologue