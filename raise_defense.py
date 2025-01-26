import argparse
import random

# UTG - BU

default_3bet = [
    "AA", "KK", "QQ", "JJ", "TT", "99", "88",
    "AKo", "AQo",
    "AKs", "AQs", "AJs", "ATs", "KQs", "KJs", "KTs", "QJs", "QTs", "JTs",
]

default_3bet_caution = [
    "AQo", "ATs", "KTs", "QTs", "JTs",
]

# SB

sb_vs_utg_3bet = [
    "AA", "KK", "QQ", "JJ", "TT",
    "AKo",
    "AKs", "AQs", "AJs", "KQs", "KJs", "QJs",
]

sb_vs_utg_3bet_caution = ['AQo', 'ATs', 'QJs', 'KJs', 'KTs', '99']

sb_vs_mp_3bet = sb_vs_utg_3bet + ['AQo', 'ATs']

sb_vs_mp_3bet_caution = ['AQo', 'QTs', 'KTs', '99', '88', 'A5s']

sb_vs_co_3bet = sb_vs_mp_3bet + ['AJo', 'KQo', 'KTs', 'QTs', 'JTs', '99']

sb_vs_co_3bet_caution = ['AJo', 'KQo', 'KJo', '88', '77', 'A9s', 'K9s', 'A5s', 'A4s', 'A3s']

sb_vs_bu_3bet = sb_vs_co_3bet +  ['A9s', 'K9s', 'Q9s', '88', '77', '66', 'A5s', 'A4s', 'A3s']

sb_vs_bu_3bet_caution = ['ATo', 'KJo', '77', '66', 'T9s', 'J9s', 'Q9s', 'K9s', 'A8s', 'A7s', 'A6s', 'A3s', 'A2s']

sb_ranges_by_position = {
    'utg': (sb_vs_utg_3bet, sb_vs_utg_3bet_caution),
    'mp': (sb_vs_mp_3bet, sb_vs_mp_3bet_caution),
    'co': (sb_vs_co_3bet, sb_vs_co_3bet_caution),
    'bu': (sb_vs_bu_3bet, sb_vs_bu_3bet_caution)
}

# BB

bb_vs_utg_3bet = [
    "AA", "KK", "QQ", "JJ", "TT",
    "AKo",
    "AKs", "AQs", "AJs", "ATs", "KQs", "KJs", "KTs", "QJs", "QTs", "JTs", "A5s", "A4s"
]

bb_vs_utg_call = [
    "AQs", "AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
    "AKo", "AQo", "AJo", "KQo",
    "KTs", "K9s", "QTs", "Q9s", "JTs", "J9s", "T9s", 
    "JJ", "TT", "99", "98s", "88", "87s", "77", "76s", "66", "55", "44", "33", "22"
]

bb_vs_mp_3bet = bb_vs_utg_3bet + ["99"]

bb_vs_mp_call = bb_vs_utg_call + ["ATo", "KJo", "K8s", "T8s", "97s"]

bb_vs_co_3bet = bb_vs_mp_3bet + ["AQo", "A9s", "K9s", "Q9s", "J9s", "T9s"]

bb_vs_co_call = bb_vs_mp_call + ["65s", "54s", "86s", "K6s", "K5s", "Q8s", "Q7s", "J8s"]

bb_vs_bu_3bet = [
    "AA", "KK", "QQ", "JJ", "TT", "88", "77",
    "AKs", "AQs", "AJs", "ATs", "A9s", "A5s", "A4s", "A3s", 
    "AKo", "AQo",
    "KQs", "KJs", "KTs", "K9s", "QJs", "QTs", "Q9s", "JTs", "J9s", "J8s" "T9s", "T8s", "98s", "87s", "76s"
]

bb_vs_bu_call = [
    "A9s", "A8s", "A7s", "A6s", "A3s", "A2s",
    "AJo", "ATo", "A9o", "A8o", "A7o", "A5o",
    "KQo", "KJo", "KTo", "K9o", "QJo", "QTo", "JTo", "T9o"
    "88", "77", "66", "55", "44", "33", "22"
    "K9s", "K8s", "K7s", "K6s", "K5s", "K4s",
    "Q9s", "Q8s", "Q7s", "Q6s",
    "J9s", "J8s", "J7s",
    "T8s", "T7s",
    "97s", "86s", "75s", "64s",
    "87s", "76s", "65s", "54s"
]

bb_vs_sb_3bet = [ "AA", "KK", "QQ", "JJ", "TT", "88", "77",
    "AKs", "AQs", "AJs", "ATs", "A9s", "A5s", "A4s", "A3s", 
    "AKo", "AQo", "AJo", "A5o", "A4o", "A3o", "A2o"] + \
    ["KQo", "KJo", "K8o", "K7o", "K6o", "K5o"] + \
    ["Q9o", "Q8o"] + \
    ["J9o", "J8o", "T9o", "T8o"] + \
    ["KQs", "KJs", "KTs", "K9s", "K7s", "K6s"] + \
    ["QJs", "QTs", "Q9s"] + \
    ["JTs", "J9s", "J4s", "J3s"] + \
    ["T9s", "T8s", "T5s", "T4s", "T3s", "T2s"] + \
    ["98s", "97s"] + \
    ["87s", "86s"] + \
    ["76s", "75s"] + \
    ["65s", "54s"] + \
    ["54s"]

bb_vs_sb_call = ["99", "88", "77", "66", "55", "44", "33", "22"] + \
    ["AJo", "ATo"] + [f"A{i}o" for i in range(2, 10)] + \
    ["KQo", "KJo", "KTo"] + [f"K{i}o" for i in range(5, 10)] + \
    ["QJo", "QTo", "Q9o", "Q8o"] + \
    ["JTo", "J9o", "J8o", "T9o", "T8o", "98o", "87o", "76o", "65o"] + \
    ["A9s", "A8s", "A7s", "A6s", "A3s", "A2s"] + \
    ["KTs"] + [f"K{i}s" for i in range(2, 10)] + \
    ["QTs"] + [f"Q{i}s" for i in range(2, 10)] + \
    [f"J{i}s" for i in range(2, 10)] + \
    [f"T{i}s" for i in range(2, 10)] + \
    [f"9{i}s" for i in range(3, 9)] + \
    [f"8{i}s" for i in range(4, 8)] + \
    [f"7{i}s" for i in range(3, 7)] + \
    [f"6{i}s" for i in range(3, 6)] + \
    [f"5{i}s" for i in range(2, 5)] + \
    [f"4{i}s" for i in range(2, 4)] + \
    ["32s"]


bb_ranges_by_position = {
    'utg': (bb_vs_utg_3bet, bb_vs_utg_call),
    'mp': (bb_vs_mp_3bet, bb_vs_mp_call),
    'co': (bb_vs_co_3bet, bb_vs_co_call),
    'bu': (bb_vs_bu_3bet, bb_vs_bu_call),
    'sb': (bb_vs_sb_3bet, bb_vs_sb_call)
}


positions = ["utg", "mp", "co", "bu", "sb", "bb"]


def generate_hand():
    ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    suits = ["s", "o"]
    rank1 = random.choice(ranks)
    rank2 = random.choice(ranks)
    if ranks.index(rank1) > ranks.index(rank2):
        rank1, rank2 = rank2, rank1
    if rank1 == rank2:
        return f"{rank1}{rank2}"
    suit = random.choice(suits)
    return f"{rank1}{rank2}{suit}"


def poker_opening_trainer():

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--blinds', action='store_true')
    parser.add_argument('-nb', '--non-blinds', action='store_true')
    args = parser.parse_args()

    correct_answers = 0
    total_questions = 0

    print("Poker table 3-bet trainer (6-max, 5% rake).")
    print("Submit 'r' for raise, 'c' for call or 'f' for fold. Submit 'q' for quit.\n")

    while True:
        if args.blinds:
            position = random.choice(positions[-2:])
        elif args.non_blinds:
            position = random.choice(positions[1:-2])
        else:
            position = random.choice(positions[1:])
        
        opponent_position = random.choice(positions[:positions.index(position)])


        def render_pos(pos):
            if pos == position:
                return f"(you {position.upper()})"
            elif pos == opponent_position:
                return f"(opp {opponent_position.upper()})"
            return pos


        hand = generate_hand()
        pos = ' '.join(render_pos(i) for i in positions)
        if total_questions:
            print(f"Precicion: {correct_answers / total_questions:.2%} ({correct_answers}/{total_questions})\n")
        print(f"Position: [{pos}], Hand: {hand}. r/c/f?")

        user_input = input("Your answer: ").strip().lower()
        while user_input not in ['r', 'c', 'f', 'q']:
            user_input = input("Your answer: ").strip().lower()

        if user_input == "q":
            break

        total_questions += 1

        RED = '\033[41m'
        GRIN = '\033[42m'
        YELLOW = '\033[43m'
        END = '\033[0m'

        if position in ['mp', 'co', 'bu']:
            raise_range = default_3bet
            caution_range = default_3bet_caution
            call_range = []
        elif position == 'bb':
            raise_range, call_range = bb_ranges_by_position[opponent_position]
            caution_range = []
        elif position == 'sb':
            raise_range, caution_range = sb_ranges_by_position[opponent_position]
            call_range = []

        if user_input == "r":
            if hand in raise_range:
                if hand in caution_range:
                    print(YELLOW + "Correct! But raise with caution!" + END)
                elif hand in call_range:
                    print(YELLOW + "Correct! But call also an option" + END)
                else:
                    print(GRIN + "Correct!" + END)
                correct_answers += 1
            else:
                print(RED + f"Incorrect. Answer is: {'c' if hand in call_range else 'f'}" + END)
        elif user_input == "f":
            if hand in raise_range and hand in call_range:
                print(RED + f"Incorrect. Answer is: r | c" + END)
            elif hand in raise_range:
                print(RED + f"Incorrect. Answer is: r" + END)
            elif hand in call_range:
                print(RED + f"Incorrect. Answer is: c" + END)
            else:
                print(GRIN + "Correct!" + END)
                correct_answers += 1
        elif user_input == "c":
            if hand in call_range:
                if hand in raise_range:
                    print(YELLOW + "Correct! But raise also an option" + END)
                else:
                    print(GRIN + "Correct!" + END)
                correct_answers += 1
            else:
                print(RED + f"Incorrect. Answer is: {'r' if hand in raise_range else 'f'}" + END)



    print(f"Total precicion: {correct_answers / total_questions:.2%} ({correct_answers}/{total_questions})")

if __name__ == "__main__":
    poker_opening_trainer()
