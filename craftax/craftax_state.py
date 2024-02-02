from dataclasses import dataclass
from typing import Tuple

import jax
from flax import struct
import jax.numpy as jnp


@struct.dataclass
class Inventory:
    wood: int = 0
    stone: int = 0
    coal: int = 0
    iron: int = 0
    diamond: int = 0
    sapling: int = 0
    pickaxe: int = 0
    sword: int = 0
    bow: int = 0
    arrows: int = 0
    armour: jnp.ndarray = jnp.array([0, 0, 0, 0], dtype=jnp.int32)
    torches: int = 0
    ruby: int = 0
    sapphire: int = 0
    potions: jnp.ndarray = jnp.array(
        [
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        dtype=jnp.int32,
    )
    books: int = 0


@struct.dataclass
class Mobs:
    position: jnp.ndarray
    health: jnp.ndarray
    mask: jnp.ndarray
    attack_cooldown: jnp.ndarray
    type_id: jnp.ndarray


# @struct.dataclass
# class Projectiles(Mobs):
#     directions: jnp.ndarray
#     lifetimes: jnp.ndarray


@struct.dataclass
class EnvState:
    map: jnp.ndarray
    mob_map: jnp.ndarray
    light_map: jnp.ndarray
    down_ladders: jnp.ndarray
    up_ladders: jnp.ndarray
    chests_opened: jnp.ndarray
    monsters_killed: jnp.ndarray

    player_position: jnp.ndarray
    player_level: int
    player_direction: int

    # Intrinsics
    player_health: float
    player_food: int
    player_drink: int
    player_energy: int
    player_mana: int
    is_sleeping: bool
    is_resting: bool

    # Second order intrinsics
    player_recover: float
    player_hunger: float
    player_thirst: float
    player_fatigue: float
    player_recover_mana: float

    # Attributes
    player_xp: int
    player_dexterity: int
    player_strength: int
    player_intelligence: int

    inventory: Inventory

    melee_mobs: Mobs
    passive_mobs: Mobs
    ranged_mobs: Mobs

    mob_projectiles: Mobs
    mob_projectile_directions: jnp.ndarray
    player_projectiles: Mobs
    player_projectile_directions: jnp.ndarray

    growing_plants_positions: jnp.ndarray
    growing_plants_age: jnp.ndarray
    growing_plants_mask: jnp.ndarray

    potion_mapping: jnp.ndarray
    learned_spells: jnp.ndarray

    sword_enchantment: int
    armour_enchantments: jnp.ndarray

    boss_progress: int
    boss_timesteps_to_spawn_this_round: int

    light_level: float

    achievements: jnp.ndarray

    state_rng: jax.random.PRNGKeyArray

    timestep: int


@struct.dataclass
class EnvParams:
    max_timesteps: int = 100000
    day_length: int = 300

    melee_mob_health: int = 5
    passive_mob_health: int = 3
    ranged_mob_health: int = 3

    mob_despawn_distance: int = 14
    max_attribute: int = 5


@struct.dataclass
class StaticEnvParams:
    map_size: Tuple[int, int] = (48, 48)
    num_levels: int = 9

    # Mobs
    max_melee_mobs: int = 3
    max_passive_mobs: int = 3
    max_growing_plants: int = 10
    max_ranged_mobs: int = 2
    max_mob_projectiles: int = 3
    max_player_projectiles: int = 3