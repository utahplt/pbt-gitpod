from hypothesis import given, settings, strategies as st
from typing import Dict, List
from card_game_utils import *
from correct_card_game import deal, draw, play_hand

MAX_EXAMPLES = 1_000 # lower number => faster, but less coverage
settings.register_profile("my_profile", settings(max_examples=MAX_EXAMPLES, deadline=None))
settings.load_profile("my_profile")


def is_valid_deal(num_players: int, dealt_hands: List[Hand]) -> bool:
    '''
    Check that dealt_hands is a valid deal for num_players

    Every player needs HAND_SIZE cards. All cards must be unique, no duplicates.
    It is illegal to call deal with no players or with more than MAX_PLAYERS players.
    '''
    raise NotImplementedError

def is_valid_draw(old_hand: Hand, num_to_draw: int, new_hand: Hand) -> bool:
    '''
    Check that new_hand is a valid result for draw(old_hand, num_to_draw)

    The new hand should have num_to_draw cards replaced with different cards.
    It is illegal to call draw on an invalid hand or with a negative
     num_to_draw or with a num_to_draw that is greater than the number of cards.
    '''
    raise NotImplementedError

def is_valid_play_hand(player: Hand, opponent: Hand, result: GameResult) -> bool:
    '''
    Check that result is a valid outcome of play_hand(player, opponent)
    from the perspective of the player.
    '''
    raise NotImplementedError

def num_players_strat():
    raise NotImplementedError

@given(num_players=num_players_strat())
def test_deal(num_players: int):
    dealt_hands = deal(num_players)
    assert is_valid_deal(num_players, dealt_hands)

def old_hand_strat():
    raise NotImplementedError

def num_to_draw_strat():
    raise NotImplementedError

@given(old_hand=old_hand_strat(), num_to_draw=num_to_draw_strat())
def test_draw(old_hand: Hand, num_to_draw: int):
    new_hand = draw(old_hand, num_to_draw)
    assert is_valid_draw(old_hand, num_to_draw, new_hand)

def player_strat():
    raise NotImplementedError

def opponent_strat():
    raise NotImplementedError

@given(player=player_strat(), opponent=opponent_strat())
def test_play_hand(player: Hand, opponent: Hand):
    result = play_hand(player, opponent)
    assert is_valid_play_hand(player, opponent, result)

## ---
# Write at least one test for each of the is_valid functions.
# These tests do NOT need to use hypothesis.

def test_is_valid_deal_1():
    raise NotImplementedError

def test_is_valid_draw_1():
    raise NotImplementedError

def test_is_valid_play_hand_1():
    raise NotImplementedError

