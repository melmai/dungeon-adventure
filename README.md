# Dungeon Adventure

## Adventurer Class

### Properties

**`.name`** <br>Returns the name of the Adventurer

**`.health`** <br>Returns the current HP

**`.healing_potions`** <br>Returns the list of Healing Potions in the inventory

**`.pillars`** <br>Returns the current status of each pillar in the inventory

**`.location`**<br>Returns the current Room of the Adventurer

---

### Methods

**`.health(hp: Int)`**<br>Sets the provided value to the Adventurer's HP

**`.take_damage(damage: Int = None)`**<br>Lowers the HP of the Adventurer by the damage amount provided. If no damage provided, generates an amount between 1-20.

**`.add_vision_potion()`**<br>Increments inventory value of Vision Potions

**`.use_vision_potion()`**<br>Decrements inventory value of Vision Potions.<br>Returns `True` if successful, `False` otherwise.

**`.add_healing_potion(healing_potion: HealingPotion = None)`**<br>Adds a Healing Potion object to the inventory. Accepts an optional `HealingPotion` object to add. If none provided, will generate one.

**`.use_healing_potion()`**<br>Updates the HP of the Adventurer, up to max HP using the most recently added Healing Potion.<br>Returns amount healed.

**`.add_pillar(pillar: String)`**<br>Adds a pillar to the inventory

**`.move(room: Room)`**<br>Updates the current location of the Adventurer

**`.mission_complete()`**<br>Checks the inventory to see if all pillars found.<br>Returns `True` if all pillars collected, `False` otherwise.
