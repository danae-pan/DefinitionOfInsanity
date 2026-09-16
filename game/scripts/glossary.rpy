style glossary_hyperlink_text:
    color "#801C1C"
    hover_color "#402814"
    underline True


init python:

    # --------------------------------------------------
    # Hyperlink behaviour
    # --------------------------------------------------

    def glossary_link_style(target):
        return style.glossary_hyperlink_text


    def glossary_link_clicked(target):
        # Glossary links only display the tooltip on hover.
        return None


    def glossary_link_focus(target):

        if target is None:
            renpy.hide_screen("glossary_tooltip")
            renpy.restart_interaction()
            return

        if target.startswith("glossary:"):
            entry_name = target.split(":", 1)[1]
            entry = getattr(store, entry_name, None)

            if entry is not None:
                renpy.show_screen(
                    "glossary_tooltip",
                    entry=entry
                )
                renpy.restart_interaction()



    # --------------------------------------------------
    # Dictionary
    # --------------------------------------------------

    glossary = Encyclopaedia(name="Dictionary")


    # --------------------------------------------------
    # Places
    # --------------------------------------------------

    matsushita_entry = EncEntry(
        parent=glossary,
        name="Matsushita",
        subject="Places",
        text=enc_utils.text_block("""\
            Matsushita is a fictional coastal town whose economy depends heavily
            on fishing and Matsushita Bay. Its story and the illness affecting its
            residents are inspired by the real events surrounding Minamata disease
            in Japan.
        """),
        locked=True
    )


    # --------------------------------------------------
    # Traditions
    # --------------------------------------------------

    wake_entry = EncEntry(
        parent=glossary,
        name="Otsuya",
        subject="Traditions",
        text=enc_utils.text_block("""\
            An overnight wake held before a funeral. In 1950s Japan, wakes
            were usually held in the family home, where relatives, friends,
            and neighbors gathered to pay their respects and support the
            grieving family.
        """),
        locked=True
    )


    # --------------------------------------------------
    # Medicine
    # --------------------------------------------------

    kampo_entry = EncEntry(
        parent=glossary,
        name="Kampo",
        subject="Medicine",
        text=enc_utils.text_block("""\
            Japan's traditional system of herbal medicine. Derived from
            ancient Chinese medicine and adapted to Japanese culture, Kampo
            uses carefully selected herbal formulas to restore the body's
            overall balance rather than treating a single symptom.
        """),
        locked=True
    )


    formula_entry = EncEntry(
        parent=glossary,
        name="Formula",
        subject="Medicine",
        text=enc_utils.text_block("""\
            A combination of medicinal herbs prepared according to the
            principles of Kampo medicine.
        """),
        locked=False
    )


    decoction_entry = EncEntry(
        parent=glossary,
        name="Decoction",
        subject="Medicine",
        text=enc_utils.text_block("""\
            A medicinal liquid made by boiling herbs in water to extract
            their properties. Decoctions are commonly used to prepare herbal
            formulas.
        """),
        locked=True
    )


    # --------------------------------------------------
    # Symptoms
    # --------------------------------------------------

    dysphagia_entry = EncEntry(
        parent=glossary,
        name="Dysphagia",
        subject="Symptoms",
        text=enc_utils.text_block("""\
            A condition that makes swallowing difficult. It can occur as a
            symptom of neurological disorders and may cause choking while
            eating or drinking because food or liquids can enter the airway
            instead of the stomach.
        """),
        locked=True
    )


    # --------------------------------------------------
    # Fictional herbs
    # --------------------------------------------------

    taeru_root_entry = EncEntry(
        parent=glossary,
        name="Taeru Root",
        subject="Herbs",
        text=enc_utils.text_block("""\
            A medicinal root believed to improve endurance and reduce fatigue.
            This fictional herb is based on Panax Ginseng, a plant traditionally
            used in East Asian medicine.
        """),
        locked=True
    )


    hogo_root_entry = EncEntry(
        parent=glossary,
        name="Hogo Root",
        subject="Herbs",
        text=enc_utils.text_block("""\
            A medicinal root believed to support the nervous system and
            promote cognitive well-being. This fictional herb is based on
            Polygala tenuifolia, a plant traditionally used in East Asian
            medicine.
        """),
        locked=True
    )


    junka_root_entry = EncEntry(
        parent=glossary,
        name="Junka Root",
        subject="Herbs",
        text=enc_utils.text_block("""\
            A medicinal root believed to support healthy blood circulation
            and promote overall vitality. This fictional herb is based on
            Dong Quai, a plant traditionally used in East Asian medicine.
        """),
        locked=True
    )


    tsuyomi_cap_entry = EncEntry(
        parent=glossary,
        name="Tsuyomi Cap",
        subject="Herbs",
        text=enc_utils.text_block("""\
            A medicinal mushroom believed to strengthen the body's resilience
            and support overall well-being. This fictional herb is based on
            Ganoderma lucidum, a mushroom traditionally used in East Asian
            medicine.
        """),
        locked=True
    )


    ryoku_berry_entry = EncEntry(
        parent=glossary,
        name="Ryoku Berry",
        subject="Herbs",
        text=enc_utils.text_block("""\
            A medicinal berry believed to improve vitality and help the body
            adapt to physical and mental stress. This fictional herb is based
            on Schisandra chinensis, a plant traditionally used in East Asian
            medicine.
        """),
        locked=True
    )


    nagomi_root_entry = EncEntry(
        parent=glossary,
        name="Nagomi Root",
        subject="Herbs",
        text=enc_utils.text_block("""\
            A medicinal root believed to soothe inflammation and promote
            overall balance. This fictional herb is based on Licorice Root,
            a plant traditionally used in East Asian medicine.
        """),
        locked=True
    )
    # --------------------------------------------------
    # Medical Terms
    # --------------------------------------------------

    poisoning_entry = EncEntry(
        parent=glossary,
        name="Poisoning",
        subject="Medical Terms",
        text=enc_utils.text_block("""\
            A condition caused by exposure to a harmful substance that damages
            the body. Minamata disease, which inspired the illness in this story,
            was caused by methylmercury poisoning from contaminated seafood.
        """),
        locked=True
    )

    nervous_system_entry = EncEntry(
        parent=glossary,
        name="Nervous System",
        subject="Medical Terms",
        text=enc_utils.text_block("""\
            The network of the brain, spinal cord, and nerves that allows the
            body to move, feel sensations, and communicate between different
            parts of the body. Damage to the nervous system can affect
            movement, coordination, speech, sensation, and many other bodily
            functions.
        """),
        locked=True
    )


    anti_inflammatory_entry = EncEntry(
        parent=glossary,
        name="Anti-inflammatory",
        subject="Medical Terms",
        text=enc_utils.text_block("""\
            A substance that helps reduce inflammation, the body's natural
            response to injury or disease. Reducing inflammation may help
            relieve pain, swelling, and tissue damage.
        """),
        locked=True
    )

    brain_hemorrhage_entry = EncEntry(
    parent=glossary,
    name="Brain Hemorrhage",
    subject="Medical Terms",
    text=enc_utils.text_block("""\
        Bleeding within or around the brain caused by a ruptured blood
        vessel. It is a medical emergency that can damage brain tissue and
        may lead to permanent disability or death if not treated promptly.
    """),
    locked=True
    )

    arrhythmia_entry = EncEntry(
    parent=glossary,
    name="Arrhythmia",
    subject="Medical Terms",
    text=enc_utils.text_block("""\
        An abnormal heartbeat caused by changes in the heart's normal rhythm.
        The heart may beat too quickly, too slowly, or irregularly. Depending
        on the type and severity, an arrhythmia can cause dizziness, fainting,
        or become life-threatening.
    """),
    locked=True
    )

    coma_entry = EncEntry(
    parent=glossary,
    name="Coma",
    subject="Medical Terms",
    text=enc_utils.text_block("""\
        A prolonged state of unconsciousness in which a person cannot be
        awakened or respond to their surroundings. In severe neurological
        illnesses, a coma may occur as the brain can no longer function
        normally.
    """),
    locked=True
    )

    respiratory_failure_entry = EncEntry(
    parent=glossary,
    name="Respiratory Failure",
    subject="Medical Terms",
    text=enc_utils.text_block("""\
        A serious condition in which the body cannot get enough oxygen
        or properly remove carbon dioxide. In severe neurological illnesses,
        respiratory failure may occur when the nervous system can no longer
        properly control breathing.
    """),
    locked=True
    )

    cardiac_arrest_entry = EncEntry(
    parent=glossary,
    name="Cardiac Arrest",
    subject="Medical Terms",
    text=enc_utils.text_block("""\
        A sudden condition in which the heart stops beating effectively,
        preventing blood from reaching the brain and other vital organs.
        Without immediate treatment, cardiac arrest can quickly lead to
        unconsciousness and death.
    """),
    locked=True
    )




    # --------------------------------------------------
    # General Terms
    # --------------------------------------------------

    social_stigma_entry = EncEntry(
        parent=glossary,
        name="Social Stigma",
        subject="General Terms",
        text=enc_utils.text_block("""\
            Negative attitudes or prejudice directed toward people because
            of a particular condition or circumstance. During the real
            Minamata disease outbreak, many patients and their families faced
            discrimination because others feared the illness was contagious.
        """),
        locked=True
    )

    # --------------------------------------------------
    # Miscellaneous
    # --------------------------------------------------

    ajisai_entry = EncEntry(
        parent=glossary,
        name="Ajisai",
        subject="Miscellaneous",
        text=enc_utils.text_block("""\
            Ajisai is the Japanese name for hydrangea, a flowering plant
            commonly seen in Japan. It is known for its large clusters of
            flowers, which can appear in shades of blue, purple, pink, or white.
        """),
        locked=True
    )

    mrs_Sato_entry = EncEntry(
        parent=glossary,
        name="Mrs. Sato",
        subject="Miscellaneous",
        text=enc_utils.text_block("""\
            Mrs. Sato lives across from the Doctor's house and is a longtime friend of his mother. 
            She has been aware of her illness since the early stages and was one of the few villagers 
            who continued to support and help her despite the social stigma and fear surrounding her condition.
        """),
        locked=True
    )

    kimono_entry = EncEntry(
        parent=glossary,
        name="Kimono",
        subject="Miscellaneous",
        text=enc_utils.text_block("""\
            A traditional Japanese garment with long sleeves and a wrap-around
            design, usually secured with a wide belt called an obi. Kimono are
            worn on various occasions, with their style and formality depending
            on the event and the person wearing them.
        """),
        locked=True
    )