from catmon import Catmon, Move


def test_attack_and_heal():
    tackle = Move("tackle", 5, "normal", "attack")
    heal = Move("heal", 3, "normal", "heal")

    mugi = Catmon("mugi", "fire", 100, 100, [tackle, heal])
    buwie = Catmon("buwie", "water", 100, 100, [tackle, heal])

    print("----")
    mugi.display_stats()
    print("----")
    buwie.display_stats()

    # Test attack
    print("----")
    mugi.use_move(buwie, tackle)
    assert buwie.health == 95

    print("----")
    print(f"mugi: {mugi.health}")
    print("----")
    print(f"buwie: {buwie.health}")

    # Test heal
    print("----")
    buwie.use_move(mugi, heal)
    assert buwie.health == 98

    print("----")
    print(f"mugi: {mugi.health}")
    print("----")
    print(f"buwie: {buwie.health}")
