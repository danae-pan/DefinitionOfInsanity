style glossary_hyperlink_text:
    color "#801C1C"
    hover_color "#402814"
    underline True

init python:

    def glossary_link_style(target):
        return style.glossary_hyperlink_text

    def glossary_link_clicked(target):
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
                renpy.show_screen("glossary_tooltip", entry=entry)
                renpy.restart_interaction()


    glossary = Encyclopaedia(name="Dictionary")

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