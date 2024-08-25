

from math import comb

def probability_of_drawing_key_cards(deck_size, hand_size, key_card_copies, desired_count):
    if desired_count > key_card_copies or desired_count > hand_size:
        return 0
    
    total_ways_to_draw_hand = comb(deck_size, hand_size)
    ways_to_draw_desired_key_cards = comb(key_card_copies, desired_count)
    ways_to_draw_remaining_cards = comb(deck_size - key_card_copies, hand_size - desired_count)
    
    probability = (ways_to_draw_desired_key_cards * ways_to_draw_remaining_cards) / total_ways_to_draw_hand
    return probability

deck_size = 40
hand_size = 5
key_card_copies = 3
desired_count = 1

probability = probability_of_drawing_key_cards(deck_size, hand_size, key_card_copies, desired_count)
print(f"Probability: {probability:.2%}")

