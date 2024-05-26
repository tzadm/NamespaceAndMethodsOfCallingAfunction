def single_root_words(root_world, *other_words):
    same_words = []
    for i in other_words:
        if root_world in i:
            same_words.append(i)
        elif root_world not in i:
            root_world = root_world.lower()
            if root_world in i:
                same_words.append(i)
            elif root_world not in i:
                root_world = str(root_world[0]).upper() + str(root_world[1:])
                if root_world in i:
                    same_words.append(i)

    for i in other_words:
        if i in root_world:
            same_words.append(i)
        elif i not in root_world:
            i = str(i).lower()
            if i in root_world:
                same_words.append(i.title())
            elif i not in root_world:
                root_world = str(root_world).lower()
                if i in root_world:
                    same_words.append(i.title())

    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
