"""
avengers_quiz.py
================
"Which Avenger Are You?" — A personality quiz application.

HOW IT WORKS:
  - Each question has 4 answer choices.
  - Every answer maps a score to one or more Avenger traits (stored as a dict).
  - After all questions, scores are tallied and the Avenger with the highest
    score is returned as the user's result.

SCORING MODEL:
  Avengers: iron_man, captain_america, thor, black_widow,
            hulk, spider_man, black_panther, hawkeye
"""

# ---------------------------------------------------------------------------
# DATA: Questions, answers, and their trait scores
# ---------------------------------------------------------------------------

# Each question is a dict with:
#   "text"    — the question shown to the user
#   "options" — list of dicts, each with:
#                 "label"  — the answer text
#                 "scores" — dict mapping avenger keys → points awarded
QUESTIONS = [
    {
        "text": "How do you handle a crisis?",
        "options": [
            {"label": "I build a solution from scratch",              "scores": {"iron_man": 3, "black_panther": 1}},
            {"label": "I follow the plan and inspire others",         "scores": {"captain_america": 3, "hawkeye": 1}},
            {"label": "I hit it head-on — hard",                      "scores": {"thor": 2, "hulk": 2}},
            {"label": "I gather intel and strike precisely",          "scores": {"black_widow": 3, "hawkeye": 1}},
        ],
    },
    {
        "text": "What's your biggest strength?",
        "options": [
            {"label": "My intellect and resourcefulness",             "scores": {"iron_man": 3, "spider_man": 1}},
            {"label": "My unwavering moral compass",                  "scores": {"captain_america": 3, "black_panther": 1}},
            {"label": "My raw power and courage",                     "scores": {"thor": 3, "hulk": 1}},
            {"label": "My adaptability and precision",                "scores": {"black_widow": 2, "hawkeye": 2}},
        ],
    },
    {
        "text": "What do you do in your downtime?",
        "options": [
            {"label": "Tinker with gadgets and upgrade my gear",      "scores": {"iron_man": 3, "spider_man": 2}},
            {"label": "Work out or study history and strategy",       "scores": {"captain_america": 3, "black_panther": 1}},
            {"label": "Feast, tell stories, and celebrate",           "scores": {"thor": 3, "hawkeye": 1}},
            {"label": "Train in silence — skills don't maintain themselves", "scores": {"black_widow": 3, "hawkeye": 1}},
        ],
    },
    {
        "text": "How do people see you?",
        "options": [
            {"label": "Brilliant but a little arrogant",              "scores": {"iron_man": 3, "thor": 1}},
            {"label": "Honourable, dependable, a born leader",        "scores": {"captain_america": 3, "black_panther": 2}},
            {"label": "Intense — calm until suddenly not",            "scores": {"hulk": 3, "black_widow": 1}},
            {"label": "Friendly, funny, a bit chaotic",               "scores": {"spider_man": 3, "hawkeye": 1}},
        ],
    },
    {
        "text": "What motivates you most?",
        "options": [
            {"label": "Protecting my legacy and proving myself",      "scores": {"iron_man": 3, "spider_man": 1}},
            {"label": "Doing what's right, no matter the cost",       "scores": {"captain_america": 3, "black_panther": 1}},
            {"label": "Glory, honour, and protecting those I love",   "scores": {"thor": 3, "hawkeye": 1}},
            {"label": "Redeeming my past and protecting the innocent","scores": {"black_widow": 3, "hulk": 1}},
        ],
    },
    {
        "text": "Pick a superpower you'd want:",
        "options": [
            {"label": "Genius-level intellect + powered armour",      "scores": {"iron_man": 3}},
            {"label": "Peak human strength and an unbreakable shield","scores": {"captain_america": 3}},
            {"label": "The power of a god — lightning at my command", "scores": {"thor": 3}},
            {"label": "Incredible Hulk strength when angry",          "scores": {"hulk": 2, "black_widow": 1}},
        ],
    },
    {
        "text": "Your team is outnumbered. What do you do?",
        "options": [
            {"label": "Analyse the enemy and create a tactical plan", "scores": {"iron_man": 2, "black_panther": 2}},
            {"label": "Rally everyone — a united team never loses",   "scores": {"captain_america": 3, "thor": 1}},
            {"label": "Go straight for the biggest threat",           "scores": {"hulk": 3, "thor": 1}},
            {"label": "Flank them quietly from the shadows",          "scores": {"black_widow": 3, "hawkeye": 2}},
        ],
    },
    {
        "text": "Which word describes your leadership style?",
        "options": [
            {"label": "Visionary",                                    "scores": {"iron_man": 2, "black_panther": 2}},
            {"label": "Inspiring",                                    "scores": {"captain_america": 3, "thor": 1}},
            {"label": "Protective",                                   "scores": {"hulk": 2, "spider_man": 2}},
            {"label": "Calculated",                                   "scores": {"black_widow": 3, "hawkeye": 1}},
        ],
    },
]

# ---------------------------------------------------------------------------
# DATA: Avenger result profiles
# ---------------------------------------------------------------------------

# Each Avenger has a display name, emoji, and description shown at the end.
AVENGERS = {
    "iron_man":        {
        "name": "Iron Man",
        "emoji": "🦾",
        "description": (
            "You are Tony Stark — brilliant, bold, and always three steps ahead. "
            "You solve problems with ingenuity and aren't afraid to bet on yourself. "
            "Your confidence can read as arrogance, but results speak louder than critics."
        ),
    },
    "captain_america": {
        "name": "Captain America",
        "emoji": "🛡️",
        "description": (
            "You are Steve Rogers — a natural leader with an unshakeable sense of right and wrong. "
            "People trust you instinctively. You inspire others not through power, but through integrity."
        ),
    },
    "thor":            {
        "name": "Thor",
        "emoji": "⚡",
        "description": (
            "You are Thor Odinson — powerful, passionate, and fiercely loyal. "
            "You live for glory and protecting those you love. "
            "Your courage is legendary, even if your humility is still… a work in progress."
        ),
    },
    "black_widow":     {
        "name": "Black Widow",
        "emoji": "🕷️",
        "description": (
            "You are Natasha Romanoff — calm, calculated, and formidably skilled. "
            "You read a room in seconds, adapt instantly, and always have a contingency plan. "
            "Few people truly know you, but those who do know they can always count on you."
        ),
    },
    "hulk":            {
        "name": "The Hulk",
        "emoji": "💚",
        "description": (
            "You are Bruce Banner / The Hulk — a brilliant mind wrestling with extraordinary inner power. "
            "When pushed, you become unstoppable. Your intensity is your greatest gift and your greatest challenge."
        ),
    },
    "spider_man":      {
        "name": "Spider-Man",
        "emoji": "🕸️",
        "description": (
            "You are Peter Parker — quick-witted, good-hearted, and endlessly resourceful. "
            "You crack jokes under pressure and always show up when it matters. "
            "With great power comes great responsibility — and you take that seriously."
        ),
    },
    "black_panther":   {
        "name": "Black Panther",
        "emoji": "🐾",
        "description": (
            "You are T'Challa — a composed, strategic king who leads with both wisdom and strength. "
            "You balance duty and compassion effortlessly and command respect without demanding it."
        ),
    },
    "hawkeye":         {
        "name": "Hawkeye",
        "emoji": "🎯",
        "description": (
            "You are Clint Barton — dependable, precise, and quietly heroic. "
            "No powers, no problem. You show up, focus on what matters, and never miss. "
            "The most human Avenger — and arguably the most grounded."
        ),
    },
}

# ---------------------------------------------------------------------------
# CORE LOGIC: Score calculation
# ---------------------------------------------------------------------------

def calculate_result(answers: list[dict]) -> dict:
    """
    Tallies scores from the user's answers and returns the best-matching Avenger.

    Args:
        answers: A list of score-dicts, one per question.
                 e.g. [{"iron_man": 3}, {"captain_america": 3, "black_panther": 1}, ...]

    Returns:
        The Avenger profile dict for the highest-scoring Avenger.
    """
    # Initialise every Avenger's total score at zero
    totals = {key: 0 for key in AVENGERS}

    # Loop through each answer the user gave and add its scores to the totals
    for score_dict in answers:
        for avenger_key, points in score_dict.items():
            totals[avenger_key] += points

    # Find the Avenger key with the highest total score
    # max() with key=lambda lets us compare by the dict values, not the keys
    best_match_key = max(totals, key=lambda k: totals[k])

    return AVENGERS[best_match_key]


# ---------------------------------------------------------------------------
# CLI INTERFACE: Run the quiz in the terminal
# ---------------------------------------------------------------------------

def run_quiz() -> None:
    """
    Runs the quiz interactively in the terminal.
    Collects one answer per question, then prints the result.
    """
    print("\n" + "=" * 55)
    print("       ✨  WHICH AVENGER ARE YOU?  ✨")
    print("=" * 55)
    print("Answer 8 questions to discover your inner Avenger.\n")

    # This list accumulates the score-dict for each chosen answer
    user_answers: list[dict] = []

    # Iterate over questions with a 1-based index for display
    for i, question in enumerate(QUESTIONS, start=1):
        print(f"Q{i}: {question['text']}")

        # Print each lettered option (A, B, C, D)
        for j, option in enumerate(question["options"]):
            letter = chr(65 + j)  # 65 = ASCII 'A'
            print(f"  {letter}) {option['label']}")

        # --- Input validation loop ---
        # Keep asking until the user gives a valid A/B/C/D response
        valid_letters = [chr(65 + j) for j in range(len(question["options"]))]
        while True:
            choice = input(f"Your answer ({'/'.join(valid_letters)}): ").strip().upper()
            if choice in valid_letters:
                break
            print(f"  ⚠ Please enter one of: {', '.join(valid_letters)}")

        # Convert letter back to index (A=0, B=1, …) and store its scores
        chosen_index = ord(choice) - 65
        user_answers.append(question["options"][chosen_index]["scores"])
        print()  # blank line between questions

    # --- Calculate and display the result ---
    result = calculate_result(user_answers)

    print("=" * 55)
    print(f"  {result['emoji']}  YOU ARE: {result['name'].upper()}  {result['emoji']}")
    print("=" * 55)
    print(f"\n{result['description']}\n")


# ---------------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------------

def main() -> None:
    """Main entry point. Runs the quiz and handles a graceful Ctrl+C exit."""
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\nQuiz cancelled. Assemble another time, hero. 👋")


if __name__ == "__main__":
    main()