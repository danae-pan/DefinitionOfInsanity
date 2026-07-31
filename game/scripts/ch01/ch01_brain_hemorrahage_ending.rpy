label ch01_brain_hemorrahage_ending:

    "He hesitates after hearing Kazuki's offer." 

    octor "The herbs in Kazuki's shop could be exactly what I need."

    doctor "Ingredients the hospital cannot provide..."

    doctor "But Mother called for me."

    doctor "No matter how important my research is..."

    doctor "I can't ignore her."

    doctor "\"Thank you, Kazuki.\""

    doctor "\"I'll visit your shop another time.\""

    "He quickly returns inside."

    "He opens the door."

    doctor "\"Mother?\""

    "..." 

    "There is no answer." 

    if ch01_brain_hemorrhage_happened :

        doctor "\"Oh no...\""
        doctor "\"Is this happening again?\""

    "Her breathing is uneven."

    "Her face is pale."

    "She looks exhausted."

    doctor "\"Mother...\""

    "He immediately checks her condition."

    if not ch01_brain_hemorrhage_happened:

        "Then he notices something."

        "A broken glass lies on the floor."

        "Water has spilled across the room."

        "The bottle beside her bed is empty."

        "..."

        doctor "She needed water."

        doctor "She tried to get it herself."

        doctor "While I was speaking with Kazuki..."

        doctor "She tried to stand."

        doctor "Her weakened body couldn't support her."

        doctor "She fell."

        doctor "Unable to call for help, she forced herself back into bed."

    else :

        doctor "It's the same scene as before..."

        doctor "The broken glass..."

        doctor "The empty bottle..."

    "He places his hands on her."

    "His medical training takes over."

    "He checks every possible sign, searching for any chance to help her."

    doctor "But deep down..."

    doctor "I already know."

    $ brain_hemorrhage_entry.locked = False

    doctor "The fall caused severe damage."

    doctor "A {a=glossary:brain_hemorrhage_entry}brain hemorrhage{/a}."

    if ch01_brain_hemorrhage_happened:

        doctor "\"Exactly like last time...\""

    "The hours pass slowly."

    "He remains beside her and tries everything he can."

    "But her condition continues to worsen."

    "Until finally..."

    "She is gone."

    "He holds Mother's hand."

    if not ch01_met_herb_in_door:

        doctor "I came back."

        doctor "I answered her call."

        doctor "I was here."

        doctor "And yet..."

        doctor "\"I still couldn't save you.\""

    if ch01_loop_count == 0:
    
        "Eventually, reality begins to settle in."

        "There are things that must be done."

        doctor "I have to report her death."

        doctor "I have to prepare her body."

        doctor "I have to tell someone."

        $ wake_entry.locked = False

        "He will have to arrange a {a=glossary:wake_entry}wake{/a}."

        if not ch01_wake_happened:

            $ ch01_wake_happened = True

    else :

        doctor "If I get another chance..."

        doctor "I won't repeat this."

        doctor "I will save her."

        scene black

        "He closes his eyes."

        doctor "\"Tomorrow...\""

        doctor "\"I'll do better.\""

    if not ch01_brain_hemorrhage_happened:

        $ ch01_brain_hemorrhage_happened = True

    call ch01_pass_to_chapter_2

    if ch01_jump_to_chapter_2 :

        jump ch02_start

    else :

        jump ch01_new_loop