# CHAPTER 2 - ENDING

label ch02_ending:

    scene bg ch01 lab_no_cat with fade

    "He wakes up in a daze."

    show doctor default at left onlayer portraits with dissolve

    doctor "I've seen Mother die so many times now..."

    doctor "I don't know how many more chances I'll get."

    doctor "But this time..."

    doctor "I'm sure I'm on the right track."

    doctor "All those failed attempts weren't for nothing..."

    doctor "Each one brought me closer to the solution."

    hide doctor default onlayer portraits with dissolve

    "He had found what was missing."

    "The herbalist's remedies offered possibilities he had never considered before."

    "He tried them."

    "He learned from his mistakes."

    "He followed the instructions."

    "And still..."

    "He was too late."

    show doctor default at left onlayer portraits with dissolve

    doctor "The treatment isn't enough."

    doctor "Even when I know what to do, I can't reach her in time."

    hide doctor default onlayer portraits with dissolve

    "He looks at the clock."

    show doctor default at left onlayer portraits with dissolve

    doctor "I know what's going to happen now."

    doctor "I know what I need to do."

    doctor "So maybe..."

    doctor "\"I just need to be faster.\""

    hide doctor default onlayer portraits with dissolve

    jump ch02_final_card

label ch02_final_card:

    $ old_text_cps = preferences.text_cps
    $ preferences.text_cps = 28

    window hide

    scene bg game_main
    show prologue overlay
    with fade

    nvl clear

    narrator_nvl "{b}You found the missing piece.{/b}"

    narrator_nvl "{b}But now, you're against the clock.{/b}"

    narrator_nvl "Knowing how to save her means nothing\nif you can't act fast enough."

    narrator_nvl "{b}Can you stay one step ahead\nand save your Mother before time runs out?{/b}"

    narrator_nvl "{b}Find out in Chapter 3.{/b}"

    pause 1.5

    nvl clear

    $ preferences.text_cps = old_text_cps

    scene black with Dissolve(1.5)

    pause 1.0

    $ renpy.full_restart()