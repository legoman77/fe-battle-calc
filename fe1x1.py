import colors as c
import random

def attack():
    global attacker_name
    global attacker_boss
    global attacker_class 
    global attacker_current_hp 
    global attacker_max_hp 
    global attacker_exp 
    global attacker_level 
    global attacker_strength
    global attacker_magic
    global attacker_skill
    global attacker_speed
    global attacker_luck
    global attacker_defense
    global attacker_resistance
    global attacker_weapon_type
    global attacker_weapon_uses
    global attacker_weapon_might
    global attacker_weapon_hit
    global attacker_weapon_crit
    global attacker_weapon_range
    global attacker_weapon_effect
    global attacker_hp_growth
    global attacker_strength_growth
    global attacker_magic_growth
    global attacker_skill_growth
    global attacker_speed_growth
    global attacker_luck_growth
    global attacker_defense_growth
    global attacker_resistance_growth
    global defender_name 
    global defender_boss 
    global defender_class
    global defender_current_hp 
    global defender_max_hp 
    global defender_exp 
    global defender_level 
    global defender_strength 
    global defender_magic 
    global defender_skill 
    global defender_speed 
    global defender_luck 
    global defender_defense 
    global defender_resistance 
    global defender_weapon_type 
    global defender_weapon_uses 
    global defender_weapon_might 
    global defender_weapon_hit 
    global defender_weapon_crit 
    global defender_weapon_range 
    global defender_weapon_effect
    global defender_hp_growth 
    global defender_strength_growth 
    global defender_magic_growth 
    global defender_skill_growth 
    global defender_speed_growth 
    global defender_luck_growth 
    global defender_defense_growth
    global defender_resistance_growth

      
      # Attacker's attack
      
      # Attacker's crit roll

      attacker_crit_roll = random.randint(1,100)

      # Attacker gets a crit

      if attacker_crit_roll <= attacker_crit_chance:
          print(attacker_name + " got a critical hit!")
          attacker_hit_roll = random.randint(1,100)
          
          # Attacker hits crit

          if attacker_hit_roll <= attacker_accuracy:
              defender_current_hp = defender_current_hp - attacker_crit_damage
              attacker_weapon_uses -= 1
              print(defender_name + " took " + str(attacker_crit_damage) + " damage!")
              if attacker_weapon_uses <= 0:
                  print(attacker_name + "'s weapon broke!")
          
          # Attacker misses crit

          else:
              print(attacker_name + " missed!")
      
      # Attacker doesn't get a crit

      else:
          attacker_hit_roll = random.randint(1,100)
          
          # Attacker hits

          if attacker_hit_roll <= attacker_accuracy:
              defender_current_hp = defender_current_hp - attacker_damage
              print(attacker_name + " attacks!")
              print(defender_name + " took " + str(attacker_damage) + " damage!")
              attacker_weapon_uses -= 1
              if attacker_weapon_uses <= 0:
                  print(attacker_name + "'s weapon broke!")
          
          # Attacker misses

          else:
              print(attacker_name + " missed!")

      # Defender's attack

      if defender_current_hp > 0:
          
          # Defender's crit roll

          defender_crit_roll = random.randint(1,100)

          # Defender gets a crit

          if defender_crit_roll <= defender_crit_chance:
              print(defender_name + " got a critical hit!")
              defender_hit_roll = random.randint(1,100)

              # Defender hits crit

              if defender_hit_roll <= defender_accuracy:
                  attacker_current_hp = attacker_current_hp - defender_crit_damage
                  print(attacker_name + " took " + str(defender_crit_damage) + " damage!")
                  defender_weapon_uses -= 1
                  if defender_weapon_uses <= 0:
                      print(defender_name + "'s weapon broke!")

              # Defender misses crit

              else:
                  print(defender_name + " missed!")

          # Defender doesn't get a crit

          else:
              defender_hit_roll = random.randint(1,100)

              # Defender hits attack

              if defender_hit_roll <= defender_accuracy:
                  attacker_current_hp = attacker_current_hp - defender_damage
                  print(defender_name + " attacks!")
                  print(attacker_name + " took " + str(defender_damage) + " damage!")
                  defender_weapon_uses -= 1
                  if defender_weapon_uses <= 0:
                      print(defender_name + "'s weapon broke!")

              # Defender misses attack
              
              else:
                  print(defender_name + " missed!")
      
      # Defender is dead
      
      else:
          print(defender_name + " has died.")
          print(attacker_name + " wins!")

      # Attacker is dead

      if attacker_current_hp <= 0:
          print(attacker_name + " has died.")
          print(defender_name + " wins!")

      # Attacker's remaining HP

      print(attacker_name + " has " + str(attacker_current_hp) + " HP remaining.")
      
      # Defender's remaining HP
      
      print(defender_name + " has " + str(defender_current_hp) + " HP remaining.")
      
      # Attacker's weapon's remaining uses

      if attacker_weapon_uses > 1 or attacker_weapon_uses < 1:
          print(attacker_name + "'s weapon has " + str(attacker_weapon_uses) + " uses remaining.")
      else: 
          print(attacker_name + "'s weapon has " + str(attacker_weapon_uses) + " use remaining.")
      
      # Defender's weapon's remaining uses

      if defender_weapon_uses > 1 or defender_weapon_uses < 1:    
          print(defender_name + "'s weapon has " + str(defender_weapon_uses) + " uses remaining.")
      else:
          print(defender_name + "'s weapon has " + str(defender_weapon_uses) + " use remaining.")
      
      # Experience Points

      # Attacker
      
      # Attacker's max level is 30

      #if attacker_class == "dancer" or attacker_class == "manakete" or attacker_class == "taguel" or attacker_class == "conqueror" or attacker_class == "dread fighter" or attacker_class == "bride" or attacker_class == "villager" or attacker_class == "lodestar" or attacker_class == "soldier" or attacker_class == "merchant" or attacker_class == "revenant" or attacker_class == "entombed" or attacker_class == "grima" or attacker_class == "mirage":
      attacker_classes = ["dancer","manakete","taguel","conqueror","dread fighter",
                          "bride","villager","lodestar","soldier","merchant","revenant",
                          "entombed","grima","mirage"]
      if attacker_class in attacker_classes:


          if attacker_current_hp > 0:
         
              if attacker_level < 30:
          
                  # Attacker hits
          
                  if attacker_hit_roll <= attacker_accuracy:
              
                      # Attacker doesn't kill

                      if defender_current_hp > 0:
                  
                          # Experience from dealing damage

                          attacker_exp_gained = int((31 + (defender_level + defender_class_bonus_a) - (attacker_level + attacker_class_bonus_a))/attacker_class_power)
                          attacker_exp += attacker_exp_gained
                          
                          # Leveling up

                          attacker_level_ups = int(attacker_exp/100)
                          attacker_exp -= attacker_level_ups * 100
                          
                          # HP

                          attacker_hp_levels = int(attacker_hp_growth/100)
                          attacker_hp_growth -= attacker_hp_levels * 100
                          
                          # Strength

                          attacker_strength_levels = int(attacker_strength_growth/100)
                          attacker_strength_growth -= attacker_strength_levels * 100
                          
                          # Magic

                          attacker_magic_levels = int(attacker_magic_growth/100)
                          attacker_magic_growth -= attacker_magic_levels * 100
                          
                          # Skill

                          attacker_skill_levels = int(attacker_skill_growth/100)
                          attacker_skill_growth -= attacker_skill_levels * 100
                          
                          # Speed

                          attacker_speed_levels = int(attacker_speed_growth/100)
                          attacker_speed_growth -= attacker_speed_levels * 100
                          
                          # Luck

                          attacker_luck_levels = int(attacker_luck_growth/100)
                          attacker_luck_growth -= attacker_luck_levels * 100
                          
                          # Defense

                          attacker_defense_levels = int(attacker_defense_growth/100)
                          attacker_defense_growth -= attacker_defense_levels * 100
                          
                          # Resistance

                          attacker_resistance_levels = int(attacker_resistance_growth/100)
                          attacker_resistance_growth -= attacker_resistance_levels * 100
                          
                          # Level ups

                          while attacker_level_ups > 0:
                              attacker_level += 1
                              print(attacker_name + " leveled up!")
                              print(attacker_name + "'s level is now " + str(attacker_level) + ".")
                              attacker_level_ups -= 1
                              
                              # HP

                              while attacker_hp_levels > 0:
                                  attacker_max_hp += 1
                                  attacker_hp_levels -= 1
                              attacker_hp_roll = random.randint(1,100)
                              if attacker_hp_roll <= attacker_hp_growth:
                                  attacker_max_hp += 1
                              print(attacker_name + "'s max HP is now " + str(attacker_max_hp) + ".")
                              
                              # Strength

                              while attacker_strength_levels > 0:
                                  attacker_strength += 1
                                  attacker_strength_levels -= 1
                              attacker_strength_roll = random.randint(1,100)
                              if attacker_strength_roll <= attacker_strength_growth:
                                  attacker_strength += 1
                              print(attacker_name + "'s Strength is now " + str(attacker_strength) + ".")
                              
                              # Magic

                              while attacker_magic_levels > 0:
                                  attacker_magic += 1
                                  attacker_magic_levels -= 1
                              attacker_magic_roll = random.randint(1,100)
                              if attacker_magic_roll <= attacker_magic_growth:
                                  attacker_magic += 1
                              print(attacker_name + "'s Magic is now " + str(attacker_magic) + ".")
                              
                              # Skill

                              while attacker_skill_levels > 0:
                                  attacker_skill += 1
                                  attacker_skill_levels -= 1
                              attacker_skill_roll = random.randint(1,100)
                              if attacker_skill_roll <= attacker_skill_growth:
                                  attacker_skill += 1
                              print(attacker_name + "'s Skill is now " + str(attacker_skill) + ".")
                              
                              # Speed

                              while attacker_speed_levels > 0:
                                  attacker_speed += 1
                                  attacker_speed_levels -= 1
                              attacker_speed_roll = random.randint(1,100)
                              if attacker_speed_roll <= attacker_speed_growth:
                                  attacker_speed += 1
                              print(attacker_name + "'s Speed is now " + str(attacker_speed) + ".")
                              
                              # Luck

                              while attacker_luck_levels > 0:
                                  attacker_luck += 1
                                  attacker_luck_levels -= 1
                              attacker_luck_roll = random.randint(1,100)
                              if attacker_luck_roll <= attacker_luck_growth:
                                  attacker_luck += 1
                              print(attacker_name + "'s Luck is now " + str(attacker_luck) + ".")
                              
                              # Defense

                              while attacker_defense_levels > 0:
                                  attacker_defense += 1
                                  attacker_defense_levels -= 1
                              attacker_defense_roll = random.randint(1,100)
                              if attacker_defense_roll <= attacker_defense_growth:
                                  attacker_defense += 1
                              print(attacker_name + "'s Defense is now " + str(attacker_defense) + ".")
                              
                              # Resistance

                              while attacker_resistance_levels > 0:
                                  attacker_resistance += 1
                                  attacker_resistance_levels -= 1
                              attacker_resistance_roll = random.randint(1,100)
                              if attacker_resistance_roll <= attacker_resistance_growth:
                                  attacker_resistance += 1
                              print(attacker_name + "'s Resistance is now " + str(attacker_resistance) + ".")
                          
                      # Attacker kills
              
                      else:
                  
                          # Experience from dealing damage

                          attacker_damage_exp = int((31 + (defender_level + defender_class_bonus_a) - (attacker_level + attacker_class_bonus_a))/attacker_class_power)
                  
                          # Experience from defeating (base)

                          attacker_base_exp = int(((defender_level * defender_class_power) + defender_class_bonus_b) - ((attacker_level * attacker_class_power) + attacker_class_bonus_b))
                  
                          # Experience from defeating enemy

                          attacker_base_defeat_exp = int(attacker_base_exp + 20 + defender_boss_bonus + defender_thief_bonus)
                          if attacker_base_defeat_exp < 0:
                              attacker_base_defeat_exp = 0
                          attacker_defeat_exp = int(attacker_damage_exp + attacker_base_defeat_exp)
                          attacker_exp += attacker_defeat_exp
                          
                          # Leveling up

                          attacker_level_ups = int(attacker_exp/100)
                          attacker_exp -= attacker_level_ups * 100
                          
                          # HP

                          attacker_hp_levels = int(attacker_hp_growth/100)
                          attacker_hp_growth -= attacker_hp_levels * 100
                          
                          # Strength

                          attacker_strength_levels = int(attacker_strength_growth/100)
                          attacker_strength_growth -= attacker_strength_levels * 100
                          
                          # Magic

                          attacker_magic_levels = int(attacker_magic_growth/100)
                          attacker_magic_growth -= attacker_magic_levels * 100
                          
                          # Skill

                          attacker_skill_levels = int(attacker_skill_growth/100)
                          attacker_skill_growth -= attacker_skill_levels * 100
                          
                          # Speed

                          attacker_speed_levels = int(attacker_speed_growth/100)
                          attacker_speed_growth -= attacker_speed_levels * 100
                          
                          # Luck

                          attacker_luck_levels = int(attacker_luck_growth/100)
                          attacker_luck_growth -= attacker_luck_levels * 100
                          
                          # Defense

                          attacker_defense_levels = int(attacker_defense_growth/100)
                          attacker_defense_growth -= attacker_defense_levels * 100
                          
                          # Resistance

                          attacker_resistance_levels = int(attacker_resistance_growth/100)
                          attacker_resistance_growth -= attacker_resistance_levels * 100
                          
                          # Level ups
                          
                          while attacker_level_ups > 0:
                              attacker_level += 1
                              print(attacker_name + " leveled up!")
                              print(attacker_name + "'s level is now " + str(attacker_level) + ".")
                              attacker_level_ups -= 1
                              
                              # HP

                              while attacker_hp_levels > 0:
                                  attacker_max_hp += 1
                                  attacker_hp_levels -= 1
                              attacker_hp_roll = random.randint(1,100)
                              if attacker_hp_roll <= attacker_hp_growth:
                                  attacker_max_hp += 1
                              print(attacker_name + "'s max HP is now " + str(attacker_max_hp) + ".")
                              
                              # Strength

                              while attacker_strength_levels > 0:
                                  attacker_strength += 1
                                  attacker_strength_levels -= 1
                              attacker_strength_roll = random.randint(1,100)
                              if attacker_strength_roll <= attacker_strength_growth:
                                  attacker_strength += 1
                              print(attacker_name + "'s Strength is now " + str(attacker_strength) + ".")
                              
                              # Magic

                              while attacker_magic_levels > 0:
                                  attacker_magic += 1
                                  attacker_magic_levels -= 1
                              attacker_magic_roll = random.randint(1,100)
                              if attacker_magic_roll <= attacker_magic_growth:
                                  attacker_magic += 1
                              print(attacker_name + "'s Magic is now " + str(attacker_magic) + ".")
                              
                              # Skill

                              while attacker_skill_levels > 0:
                                  attacker_skill += 1
                                  attacker_skill_levels -= 1
                              attacker_skill_roll = random.randint(1,100)
                              if attacker_skill_roll <= attacker_skill_growth:
                                  attacker_skill += 1
                              print(attacker_name + "'s Skill is now " + str(attacker_skill) + ".")
                              
                              # Speed

                              while attacker_speed_levels > 0:
                                  attacker_speed += 1
                                  attacker_speed_levels -= 1
                              attacker_speed_roll = random.randint(1,100)
                              if attacker_speed_roll <= attacker_speed_growth:
                                  attacker_speed += 1
                              print(attacker_name + "'s Speed is now " + str(attacker_speed) + ".")
                              
                              # Luck

                              while attacker_luck_levels > 0:
                                  attacker_luck += 1
                                  attacker_luck_levels -= 1
                              attacker_luck_roll = random.randint(1,100)
                              if attacker_luck_roll <= attacker_luck_growth:
                                  attacker_luck += 1
                              print(attacker_name + "'s Luck is now " + str(attacker_luck) + ".")
                              
                              # Defense

                              while attacker_defense_levels > 0:
                                  attacker_defense += 1
                                  attacker_defense_levels -= 1
                              attacker_defense_roll = random.randint(1,100)
                              if attacker_defense_roll <= attacker_defense_growth:
                                  attacker_defense += 1
                              print(attacker_name + "'s Defense is now " + str(attacker_defense) + ".")
                              
                              # Resistance

                              while attacker_resistance_levels > 0:
                                  attacker_resistance += 1
                                  attacker_resistance_levels -= 1
                              attacker_resistance_roll = random.randint(1,100)
                              if attacker_resistance_roll <= attacker_resistance_growth:
                                  attacker_resistance += 1
                              print(attacker_name + "'s Resistance is now " + str(attacker_resistance)  + ".")
                          
                          print(attacker_name + " now has " + str(attacker_exp) + " experience points!")
          
              # Attacker misses

              else:
                  print(attacker_name + " now has " + str(attacker_exp) + " experience points!")
      
          # Attacker is at max level

          else:
              print(attacker_name + " now has " + str(attacker_exp) + " experience points!")

      # Attacker's max level is 20

      else:
          
          if attacker_current_hp > 0:
          
              if attacker_level < 20:
             
                  # Attacker hits
          
                  if attacker_hit_roll <= attacker_accuracy:
              
                      # Attacker doesn't kill

                      if defender_current_hp > 0:
                  
                          # Experience from dealing damage

                          attacker_exp_gained = int((31 + (defender_level + defender_class_bonus_a) - (attacker_level + attacker_class_bonus_a))/attacker_class_power)
                          attacker_exp += attacker_exp_gained
                          
                          # Leveling up

                          attacker_level_ups = int(attacker_exp/100)
                          attacker_exp -= attacker_level_ups * 100
                          
                          # HP

                          attacker_hp_levels = int(attacker_hp_growth/100)
                          attacker_hp_growth -= attacker_hp_levels * 100
                          
                          # Strength

                          attacker_strength_levels = int(attacker_strength_growth/100)
                          attacker_strength_growth -= attacker_strength_levels * 100
                          
                          # Magic

                          attacker_magic_levels = int(attacker_magic_growth/100)
                          attacker_magic_growth -= attacker_magic_levels * 100
                          
                          # Skill

                          attacker_skill_levels = int(attacker_skill_growth/100)
                          attacker_skill_growth -= attacker_skill_levels * 100
                          
                          # Speed

                          attacker_speed_levels = int(attacker_speed_growth/100)
                          attacker_speed_growth -= attacker_speed_levels * 100
                          
                          # Luck

                          attacker_luck_levels = int(attacker_luck_growth/100)
                          attacker_luck_growth -= attacker_luck_levels * 100
                          
                          # Defense

                          attacker_defense_levels = int(attacker_defense_growth/100)
                          attacker_defense_growth -= attacker_defense_levels * 100
                          
                          # Resistance

                          attacker_resistance_levels = int(attacker_resistance_growth/100)
                          attacker_resistance_growth -= attacker_resistance_levels * 100
                          
                          # Level ups

                          while attacker_level_ups > 0:
                              attacker_level += 1
                              print(attacker_name + " leveled up!")
                              print(attacker_name + "'s level is now " + str(attacker_level) + ".")
                              attacker_level_ups -= 1
                              
                              # HP

                              while attacker_hp_levels > 0:
                                  attacker_max_hp += 1
                                  attacker_hp_levels -= 1
                              attacker_hp_roll = random.randint(1,100)
                              if attacker_hp_roll <= attacker_hp_growth:
                                  attacker_max_hp += 1
                              print(attacker_name + "'s max HP is now " + str(attacker_max_hp) + ".")
                              
                              # Strength

                              while attacker_strength_levels > 0:
                                  attacker_strength += 1
                                  attacker_strength_levels -= 1
                              attacker_strength_roll = random.randint(1,100)
                              if attacker_strength_roll <= attacker_strength_growth:
                                  attacker_strength += 1
                              print(attacker_name + "'s Strength is now " + str(attacker_strength) + ".")
                              
                              # Magic

                              while attacker_magic_levels > 0:
                                  attacker_magic += 1
                                  attacker_magic_levels -= 1
                              attacker_magic_roll = random.randint(1,100)
                              if attacker_magic_roll <= attacker_magic_growth:
                                  attacker_magic += 1
                              print(attacker_name + "'s Magic is now " + str(attacker_magic) + ".")
                              
                              # Skill

                              while attacker_skill_levels > 0:
                                  attacker_skill += 1
                                  attacker_skill_levels -= 1
                              attacker_skill_roll = random.randint(1,100)
                              if attacker_skill_roll <= attacker_skill_growth:
                                  attacker_skill += 1
                              print(attacker_name + "'s Skill is now " + str(attacker_skill) + ".")
                              
                              # Speed

                              while attacker_speed_levels > 0:
                                  attacker_speed += 1
                                  attacker_speed_levels -= 1
                              attacker_speed_roll = random.randint(1,100)
                              if attacker_speed_roll <= attacker_speed_growth:
                                  attacker_speed += 1
                              print(attacker_name + "'s Speed is now " + str(attacker_speed) + ".")
                              
                              # Luck

                              while attacker_luck_levels > 0:
                                  attacker_luck += 1
                                  attacker_luck_levels -= 1
                              attacker_luck_roll = random.randint(1,100)
                              if attacker_luck_roll <= attacker_luck_growth:
                                  attacker_luck += 1
                              print(attacker_name + "'s Luck is now " + str(attacker_luck) + ".")
                              
                              # Defense

                              while attacker_defense_levels > 0:
                                  attacker_defense += 1
                                  attacker_defense_levels -= 1
                              attacker_defense_roll = random.randint(1,100)
                              if attacker_defense_roll <= attacker_defense_growth:
                                  attacker_defense += 1
                              print(attacker_name + "'s Defense is now " + str(attacker_defense) + ".")
                              
                              # Resistance

                              while attacker_resistance_levels > 0:
                                  attacker_resistance += 1
                                  attacker_resistance_levels -= 1
                              attacker_resistance_roll = random.randint(1,100)
                              if attacker_resistance_roll <= attacker_resistance_growth:
                                  attacker_resistance += 1
                              print(attacker_name + "'s Resistance is now " + str(attacker_resistance) + ".")
                          
              
                      # Attacker kills
              
                      else:
                  
                          # Experience from dealing damage

                          attacker_damage_exp = int((31 + (defender_level + defender_class_bonus_a) - (attacker_level + attacker_class_bonus_a))/attacker_class_power)
                  
                          # Experience from defeating (base)

                          attacker_base_exp = int(((defender_level * defender_class_power) + defender_class_bonus_b) - ((attacker_level * attacker_class_power) + attacker_class_bonus_b))
                  
                          # Experience from defeating enemy

                          attacker_base_defeat_exp = int(attacker_base_exp + 20 + defender_boss_bonus + defender_thief_bonus)
                          if attacker_base_defeat_exp < 0:
                              attacker_base_defeat_exp = 0
                          attacker_defeat_exp = int(attacker_damage_exp + attacker_base_defeat_exp)
                          attacker_exp += attacker_defeat_exp
                      
                          # Leveling up

                          attacker_level_ups = int(attacker_exp/100)
                          attacker_exp -= attacker_level_ups * 100
                          
                          # HP

                          attacker_hp_levels = int(attacker_hp_growth/100)
                          attacker_hp_growth -= attacker_hp_levels * 100
                          
                          # Strength

                          attacker_strength_levels = int(attacker_strength_growth/100)
                          attacker_strength_growth -= attacker_strength_levels * 100
                          
                          # Magic

                          attacker_magic_levels = int(attacker_magic_growth/100)
                          attacker_magic_growth -= attacker_magic_levels * 100
                          
                          # Skill

                          attacker_skill_levels = int(attacker_skill_growth/100)
                          attacker_skill_growth -= attacker_skill_levels * 100
                          
                          # Speed

                          attacker_speed_levels = int(attacker_speed_growth/100)
                          attacker_speed_growth -= attacker_speed_levels * 100
                          
                          # Luck

                          attacker_luck_levels = int(attacker_luck_growth/100)
                          attacker_luck_growth -= attacker_luck_levels * 100
                          
                          # Defense

                          attacker_defense_levels = int(attacker_defense_growth/100)
                          attacker_defense_growth -= attacker_defense_levels * 100
                          
                          # Resistance

                          attacker_resistance_levels = int(attacker_resistance_growth/100)
                          attacker_resistance_growth -= attacker_resistance_levels * 100
                          
                          # Level ups

                          while attacker_level_ups > 0:
                              attacker_level += 1
                              print(attacker_name + " leveled up!")
                              print(attacker_name + "'s level is now " + str(attacker_level) + ".")
                              attacker_level_ups -= 1
                              
                              # HP

                              while attacker_hp_levels > 0:
                                  attacker_max_hp += 1
                                  attacker_hp_levels -= 1
                              attacker_hp_roll = random.randint(1,100)
                              if attacker_hp_roll <= attacker_hp_growth:
                                  attacker_max_hp += 1
                              print(attacker_name + "'s max HP is now " + str(attacker_max_hp) + ".")
                              
                              # Strength

                              while attacker_strength_levels > 0:
                                  attacker_strength += 1
                                  attacker_strength_levels -= 1
                              attacker_strength_roll = random.randint(1,100)
                              if attacker_strength_roll <= attacker_strength_growth:
                                  attacker_strength += 1
                              print(attacker_name + "'s Strength is now " + str(attacker_strength) + ".")
                              
                              # Magic

                              while attacker_magic_levels > 0:
                                  attacker_magic += 1
                                  attacker_magic_levels -= 1
                              attacker_magic_roll = random.randint(1,100)
                              if attacker_magic_roll <= attacker_magic_growth:
                                  attacker_magic += 1
                              print(attacker_name + "'s Magic is now " + str(attacker_magic) + ".")
                              
                              # Skill

                              while attacker_skill_levels > 0:
                                  attacker_skill += 1
                                  attacker_skill_levels -= 1
                              attacker_skill_roll = random.randint(1,100)
                              if attacker_skill_roll <= attacker_skill_growth:
                                  attacker_skill += 1
                              print(attacker_name + "'s Skill is now " + str(attacker_skill) + ".")
                              
                              # Speed

                              while attacker_speed_levels > 0:
                                  attacker_speed += 1
                                  attacker_speed_levels -= 1
                              attacker_speed_roll = random.randint(1,100)
                              if attacker_speed_roll <= attacker_speed_growth:
                                  attacker_speed += 1
                              print(attacker_name + "'s Speed is now " + str(attacker_speed) + ".")
                              
                              # Luck

                              while attacker_luck_levels > 0:
                                  attacker_luck += 1
                                  attacker_luck_levels -= 1
                              attacker_luck_roll = random.randint(1,100)
                              if attacker_luck_roll <= attacker_luck_growth:
                                  attacker_luck += 1
                              print(attacker_name + "'s Luck is now " + str(attacker_luck) + ".")
                              
                              # Defense

                              while attacker_defense_levels > 0:
                                  attacker_defense += 1
                                  attacker_defense_levels -= 1
                              attacker_defense_roll = random.randint(1,100)
                              if attacker_defense_roll <= attacker_defense_growth:
                                  attacker_defense += 1
                              print(attacker_name + "'s Defense is now " + str(attacker_defense) + ".")
                              
                              # Resistance

                              while attacker_resistance_levels > 0:
                                  attacker_resistance += 1
                                  attacker_resistance_levels -= 1
                              attacker_resistance_roll = random.randint(1,100)
                              if attacker_resistance_roll <= attacker_resistance_growth:
                                  attacker_resistance += 1
                              print(attacker_name + "'s Resistance is now " + str(attacker_resistance) + ".")
                          
                  # Attacker misses

                  else:
                      print(attacker_name + " now has " + str(attacker_exp) + " experience points!")
          
              # Attacker is at max level

              else:
                  print(attacker_name + " now has " + str(attacker_exp) + " experience points!")

      # Defender
      
      # Defender's max level is 30

      #if attacker_class == "dancer" or attacker_class == "manakete" or attacker_class == "taguel" or attacker_class == "conqueror" or attacker_class == "dread fighter" or attacker_class == "bride" or attacker_class == "villager" or attacker_class == "lodestar" or attacker_class == "soldier" or attacker_class == "merchant" or attacker_class == "revenant" or attacker_class == "entombed" or attacker_class == "grima" or attacker_class == "mirage":
      defender_classes = ["dancer","manakete","taguel","conqueror","dread fighter",
                          "bride","villager","lodestar","soldier","merchant","revenant",
                          "entombed","grima","mirage"]
      if defender_class in defender_classes:


          if defender_current_hp > 0:
         
              if defender_level < 30:
          
                  # Defender hits
          
                  if defender_hit_roll <= defender_accuracy:
              
                      # Defender doesn't kill

                      if attacker_current_hp > 0:
                  
                          # Experience from dealing damage

                          defender_exp_gained = int((31 + (attacker_level + attacker_class_bonus_a) - (defender_level + defender_class_bonus_a))/defender_class_power)
                          defender_exp += defender_exp_gained
                          
                          # Leveling up

                          defender_level_ups = int(defender_exp/100)
                          defender_exp -= defender_level_ups * 100
                          
                          # HP

                          defender_hp_levels = int(defender_hp_growth/100)
                          defender_hp_growth -= defender_hp_levels * 100
                          
                          # Strength

                          defender_strength_levels = int(defender_strength_growth/100)
                          defender_strength_growth -= defender_strength_levels * 100
                          
                          # Magic

                          defender_magic_levels = int(defender_magic_growth/100)
                          defender_magic_growth -= defender_magic_levels * 100
                          
                          # Skill

                          defender_skill_levels = int(defender_skill_growth/100)
                          defender_skill_growth -= defender_skill_levels * 100
                          
                          # Speed

                          defender_speed_levels = int(defender_speed_growth/100)
                          defender_speed_growth -= defender_speed_levels * 100
                          
                          # Luck

                          defender_luck_levels = int(defender_luck_growth/100)
                          defender_luck_growth -= defender_luck_levels * 100
                          
                          # Defense

                          defender_defense_levels = int(defender_defense_growth/100)
                          defender_defense_growth -= defender_defense_levels * 100
                          
                          # Resistance

                          defender_resistance_levels = int(defender_resistance_growth/100)
                          defender_resistance_growth -= defender_resistance_levels * 100
                          
                          # Level ups

                          while defender_level_ups > 0:
                              defender_level += 1
                              print(defender_name + " leveled up!")
                              print(defender_name + "'s level is now " + str(defender_level) + ".")
                              defender_level_ups -= 1
                              
                              # HP

                              while defender_hp_levels > 0:
                                  defender_max_hp += 1
                                  defender_hp_levels -= 1
                              defender_hp_roll = random.randint(1,100)
                              if defender_hp_roll <= defender_hp_growth:
                                  defender_max_hp += 1
                              print(defender_name + "'s max HP is now " + str(defender_max_hp) + ".")
                              
                              # Strength

                              while defender_strength_levels > 0:
                                  defender_strength += 1
                                  defender_strength_levels -= 1
                              defender_strength_roll = random.randint(1,100)
                              if defender_strength_roll <= defender_strength_growth:
                                  defender_strength += 1
                              print(defender_name + "'s Strength is now " + str(defender_strength) + ".")
                              
                              # Magic

                              while defender_magic_levels > 0:
                                  defender_magic += 1
                                  defender_magic_levels -= 1
                              defender_magic_roll = random.randint(1,100)
                              if defender_magic_roll <= defender_magic_growth:
                                  defender_magic += 1
                              print(defender_name + "'s Magic is now " + str(defender_magic) + ".")
                              
                              # Skill

                              while defender_skill_levels > 0:
                                  defender_skill += 1
                                  defender_skill_levels -= 1
                              defender_skill_roll = random.randint(1,100)
                              if defender_skill_roll <= defender_skill_growth:
                                  defender_skill += 1
                              print(defender_name + "'s Skill is now " + str(defender_skill) + ".")
                              
                              # Speed

                              while defender_speed_levels > 0:
                                  defender_speed += 1
                                  defender_speed_levels -= 1
                              defender_speed_roll = random.randint(1,100)
                              if defender_speed_roll <= defender_speed_growth:
                                  defender_speed += 1
                              print(defender_name + "'s Speed is now " + str(defender_speed) + ".")
                              
                              # Luck

                              while defender_luck_levels > 0:
                                  defender_luck += 1
                                  defender_luck_levels -= 1
                              defender_luck_roll = random.randint(1,100)
                              if defender_luck_roll <= defender_luck_growth:
                                  defender_luck += 1
                              print(defender_name + "'s Luck is now " + str(defender_luck) + ".")
                              
                              # Defense

                              while defender_defense_levels > 0:
                                  defender_defense += 1
                                  defender_defense_levels -= 1
                              defender_defense_roll = random.randint(1,100)
                              if defender_defense_roll <= defender_defense_growth:
                                  defender_defense += 1
                              print(defender_name + "'s Defense is now " + str(defender_defense) + ".")
                              
                              # Resistance

                              while defender_resistance_levels > 0:
                                  defender_resistance += 1
                                  defender_resistance_levels -= 1
                              defender_resistance_roll = random.randint(1,100)
                              if defender_resistance_roll <= defender_resistance_growth:
                                  defender_resistance += 1
                              print(defender_name + "'s Resistance is now " + str(defender_resistance) + ".")
                          
                      # Defender kills
              
                      else:
                  
                          # Experience from dealing damage

                          defender_damage_exp = int((31 + (attacker_level + attacker_class_bonus_a) - (defender_level + defender_class_bonus_a))/defender_class_power)
                  
                          # Experience from defeating (base)

                          attacker_base_exp = int(((attacker_level * attacker_class_power) + attacker_class_bonus_b) - ((defender_level * defender_class_power) + defender_class_bonus_b))
                  
                          # Experience from defeating enemy

                          defender_base_defeat_exp = int(defender_base_exp + 20 + attacker_boss_bonus + attacker_thief_bonus)
                          if defender_base_defeat_exp < 0:
                              defender_base_defeat_exp = 0
                          defender_defeat_exp = int(defender_damage_exp + defender_base_defeat_exp)
                          defender_exp += defender_defeat_exp
                          
                          # Leveling up

                          defender_level_ups = int(defenderr_exp/100)
                          defender_exp -= defender_level_ups * 100
                          
                          # HP

                          defender_hp_levels = int(defender_hp_growth/100)
                          defender_hp_growth -= defender_hp_levels * 100
                          
                          # Strength

                          defender_strength_levels = int(defender_strength_growth/100)
                          defender_strength_growth -= defender_strength_levels * 100
                          
                          # Magic

                          defender_magic_levels = int(defender_magic_growth/100)
                          defender_magic_growth -= defender_magic_levels * 100
                          
                          # Skill

                          defender_skill_levels = int(defender_skill_growth/100)
                          defender_skill_growth -= defender_skill_levels * 100
                          
                          # Speed

                          defender_speed_levels = int(defender_speed_growth/100)
                          defender_speed_growth -= defender_speed_levels * 100
                          
                          # Luck

                          defender_luck_levels = int(defender_luck_growth/100)
                          defender_luck_growth -= defender_luck_levels * 100
                          
                          # Defense

                          defender_defense_levels = int(defender_defense_growth/100)
                          defender_defense_growth -= defender_defense_levels * 100
                          
                          # Resistance

                          defender_resistance_levels = int(defender_resistance_growth/100)
                          defender_resistance_growth -= defender_resistance_levels * 100
                          
                          # Level ups

                          while defender_level_ups > 0:
                              defender_level += 1
                              print(defender_name + " leveled up!")
                              print(defender_name + "'s level is now " + str(defender_level) + ".")
                              defender_level_ups -= 1
                              
                              # HP

                              while defender_hp_levels > 0:
                                  defender_max_hp += 1
                                  defender_hp_levels -= 1
                              defender_hp_roll = random.randint(1,100)
                              if defender_hp_roll <= defender_hp_growth:
                                  defender_max_hp += 1
                              print(defender_name + "'s max HP is now " + str(defender_max_hp) + ".")
                              
                              # Strength

                              while defender_strength_levels > 0:
                                defender_strength += 1
                                defender_strength_levels -= 1
                              defender_strength_roll = random.randint(1,100)
                              if defender_strength_roll <= defender_strength_growth:
                                  defender_strength += 1
                              print(defender_name + "'s Strength is now " + str(defender_strength) + ".")
                              
                              # Magic

                              while defender_magic_levels > 0:
                                  defender_magic += 1
                                  defender_magic_levels -= 1
                              defender_magic_roll = random.randint(1,100)
                              if defender_magic_roll <= defender_magic_growth:
                                  defender_magic += 1
                              print(defender_name + "'s Magic is now " + str(defender_magic) + ".")
                              
                              # Skill

                              while defender_skill_levels > 0:
                                  defender_skill += 1
                                  defender_skill_levels -= 1
                              defender_skill_roll = random.randint(1,100)
                              if defender_skill_roll <= defender_skill_growth:
                                  defender_skill += 1
                              print(defender_name + "'s Skill is now " + str(defender_skill) + ".")
                              
                              # Speed

                              while defender_speed_levels > 0:
                                  defender_speed += 1
                                  defender_speed_levels -= 1
                              defender_speed_roll = random.randint(1,100)
                              if defender_speed_roll <= defender_speed_growth:
                                  defender_speed += 1
                              print(defender_name + "'s Speed is now "+ str(defender_speed) + ".")
                              
                              # Luck

                              while defender_luck_levels > 0:
                                  defender_luck += 1
                                  defender_luck_levels -= 1
                              defender_luck_roll = random.randint(1,100)
                              if defender_luck_roll <= defender_luck_growth:
                                  defender_luck += 1
                              print(defender_name + "'s Luck is now " + str(defender_luck) + ".")
                              
                              # Defense

                              while defender_defense_levels > 0:
                                  defender_defense += 1
                                  defender_defense_levels -= 1
                              defender_defense_roll = random.randint(1,100)
                              if defender_defense_roll <= defender_defense_growth:
                                  defender_defense += 1
                              print(defender_name + "'s Defense is now " + str(defender_defense) + ".")
                              
                              # Resistance

                              while defender_resistance_levels > 0:
                                  defender_resistance += 1
                                  defender_resistance_levels -= 1
                              defender_resistance_roll = random.randint(1,100)
                              if defender_resistance_roll <= defender_resistance_growth:
                                  defender_resistance += 1
                              print(defender_name + "'s Resistance is now " + str(defender_resistance)  + ".")
                          
                          print(defender_name + " now has " + str(defender_exp) + " experience points!")
          
              # Defender misses

                  else:
                      print(defender_name + " now has " + str(defender_exp) + " experience points!")
      
          # Defender is at max level

              else:
                  print(defender_name + " now has " + str(defender_exp) + " experience points!")

      # Defender's max level is 20

      else:
          
          if defender_current_hp > 0:
          
              if defender_level < 20:
             
                  # Defender hits
          
                  if defender_hit_roll <= defender_accuracy:
              
                      # Defender doesn't kill

                      if attacker_current_hp > 0:
                  
                          # Experience from dealing damage

                          defender_exp_gained = int((31 + (attacker_level + attacker_class_bonus_a) - (defender_level + defender_class_bonus_a))/defender_class_power)
                          defender_exp += defender_exp_gained
                          
                          # Leveling up

                          defender_level_ups = int(defender_exp/100)
                          defender_exp -= defender_level_ups * 100
                          
                          # HP

                          defender_hp_levels = int(defender_hp_growth/100)
                          defender_hp_growth -= defender_hp_levels * 100
                          
                          # Strength

                          defender_strength_levels = int(defender_strength_growth/100)
                          defender_strength_growth -= defender_strength_levels * 100
                          
                          # Magic

                          defender_magic_levels = int(defender_magic_growth/100)
                          defender_magic_growth -= defender_magic_levels * 100
                          
                          # Skill

                          defender_skill_levels = int(defender_skill_growth/100)
                          defender_skill_growth -= defender_skill_levels * 100
                          
                          # Speed

                          defender_speed_levels = int(defender_speed_growth/100)
                          defender_speed_growth -= defender_speed_levels * 100
                          
                          # Luck

                          defender_luck_levels = int(defender_luck_growth/100)
                          defender_luck_growth -= defender_luck_levels * 100
                          
                          # Defense

                          defender_defense_levels = int(defender_defense_growth/100)
                          defender_defense_growth -= defender_defense_levels * 100
                          
                          # Resistance

                          defender_resistance_levels = int(defender_resistance_growth/100)
                          defender_resistance_growth -= defender_resistance_levels * 100
                          
                          # Level ups

                          while defender_level_ups > 0:
                              defender_level += 1
                              print(defender_name + " leveled up!")
                              print(defender_name + "'s level is now " + str(defender_level) + ".")
                              defender_level_ups -= 1
                              
                              # HP

                              while defender_hp_levels > 0:
                                  defender_max_hp += 1
                                  defender_hp_levels -= 1
                              defender_hp_roll = random.randint(1,100)
                              if defender_hp_roll <= defender_hp_growth:
                                  defender_max_hp += 1
                              print(defender_name + "'s max HP is now " + str(defender_max_hp) + ".")
                              
                              # Strength

                              while defender_strength_levels > 0:
                                  defender_strength += 1
                                  defender_strength_levels -= 1
                              defender_strength_roll = random.randint(1,100)
                              if defender_strength_roll <= defender_strength_growth:
                                  defender_strength += 1
                              print(defender_name + "'s Strength is now " + str(defender_strength) + ".")
                              
                              # Magic

                              while defender_magic_levels > 0:
                                  defender_magic += 1
                                  defender_magic_levels -= 1
                              defender_magic_roll = random.randint(1,100)
                              if defender_magic_roll <= defender_magic_growth:
                                  defender_magic += 1
                              print(defender_name + "'s Magic is now " + str(defender_magic) + ".")
                              
                              # Skill

                              while defender_skill_levels > 0:
                                  defender_skill += 1
                                  defender_skill_levels -= 1
                              defender_skill_roll = random.randint(1,100)
                              if defender_skill_roll <= defender_skill_growth:
                                  defender_skill += 1
                              print(defender_name + "'s Skill is now " + str(defender_skill) + ".")
                              
                              # Speed

                              while defender_speed_levels > 0:
                                  defender_speed += 1
                                  defender_speed_levels -= 1
                              defender_speed_roll = random.randint(1,100)
                              if defender_speed_roll <= defender_speed_growth:
                                  defender_speed += 1
                              print(defender_name + "'s Speed is now " + str(defender_speed) + ".")
                              
                              # Luck

                              while defender_luck_levels > 0:
                                  defender_luck += 1
                                  defender_luck_levels -= 1
                              defender_luck_roll = random.randint(1,100)
                              if defender_luck_roll <= defender_luck_growth:
                                  defender_luck += 1
                              print(defender_name + "'s Luck is now " + str(defender_luck) + ".")
                              
                              # Defense

                              while defender_defense_levels > 0:
                                  defender_defense += 1
                                  defender_defense_levels -= 1
                              defender_defense_roll = random.randint(1,100)
                              if defender_defense_roll <= defender_defense_growth:
                                  defender_defense += 1
                              print(defender_name + "'s Defense is now " + str(defender_defense) + ".")
                              
                              # Resistance

                              while defender_resistance_levels > 0:
                                  defender_resistance += 1
                                  defender_resistance_levels -= 1
                              defender_resistance_roll = random.randint(1,100)
                              if defender_resistance_roll <= defender_resistance_growth:
                                  defender_resistance += 1
                              print(defender_name + "'s Resistance is now " + str(defender_resistance) + ".")
                          
              
                      # Defender kills
              
                      else:
                  
                          # Experience from dealing damage

                          defender_damage_exp = int((31 + (attacker_level + attacker_class_bonus_a) - (defender_level + defender_class_bonus_a))/defender_class_power)
                  
                          # Experience from defeating (base)

                          defender_base_exp = int(((attacker_level * attacker_class_power) + attacker_class_bonus_b) - ((defender_level * defender_class_power) + defender_class_bonus_b))
                  
                          # Experience from defeating enemy

                          defender_base_defeat_exp = int(defender_base_exp + 20 + attacker_boss_bonus + attacker_thief_bonus)
                          if defender_base_defeat_exp < 0:
                              defender_base_defeat_exp = 0
                          defender_defeat_exp = int(defender_damage_exp + defender_base_defeat_exp)
                          defender_exp += defender_defeat_exp
                      
                          # Leveling up

                          defender_level_ups = int(defender_exp/100)
                          defender_exp -= defender_level_ups * 100
                          
                          # HP

                          defender_hp_levels = int(defender_hp_growth/100)
                          defender_hp_growth -= defender_hp_levels * 100
                          
                          # Strength

                          defender_strength_levels = int(defender_strength_growth/100)
                          defender_strength_growth -= defender_strength_levels * 100
                          
                          # Magic

                          defender_magic_levels = int(defender_magic_growth/100)
                          defender_magic_growth -= defender_magic_levels * 100
                          
                          # Skill

                          defender_skill_levels = int(defender_skill_growth/100)
                          defender_skill_growth -= defender_skill_levels * 100
                          
                          # Speed

                          defender_speed_levels = int(defender_speed_growth/100)
                          defender_speed_growth -= defender_speed_levels * 100
                          
                          # Luck

                          defender_luck_levels = int(defender_luck_growth/100)
                          defender_luck_growth -= defender_luck_levels * 100
                          
                          # Defense

                          defender_defense_levels = int(defender_defense_growth/100)
                          defender_defense_growth -= defender_defense_levels * 100
                          
                          # Resistance

                          defender_resistance_levels = int(defender_resistance_growth/100)
                          defender_resistance_growth -= defender_resistance_levels * 100
                          
                          # Level ups

                          while defender_level_ups > 0:
                              defender_level += 1
                              print(defender_name + " leveled up!")
                              print(defender_name + "'s level is now " + str(defender_level) + ".")
                              defender_level_ups -= 1
                              
                              # HP

                              while defender_hp_levels > 0:
                                  defender_max_hp += 1
                                  defender_hp_levels -= 1
                              defender_hp_roll = random.randint(1,100)
                              if defender_hp_roll <= defender_hp_growth:
                                  defender_max_hp += 1
                              print(defender_name + "'s max HP is now " + str(defender_max_hp) + ".")
                              
                              # Strength

                              while defender_strength_levels > 0:
                                  defender_strength += 1
                                  defender_strength_levels -= 1
                              defender_strength_roll = random.randint(1,100)
                              if defender_strength_roll <= defender_strength_growth:
                                  defender_strength += 1
                              print(defender_name + "'s Strength is now " + str(defender_strength) + ".")
                              
                              # Magic

                              while defender_magic_levels > 0:
                                  defender_magic += 1
                                  defender_magic_levels -= 1
                              defender_magic_roll = random.randint(1,100)
                              if defender_magic_roll <= defender_magic_growth:
                                  defender_magic += 1
                              print(defender_name + "'s Magic is now " + str(defender_magic) + ".")
                              
                              # Skill

                              while defender_skill_levels > 0:
                                  defender_skill += 1
                                  defender_skill_levels -= 1
                              defender_skill_roll = random.randint(1,100)
                              if defender_skill_roll <= defender_skill_growth:
                                  defender_skill += 1
                              print(defender_name + "'s Skill is now " + str(defender_skill) + ".")
                              
                              # Speed

                              while defender_speed_levels > 0:
                                  defender_speed += 1
                                  defender_speed_levels -= 1
                              defender_speed_roll = random.randint(1,100)
                              if defender_speed_roll <= defender_speed_growth:
                                  defender_speed += 1
                              print(defender_name + "'s Speed is now " + str(defender_speed) + ".")
                              
                              # Luck

                              while defender_luck_levels > 0:
                                  defender_luck += 1
                                  defender_luck_levels -= 1
                              defender_luck_roll = random.randint(1,100)
                              if defender_luck_roll <= defender_luck_growth:
                                  defender_luck += 1
                              print(defender_name + "'s Luck is now " + str(defender_luck) + ".")
                              
                              # Defense

                              while defender_defense_levels > 0:
                                  defender_defense += 1
                                  defender_defense_levels -= 1
                              defender_defense_roll = random.randint(1,100)
                              if defender_defense_roll <= defender_defense_growth:
                                  defender_defense += 1
                              print(defender_name + "'s Defense is now " + str(defender_defense) + ".")
                              
                              # Resistance
                              
                              while defender_resistance_levels > 0:
                                  defender_resistance += 1
                                  defender_resistance_levels -= 1
                              defender_resistance_roll = random.randint(1,100)
                              if defender_resistance_roll <= defender_resistance_growth:
                                  defender_resistance += 1
                              print(defender_name + "'s Resistance is now " + str(defender_resistance) + ".")
                  
                  # Defender misses
              
                  else:
                    print(defender_name + " now has " + str(defender_exp) + " experience points!")
          
              # Defender is at max level
          
            # else:
                # print(defender_name + " now has " + str(defender_exp) + " experience points!")
