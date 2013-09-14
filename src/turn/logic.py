from turn.models import Turn


def turn_tick():
    new_turn = Turn.new()
    new_turn.save()
    return new_turn