from catmon import Catmon, Move


def test_attack_and_heal():
    tackle = Move("tackle", 5, "physical", "Normal")
    fireball = Move("fireball", 10, "special", "Fire")
    heal = Move("heal", 3, "heal", "Normal")

    mugi = Catmon("mugi", "Fire", 100, 100, [tackle, fireball, heal], 10, 10, 15, 10, 5)
    buwie = Catmon("buwie", "Grass", 100, 100, [tackle, heal], 10, 10, 10, 15, 4)

    # Test attack
    mugi.use_move(buwie, tackle)
    # assert buwie.health == 95

    # Test fireball
    mugi.use_move(buwie, fireball)
    # assert buwie.health == 95

    # Test heal
    buwie.use_move(mugi, heal)
    # assert buwie.health == 98
