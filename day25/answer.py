val = 1
card_subject = 7
card_key = 12320657
card_loop_count = 0
while val != card_key:
    val = val * card_subject % 20201227
    card_loop_count += 1
print(card_subject, card_loop_count)

val = 1
door_subject = card_subject
door_loop_count = 0
door_key = 9659666
while val != door_key:
    val = val * door_subject % 20201227
    door_loop_count += 1    

print(door_loop_count)

card_subject = door_key
val = 1
while card_loop_count > 0:
    val = val * card_subject % 20201227
    card_loop_count -= 1

print(val)