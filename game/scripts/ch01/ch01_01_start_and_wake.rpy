image bg lab = "images/backgrounds/lab_background.png"

label ch01_start:

    scene bg lab
    with fade

    jump ch01_wake_up

label ch01_new_loop:

    $ ch01_loop_count += 1

    call ch01_reset_attempt_state

    jump ch01_start

label ch01_reset_attempt_state:

    # Reset choices/actions from the previous attempt.
    $ ch01_breakfast_made = False
    $ ch01_bread_added = False
    $ ch01_mother_checked = False
    $ ch01_cat_in_lab = False
    $ ch01_formula_finished = False
    $ ch01_met_herb_in_door = False
    $ ch01_met_herb_in_hospital = False
    $ herbalist_visited = False
    $ ch01_cat_broke_formula = False
    $ ch01_prepared_formula = False

    return

# Event Wake UP
# Choices
#   Make Breakfast 
#   Check on Mother
label ch01_wake_up:

    if ch01_loop_count == 0:

        call ch01_first_wakeup
        
    else:

        call ch01_loop_wakeup
        
    menu:

        "Make breakfast":

            "I should make breakfast."
            
            jump ch01_make_breakfast

        "Check on your mother":
            
            jump ch01_check_mother

label ch01_first_wakeup:

    "A new day begins... and Dr Yosuke wakes up."

    doctor "Once again reality hits me."

    "His mother is suffering from a mysterious illness, one for which medicine has yet to discover a cure."

    doctor "I came back to help her survive, and the only way I can do that is by finding the cure myself."

    "Years of study and countless experiments have brought him closer to several possible treatments."

    doctor "One of these formulas has to work."

    doctor "I just have to keep testing."

    "A sharp pain twists his stomach."

    doctor "I probably didn't eat yesterday..."

    "The days have begun to blur together. Endless hours spent moving between the laboratory and his mother's bedside have made him lose all sense of time."

    doctor "I should see if Mother is awake."

    return

label ch01_loop_wakeup:

    "He slowly opens his eyes."

    if ch01_loop_count == 1:

        "For his entire life, he wished this day would never come."

        "His body feels heavy. His mind feels even heavier."

        "His mother is dead."

    else: 

        "He wakes in confusion."

        "Fragments of memories rush through his mind."
    
    "Then everything comes back to him."

    call ch01_remember_previous_deaths

    doctor "There's no time to dwell on it."

    doctor "I have too much to do."

    doctor "She is in the room… I could go see her.. "

    "A dull pain twists his stomach."

    doctor "I probably didn't eat yesterday."

    return

label ch01_remember_previous_deaths:

    if ch01_wake_happened:

        doctor "The otsuya… The neighbors..."
        
    if ch01_brain_hemorrhage_happened:

        doctor "The broken glass in the floor... Mother fell off her bed..."
    
    if ch01_knows_arrhythmia:

        doctor "I gave her the formula... Licorice root... It caused her arrythmia..."

    if ch01_knows_coma :

        doctor "I didn't gave her the formula... She died from coma..."

    return