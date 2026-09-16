label ch01_pass_to_chapter_2:

    if met_herbalist and ch01_check_formula :

        if ch01_loop_count == 0:

            $ chapter_1_with_one_try = True

        #temp for testing
        $ ch01_jump_to_chapter_2 = True

    return