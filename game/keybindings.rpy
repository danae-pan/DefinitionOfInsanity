# ==================================================
# CUSTOM KEYBINDINGS
# ==================================================

init python:

    # Auto Mode
    config.keymap["toggle_afm"] = [ "K_a" ]

    # History
    config.keymap["open_history"] = [ "K_j" ]

    # Quick Save
    config.keymap["quick_save_custom"] = [ "K_F5" ]

    # Quick Load
    config.keymap["quick_load_custom"] = [ "K_F9" ]


screen custom_keybindings():

    key "open_history" action ShowMenu("history")

    key "quick_save_custom" action QuickSave()

    key "quick_load_custom" action QuickLoad()


init python:
    config.overlay_screens.append("custom_keybindings")