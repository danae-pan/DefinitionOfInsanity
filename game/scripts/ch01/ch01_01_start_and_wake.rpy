label ch01_start:

    scene black 
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
    $ ch01_went_to_shop = False
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

    "A new day begins... Once again, reality hits me."

    "Mother is suffering from an illness for which no cure has yet been found." 

    "I came back to help her survive, and the only way I can do that is by finding the cure myself."

    "Years of study and scientific experimentation have led me to several possible treatments that could save her, but I still don't know which one is the right one."

    "I have to keep testing formulas."

    "My stomach hurts... I probably didn't eat yesterday."

    "I don't even notice how the hours pass anymore, caught between endless experiments and taking care of Mother."

    "Maybe I should check if she's awake first."

    return

label ch01_loop_wakeup:

    "I open my eyes."

    if ch01_loop_count == 1:

        "All my life i wished this day will never come…"

        "My body feels heavy. My mind feels even heavier." 

        "Mother is gone."

    else: 

        "I feel so confused… memories are coming though my head"
    
    "All comes back…"

    call ch01_remember_previous_deaths

    "I have so much to do… i cannot hide any more.."

    "She is in the room… I could go see her.. "

    "My stomach hurts... I probably didn't eat yesterday."
    
    return

label ch01_remember_previous_deaths:

    if ch01_wake_happened:

        "The otsuya… The neighbors..."
        
    if ch01_brain_hemorrhage_happened:

        "The broken glass in the floor... Mother fell off her bed..."
    
    if ch01_knows_arrhythmia:

        "I gave her the formula... Licorice root... It caused her arrythmia..."

    if ch01_knows_coma :

        "I didn't gave her the formula... She died from coma..."

    return