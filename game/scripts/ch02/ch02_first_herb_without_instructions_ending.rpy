label ch02_first_herb_without_instructions_ending:

    hide doctor default at left onlayer portraits with dissolve

    "The doctor grips the medicine bottle tightly."

    show doctor default at left onlayer portraits with dissolve

    doctor "I don't have time to prepare a meal."

    doctor "Every minute I wait is another minute the poison spreads."

    hide doctor default at left onlayer portraits with dissolve

    scene black with fade

    "He hurries upstairs."

    scene bg ch01 mother with fade

    "His mother looks up weakly as he enters."

    mother "\"My son...\""

    "He kneels beside the bed."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"I've prepared a new medicine.\""

    doctor "\"I need you to drink this.\""

    hide doctor default onlayer portraits with dissolve

    "He carefully helps her sit upright and raises the bottle to her lips."

    "She drinks without hesitation."

    "For a few moments..."

    "Nothing happens."

    "The doctor quietly observes her breathing."

    show doctor default at left onlayer portraits with dissolve

    doctor "Perhaps this was the right decision."

    hide doctor default onlayer portraits with dissolve

    "Then she suddenly clutches her stomach."

    "A painful groan escapes her lips."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Mother?\""

    hide doctor default onlayer portraits with dissolve

    "Without warning, she begins vomiting violently."

    "The doctor reaches forward to support her."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Easy... easy...\""

    hide doctor default onlayer portraits with dissolve

    "She tries to cough."

    "Instead, she chokes."

    "The vomit enters her airway."

    if knows_dysphagia :

        "Her weakened swallowing reflex cannot protect her."

        show doctor default at left onlayer portraits with dissolve

        doctor "Her swallowing..."

        doctor "Of course."

        $ dysphagia_entry.locked = False

        doctor "{a=glossary:dysphagia_entry}Dysphagia{/a}."

        doctor "How could I forget? It's a symptom of the disease."

        hide doctor default onlayer portraits with dissolve

        $ knows_dysphagia = True

    "She gasps desperately for air."

    "The doctor quickly turns her onto her side, desperately trying to clear her airway."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"Come on...\""

    doctor "\"Breathe!\""

    hide doctor default onlayer portraits with dissolve

    "Her struggles become weaker."

    "Then..."

    "They stop."

    "Silence fills the room."

    "The doctor slowly removes his trembling hands."

    "He stares at the floor."
    
    "Broken pieces of the medicine bottle his mother threw."

    if ch02_first_herb_with_instructions :

        show doctor default at left onlayer portraits

        doctor "\"...but why?\""

        hide doctor default onlayer portraits

        doctor "I tried before by following the instructions."

        doctor "..and I was too late."

        doctor "I thought skipping the dinner would buy us some time.."

        doctor "..I thought this decision would save her."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"...I should have listened.\""

    hide doctor default onlayer portraits with dissolve

    "For a long moment, he remains kneeling beside the bed."

    "Unable to accept what has happened."

    "Finally, he reaches for the bedsheet."

    "He gently pulls it over his mother's face."

    show doctor default at left onlayer portraits with dissolve

    doctor "\"...I'm sorry.\""

    hide doctor default onlayer portraits with dissolve

    "He fetches a cloth and a bucket of water."

    "Without thinking, he begins cleaning the floor."

    "The stains."

    "The shattered bottle."

    show doctor default at left onlayer portraits with dissolve

    doctor "But maybe, just maybe, the day repeats itself again."

    doctor "Maybe tomorrow I will get another chance."

    if ch02_first_herb_with_instructions :

        doctor "If I do..I should make sure to cook dinner early in the morning."

        doctor "That way, I won’t lose time during the day."

    hide doctor default onlayer portraits with dissolve

    scene black with fade

    "His legs carry him back to the laboratory almost on their own."

    scene bg ch01 lab with fade 

    "The books remain open exactly where he had left them."

    "He sits heavily at the workbench."

    "He turns another page."

    "He reads the instructions again."

    "Searching for something he had overlooked."

    show doctor default at left onlayer portraits with dissolve

    doctor "Perhaps I should have studied the herb more thoroughly..."

    doctor "Understood why it said to be taken after eating…"

    hide doctor default onlayer portraits with dissolve

    "He begins writing new observations beneath his previous notes."

    "Possible interactions."

    "Alternative preparations."

    "His handwriting grows slower."

    scene black with fade

    "His eyes become heavy."

    "Still staring at the open manuscript with his head resting on the workbench.."

    "..he falls asleep."

    $ ch02_first_herb_without_instructions = True

    $ ch02_previous_death = "first_herb_without_instructions"

    jump ch02_new_loop