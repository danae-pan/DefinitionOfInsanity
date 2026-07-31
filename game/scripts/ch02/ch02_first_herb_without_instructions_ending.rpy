label ch02_first_herb_without_instructions_ending:

    "The doctor grips the medicine bottle tightly."

    doctor "I don't have time to prepare a meal."

    doctor "Every minute I wait is another minute the poison spreads."

    "He hurries upstairs."

    "His mother looks up weakly as he enters"

    mother "\"My son...\""

    "He kneels beside the bed."

    show doctor default at left onlayer portraits

    doctor "\"I've prepared a new medicine.\""

    doctor "\"I need you to drink this.\""

    hide doctor default onlayer portraits

    "He carefully helps her sit upright and raises the bottle to her lips."

    "She drinks without hesitation."

    "For a few moments..."

    "Nothing happens."

    "The doctor quietly observes her breathing."

    "Perhaps this was the right decision."

    "Then she suddenly clutches her stomach."

    "A painful groan escapes her lips."

    show doctor default at left onlayer portraits

    doctor "\"Mother?\""

    hide doctor default onlayer portraits

    "Without warning, she begins vomiting violently."

    "The doctor reaches forward to support her."

    show doctor default at left onlayer portraits

    doctor "\"Easy... easy...\""

    hide doctor default onlayer portraits

    "She tries to cough."

    "Instead, she chokes."

    "The vomit enters her airway."

    if knows_dysphagia :

        "Her weakened swallowing reflex cannot protect her."

        show doctor default at left onlayer portraits

        doctor "\"Not again…\""

        hide doctor default onlayer portraits

        "He recalls that {a=glossary:dysphagia_entry}dysphagia{/a} caused her to choke while eating bread before."

        "Fear starts to fill up."

    "She gasps desperately for air."

    "The doctor quickly turns her onto her side, desperately trying to clear her airway."

    show doctor default at left onlayer portraits

    doctor "\"Come on...\""

    doctor "\"Breathe!\""

    hide doctor default onlayer portraits

    "Her struggles become weaker."

    "Then..."

    "They stop."

    "Silence fills the room."

    "The doctor slowly removes his trembling hands."

    "He stares at the empty medicine bottle."

    if ch02_first_herb_with_instructions :

        show doctor default at left onlayer portraits

        doctor "\"...but why?\""

        hide doctor default onlayer portraits

        doctor "I tried before by following the instructions."

        doctor "..and I was too late."

        doctor "I thought skipping the dinner would buy us some time.."

        doctor "..I thought this decision would save her."

    show doctor default at left onlayer portraits

    doctor "\"...I should have listened.\""

    hide doctor default onlayer portraits

    "For a long moment, he remains kneeling beside the bed."

    "Unable to accept what has happened."

    "Finally, he reaches for the bedsheet."

    "He gently pulls it over his mother's face."

    show doctor default at left onlayer portraits

    doctor "\"...I'm sorry.\""

    hide doctor default onlayer portraits

    "He fetches a cloth and a bucket of water."

    "Without thinking, he begins cleaning the floor."

    "The stains."

    "The shattered bottle."

    doctor "But maybe, just maybe, the day repeats itself again."

    doctor "Maybe tomorrow I will get another chance."

    if ch02_first_herb_with_instructions :

        doctor "If I do..I should make sure to cook dinner early in the morning."

        doctor "That way, I won’t lose time during the day."

    scene bg ch01 lab with fade 

    "His legs carry him back to the laboratory almost on their own."

    "The books remain open exactly where he had left them."

    "He sits heavily at the workbench."

    "He turns another page."

    "He reads the instructions again."

    "Searching for something he had overlooked."

    doctor "Perhaps I should have studied the herb more thoroughly..."

    doctor "Understood why it said to be taken after eating…"

    "He begins writing new observations beneath his previous notes."

    "Possible interactions."

    "Alternative preparations."

    "His handwriting grows slower."

    "His eyes become heavy."

    "Still staring at the open manuscript with his head resting on the workbench.."

    "..he falls asleep."

    $ ch02_first_herb_without_instructions = True

    jump ch02_start