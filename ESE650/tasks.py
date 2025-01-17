from pdb import set_trace as T

from nmmo import Task
from collections import namedtuple

class Tier:
    REWARD_SCALE = 15
    EASY         = 4  / REWARD_SCALE
    NORMAL       = 6  / REWARD_SCALE
    HARD         = 11 / REWARD_SCALE

def player_kills(realm, player):
    return player.history.playerKills

def equipment(realm, player):
    return player.equipment.total(lambda e: e.level)

def exploration(realm, player):
    return player.history.exploration

def foraging(realm, player):
    return max(
            player.skills.fishing.level.val,
            player.skills.herbalism.level.val,
            player.skills.prospecting.level.val,
            player.skills.carving.level.val,
            player.skills.alchemy.level.val)

def combat(realm, player):
    return max(
            player.skills.mage.level.val,
            player.skills.range.level.val,
            player.skills.melee.level.val)


PlayerKills = [
        Task(player_kills, 1, Tier.EASY),
        Task(player_kills, 3, Tier.NORMAL),
        Task(player_kills, 6, Tier.HARD)]

Equipment = [
        Task(equipment, 1,  Tier.EASY),
        Task(equipment, 10, Tier.NORMAL),
        Task(equipment, 20, Tier.HARD)]

Exploration = [
        Task(exploration, 32,  Tier.EASY),
        Task(exploration, 64,  Tier.NORMAL),
        Task(exploration, 127, Tier.HARD)]

Foraging = [
        Task(foraging, 3, Tier.EASY),
        Task(foraging, 5, Tier.NORMAL),
        Task(foraging, 10, Tier.HARD)]

Combat  = [
        Task(combat, 3, Tier.EASY),
        Task(combat, 5, Tier.NORMAL),
        Task(combat, 10, Tier.HARD)]

All = PlayerKills + Equipment + Exploration + Foraging
MAF = Exploration