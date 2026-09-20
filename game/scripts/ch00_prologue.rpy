image bg game_main = "gui/main_menu.png"
image prologue overlay = "gui/prologue.png"

define narrator_nvl = Character(None, kind=nvl, what_style="nvl_dialogue")

label prologue:

    $ old_text_cps = preferences.text_cps
    $ preferences.text_cps = 14
    $ matsushita_entry.locked = False
    $ nervous_system_entry.locked = False
    $ social_stigma_entry.locked = False
    $ poisoning_entry.locked = False
    $ kampo_entry.locked = False
    window hide

    scene bg game_main
    show prologue overlay
    with fade

    nvl clear

    narrator_nvl """
1956
{a=glossary:matsushita_entry}Matsushita{/a}
{vspace=35}
For many years, a mysterious illness had plagued the quiet coastal town of Matsushita.{w=1.2}
{vspace=35}
It began with subtle symptoms: numbness in the hands and feet, loss of sensation, and difficulty maintaining balance.{w=1.2}
{vspace=30}
As the illness progressed, it slowly destroyed the {a=glossary:nervous_system_entry}nervous system{/a}, leaving its victims unable to control their bodies.{w=1.2}
{vspace=30}
In its final stages, it could lead to paralysis, coma... or even complete mental deterioration.{w=1.2}
{vspace=30}
Fear spread throughout the town."""

    nvl clear

    narrator_nvl """

Believing the illness to be contagious, many residents avoided those who had fallen ill. {w=1.2}
{vspace=30}
Families became isolated, and the disease carried a heavy {a=glossary:social_stigma_entry}social stigma{/a}.{w=1.2}
{vspace=30}
Among the victims was Dr. Yosuke's Mother.{w=1.2}
{vspace=30}
Her symptoms had first appeared more than fifteen years earlier, growing steadily worse with each passing year.{w=1.2}
{vspace=30}
In 1930, Yosuke left Matsushita to study medicine in the capital.{w=1.2}
{vspace=30}
Whenever he was able, he returned home to care for his Mother, doing everything he could to ease her suffering.{w=1.2}
{vspace=30}"""
    nvl clear

    narrator_nvl """
Years later, researchers finally uncovered an important clue.
{vspace=30}
The illness was linked to {a=glossary:poisoning_entry}poisoning{/a} caused by consuming contaminated fish.{w=1.2}
{vspace=30}
Without hesitation, Yosuke returned to Matsushita for good. {w=1.2}
{vspace=30}
He removed seafood from his Mother's diet and accepted a position at the town's small hospital, where the growing number of patients had overwhelmed the remaining physicians. {w=1.2}
{vspace=30}
The discovery proved that the illness was not contagious, yet the stigma remained.{w=1.2}
{vspace=30}
Although patients were now treated with greater compassion, many townspeople still feared approaching them.{w=1.2}
{vspace=30}"""
    nvl clear

    narrator_nvl """
Fishing was the heart of Matsushita's economy, and generations of families had depended on the waters of Matsushita Bay for their livelihood.{w=1.2}
{vspace=30}
To many, believing the sea itself had become dangerous was simply unthinkable.{w=1.2}
{vspace=30}
So, they simply refused to accept that fish could be responsible.{w=1.2}
{vspace=30}
With his Mother's condition worsening by the day and the number of patients continuing to rise, Yosuke devoted himself to a single goal.{w=1.2}
{vspace=30}
Modern medicine offered no way to reverse the damage that had already been done.{w=1.2}
{vspace=30}"""
    nvl clear

    narrator_nvl """

Desperate for another approach, Yosuke turned to {a=glossary:kampo_entry}Kampo{/a} medicine, searching for a way to support the body's own ability to recover.{w=1.2}
{vspace=30}
His research eventually led him to an old manuscript describing a treatment that went beyond accepted medical practice.{w=1.2}
{vspace=30}
The damage could not simply be undone... but perhaps the nervous system could adapt.{w=1.2}
{vspace=30}
If healthy neural pathways could compensate for those that had been lost, perhaps the body could learn to function again.{w=1.2}
{vspace=30}
It was only a theory.
{vspace=30}
And Yosuke intended to test it.
{vspace=30}
"""
    nvl clear

    narrator_nvl """
He had only one goal.
{vspace=30}
To find a cure...
{vspace=30}
...before time ran out.
"""

    nvl clear

    hide prologue overlay

    $ preferences.text_cps = old_text_cps

    jump ch01_start