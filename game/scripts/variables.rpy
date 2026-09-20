image bg ch01 kitchen = im.Scale("images/backgrounds/kitchen_background.png", 1920, 1080)
#image bg ch01 mother = im.Scale("images/backgrounds/mother_background.png", 1920, 1080)
image bg ch01 lab = im.Scale("images/backgrounds/lab_background.png", 1920, 1080)
image bg ch01 herbstore = im.Scale("images/backgrounds/herbstore_background.png", 1920, 1080)
image bg ch01 hospital = im.Scale("images/backgrounds/hospital_background.png", 1920, 1080)
image bg ch01 lab_no_cat = im.Scale("images/backgrounds/labwithoutcat_background.png", 1920,1080)
image chapter_1_title = "gui/chapter_one.png"
image chapter_2_title = "gui/chapter_two.png"

##Expressions

layeredimage doctor:

    always:
        "images/characters/doctor_base.png"

    group expression:
        attribute default default:
            "images/characters/doctor_default.png"

        attribute worried:
            "images/characters/doctor_worried.png"

        attribute panicked:
            "images/characters/doctor_panicked.png"

        attribute smile:
            "images/characters/doctor_smile.png"

layeredimage mother:

    always:
        "images/characters/mother_base.png"

    group expression:
        attribute default default:
            "images/characters/mother_default.png"

        attribute smile:
            "images/characters/mother_smile.png"

        attribute sick:
            "images/characters/mother_sick.png"

layeredimage herbalist:

    always:
        "images/characters/herbalist_base.png"

    group expression:

        attribute default default:
            Fixed(
                "images/characters/herbalist_default_face.png",
                "images/characters/herbalist_hair_front.png",
                "images/characters/herbalist_default_eyebrows.png",
                xysize=(411, 473)
            )

        attribute smile:
            Fixed(
                "images/characters/herbalist_smile_face.png",
                "images/characters/herbalist_hair_front.png",
                "images/characters/herbalist_smile_eyebrows.png",
                xysize=(411, 473)
            )

        attribute sceptical:
            Fixed(
                "images/characters/herbalist_sceptical_face.png",
                "images/characters/herbalist_hair_front.png",
                "images/characters/herbalist_sceptical_eyebrows.png",
                xysize=(411, 473)
            )




default took_herbs = False
default chapter_1_with_one_try = False
default met_herbalist = False
default kept_cat_in_lab_once = False # chapters's 2 noisy pet
default knows_dysphagia = False
