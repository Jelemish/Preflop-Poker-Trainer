import random


utg_ranges = [
    "AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", 
    "AKo", "AQo", "AJo", "ATo", "KQo",
    "AKs", "AQs", "AJs", "ATs", "A9s", "KQs", "KJs", "KTs", "QJs", "QTs", "JTs", "T9s"
]
mp_ranges = utg_ranges + [f"A{i}s" for i in range(2, 10)] + ["55"]
co_ranges = mp_ranges + ['44'] + ['KTo', 'KJo', 'QTo', 'QJo', 'JTo'] + ['K9s', 'Q9s', 'J9s', 'K8s', 'Q8s', 'J8s', 'T8s', 'K7s'] + [f"{i+1}{i}s" for i in range(5, 9)]
bu_ranges = co_ranges + ['33', '22', 'A7o', 'A8o', 'A9o', 'A5o', 'A4o'] + ['K9o', 'Q9o', 'J9o', 'T9o', 'K8o', 'Q8o'] + [f"K{i}s" for i in range(2, 7)] + ['Q7s', 'J7s', 'T7s', 'Q6s', '43s', '54s'] + [f"{i+2}{i}s" for i in range(3, 8)]
sb_ranges = bu_ranges + [f"Q{i}s" for i in range(2, 6)] + [f"J{i}s" for i in range(5, 8)] + ['T6s', '96s']
open_ranges = {
    "utg": utg_ranges,
    "mp": mp_ranges,
    "co": co_ranges,
    "bu": bu_ranges,
    "sb": sb_ranges
}

positions = ["utg", "mp", "co", "bu", "sb"]

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
    correct_answers = 0
    total_questions = 0

    print("Poker table open trainer (6-max, 5% rake).")
    print("Submit 'r' for raise or 'f' for fold. Submit 'q' for quit.\n")

    while True:
        position = random.choice(positions)
        hand = generate_hand()
        pos = ' '.join(
            [('[' + p.upper() + ']' if p == position else p) for p in positions] + ['bb']
        )
        if total_questions:
            print(f"Precicion: {correct_answers / total_questions:.2%} ({correct_answers}/{total_questions})\n")
        print(f"Position: ({pos}), Hand: {hand}. r/f?")
        user_input = input("Your answer: ").strip().lower()

        if user_input == "q":
            break

        total_questions += 1
        correct_range = open_ranges[position]
        is_correct = (user_input == "r" and hand in correct_range) or (user_input == "f" and hand not in correct_range)

        RED = '\033[41m'
        GRIN = '\033[42m'
        END = '\033[0m'
        if is_correct:
            print(GRIN + "Correct!" + END)
            correct_answers += 1
        else:
            print(RED + f"Incorrect. Answer is: {'r' if hand in correct_range else 'f'}" + END)

    print(f"Total precicion: {correct_answers / total_questions:.2%} ({correct_answers}/{total_questions})")

if __name__ == "__main__":
    poker_opening_trainer()

