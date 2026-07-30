label ch02_try_different_herb :

    scene bg ch01 lab 

    doctor "I should not lose time. I need a different herb now."

    $ ch02_checked_mother = False
    $ ch02_route_choice = "try_herb"

    menu:
        "Go to the herbalist":
            jump ch02_go_to_herbalist

        "Go to the hospital":
            jump ch02_go_to_hospital
    
    return