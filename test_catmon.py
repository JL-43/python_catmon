from catmon import Catmon, Move


def test_attack_and_heal():
    tackle = Move("tackle", 5, "physical", "Normal")
    fireball = Move("fireball", 10, "special", "Fire")
    heal = Move("heal", 3, "heal", "Normal")

    mugi = Catmon("mugi", "Fire", 100, 100, [tackle, fireball, heal], 10, 10, 15, 10, 5)
    buwie = Catmon("buwie", "Water", 100, 100, [tackle, heal], 10, 10, 10, 15, 4)

    print("----")
    mugi.display_stats()
    print("----")
    buwie.display_stats()

    # Test attack
    print("----")
    mugi.use_move(buwie, tackle)
    # assert buwie.health == 95

    print("----")
    print(f"mugi: {mugi.health}")
    print("----")
    print(f"buwie: {buwie.health}")

    # Test fireball
    print("----")
    mugi.use_move(buwie, fireball)
    # assert buwie.health == 95

    print("----")
    print(f"mugi: {mugi.health}")
    print("----")
    print(f"buwie: {buwie.health}")

    # Test heal
    print("----")
    buwie.use_move(mugi, heal)
    # assert buwie.health == 98

    print("----")
    print(f"mugi: {mugi.health}")
    print("----")
    print(f"buwie: {buwie.health}")
