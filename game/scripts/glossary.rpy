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
            Matsushita is a quiet coastal town whose economy depends heavily
            on fishing and Matsushita Bay.
        """),
        locked=True
    )


    # --------------------------------------------------
    # Traditions
    # --------------------------------------------------

    wake_entry = EncEntry(
        parent=glossary,
        name="Wake",
        subject="Traditions",
        text=enc_utils.text_block("""\
            An overnight vigil held before a funeral. In 1950s Japan, wakes
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
        name="Kampō",
        subject="Medicine",
        text=enc_utils.text_block("""\
            Japan's traditional system of herbal medicine. Derived from
            ancient Chinese medicine and adapted to Japanese culture, Kampō
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
            principles of Kampō medicine.
        """),
        locked=True
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