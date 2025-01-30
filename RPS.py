def player(prev_play, opponent_history=[], my_history=[], play_order={}):
    if prev_play:
        opponent_history.append(prev_play)

    specific_sequence = ["R", "P", "S"]

    # Use a specific sequence for the first 5 plays
    if len(my_history) < 5:
        my_move = specific_sequence[len(my_history) % 3]
        my_history.append(my_move)
        return my_move

    # Update play order with the opponent's response to our previous move
    if len(opponent_history) >= 5:
        last_five = "".join(opponent_history[-5:])
        play_order[last_five] = play_order.get(last_five, 0) + 1

    # Predict the opponent's next move based on their response history
    if len(opponent_history) >= 4:
        last_four = "".join(opponent_history[-4:])
        potential_plays = [last_four + v for v in ['R', 'P', 'S']]
        sub_order = {k: play_order[k] for k in potential_plays if k in play_order}

        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1]
        else:
            prediction = "S"  # Default prediction when there is no clear pattern
    else:
        prediction = "S"  # Default prediction when there is no clear pattern

    counter_moves = {"R": "P", "P": "S", "S": "R"}
    my_move = counter_moves[prediction]

    my_history.append(my_move)
    return my_move
