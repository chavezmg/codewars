#Holiday VI - Shark Pontoon
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    shark_time = shark_distance/shark_speed
    you_time = pontoon_distance/you_speed
    
    if shark_time < you_time:
        return "Shark Bait!"
    else:
        return "Alive!"