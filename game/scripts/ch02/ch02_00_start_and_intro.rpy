
default ch02_loop_count = 0

label ch02_start:

    call ch02_reset_runtime_state

    jump ch02_intro

    return

label ch02_reset_runtime_state:

    return

label ch02_intro:

    if chapter_1_with_one_try:

        "He wakes up in a daze. He cannot believe his mother is no more."

        doctor "How could I let this be? I don’t deserve to call myself a doctor."

        doctor "No time for this, I should prepare the death certificate and go to the municipality."
        
        doctor "But first, I should prepare my mother for the wake."

        "He heads to his mother’s room and for his surprise, find her alive."

        doctor "Wait a second, what? Am I in a dream?"

        "He slaps himself, pinch his arm and he feels the pain."

        doctor "Maybe yesterday was just a nightmare? Maybe mother never died."

        doctor "No way, I remember it clearly."

        doctor "This is an act of god, I should take advantage of this second chance to save her this time."
    
    else:

        "He wakes up in a daze. Slowly, everything comes back to him."

        "His mother might still be alive."

    "He is thinking he should run some tests to check whether everything is okey but maybe he shouldn’t lose time on this and instantly try a different herb and prepare a formula."

    menu :

        "Check on your mother":

            jump ch02_check_mother

        "Try a different herb":

            jump ch02_try_different_herb

    return