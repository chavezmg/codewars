#Kill the monsters!

def kill_monsters(health, monsters, damage):
    if (monsters % 3) == 0:
        hits = int(monsters/3)-1
    else:
        hits = int(monsters/3)
    dmg = int(hits * damage)
    hp = int(health - dmg)
    if hp <= 0:
        return "hero died"
    return f"hits: {hits}, damage: {dmg}, health: {hp}"

print(kill_monsters(10, 7, 5))