image bg game_main = "gui/main_menu.png"
image prologue overlay = "gui/prologue.png"

define narrator_nvl = Character(None, kind=nvl, what_style="nvl_dialogue")

label prologue:

    $ old_text_cps = preferences.text_cps
    $ preferences.text_cps = 14
    window hide

    scene bg game_main
    show prologue overlay
    with fade

    nvl clear

    narrator_nvl """
1956
Matsushita
{vspace=35}
For many years, a mysterious illness had plagued the quiet coastal town of Matsushita.{w=1.2}
{vspace=35}
It began with subtle symptoms: numbness in the hands and feet, loss of sensation, and difficulty maintaining balance.{w=1.2}
{vspace=30}
As the illness progressed, it slowly destroyed the nervous system, leaving its victims unable to control their bodies.{w=1.2}
{vspace=30}
In its final stages, it could lead to paralysis, coma... or even complete mental deterioration.{w=1.2}
{vspace=30}
Fear spread throughout the town."""

    nvl clear

    narrator_nvl """

Believing the illness to be contagious, many residents avoided those who had fallen ill. {w=1.2}
{vspace=30}
Families became isolated, and the disease carried a heavy social stigma.{w=1.2}
{vspace=30}
Among the victims was Dr. Yosuke's mother.{w=1.2}
{vspace=30}
Her symptoms had first appeared more than fifteen years earlier, growing steadily worse with each passing year.{w=1.2}
{vspace=30}
In 1930, Yosuke left Matsushita to study medicine in the capital.{w=1.2}
{vspace=30}
Whenever he was able, he returned home to care for his mother, doing everything he could to ease her suffering.{w=1.2}
{vspace=30}"""
    nvl clear

    narrator_nvl """
Years later, researchers finally uncovered an important clue.
{vspace=30}
The illness was linked to the consumption of contaminated fish.{w=1.2}
{vspace=30}
Without hesitation, Yosuke returned to Matsushita for good. {w=1.2}
{vspace=30}
He removed seafood from his mother's diet and accepted a position at the town's small hospital, where the growing number of patients had overwhelmed the remaining physicians. {w=1.2}
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
With his mother's condition worsening by the day and the number of patients continuing to rise, Yosuke devoted himself to a single goal.{w=1.2}
{vspace=30}
To find a cure...
{vspace=30}
...before time ran out.
"""

    nvl clear
    hide prologue overlay
    jump ch01_start