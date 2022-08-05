################### Scope ####################
#* global scope 
enemies = 1
#? local scope
def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#* Python does not have block scope
# game_level = 3
# nme = ['skeleton', 'zombie', 'alien']
# if game_level < 5:
#     new_nme = nme[0]

#? OK - if block is not scoped 
# print(new_nme)

def create_enemy():
    game_level = 3
    nme = ['skeleton', 'zombie', 'alien']
    if game_level < 5:
        new_nme = nme[0]

#! NOPE - function has local scope
print(new_nme)