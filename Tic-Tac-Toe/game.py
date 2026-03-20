#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║       TIC-TAC-TOE: TEXT ADVENTURE        ║
║   A classic game with a narrative twist  ║
╚══════════════════════════════════════════╝
"""

import os
import random
import time


# ─── Constants ────────────────────────────────────────────────────────────────

EMPTY  = " "
PLAYER = "X"
AI     = "O"

POSITION_NAMES = {
    1: "top-left",    2: "top-center",    3: "top-right",
    4: "middle-left", 5: "center",        6: "middle-right",
    7: "bottom-left", 8: "bottom-center", 9: "bottom-right",
}

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6),             # diagonals
]

AI_FLAVOR = [
    "The machine hums quietly and places its mark...",
    "Cold calculation flickers behind silicon eyes...",
    "Circuits fire. The AI makes its move...",
    "After a nanosecond of deliberation, the AI acts...",
    "The AI studies the board... and strikes.",
]


# ─── Display ──────────────────────────────────────────────────────────────────

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    print("""
╔══════════════════════════════════════════╗
║       TIC-TAC-TOE: TEXT ADVENTURE        ║
╚══════════════════════════════════════════╝
""")


def print_board(board: list[str]) -> None:
    """Render the board with position hints on a reference grid."""
    def cell(idx):
        val = board[idx]
        if val == PLAYER:
            return f" \033[1;34m{val}\033[0m "   # bold blue X
        elif val == AI:
            return f" \033[1;31m{val}\033[0m "   # bold red O
        else:
            return f" \033[2m{idx + 1}\033[0m "  # dim position number

    print()
    print("    BOARD              POSITIONS")
    print(" ───┬───┬───         ───┬───┬───")
    for row in range(3):
        i = row * 3
        board_row  = f"{cell(i)}│{cell(i+1)}│{cell(i+2)}"
        print(f" {board_row}      {i+1:^3}│{i+2:^3}│{i+3:^3}")
        if row < 2:
            print(" ───┼───┼───         ───┼───┼───")
    print(" ───┴───┴───         ───┴───┴───")
    print()


def slow_print(text: str, delay: float = 0.03) -> None:
    """Print text character-by-character for dramatic effect."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


# ─── Game Logic ───────────────────────────────────────────────────────────────

def check_winner(board: list[str]) -> str | None:
    """Return the winning mark, 'draw', or None."""
    for a, b, c in WIN_COMBOS:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    if EMPTY not in board:
        return "draw"
    return None


def get_available(board: list[str]) -> list[int]:
    return [i for i, v in enumerate(board) if v == EMPTY]


# ─── AI (Minimax) ─────────────────────────────────────────────────────────────

def minimax(board: list[str], is_maximizing: bool, depth: int = 0) -> int:
    result = check_winner(board)
    if result == AI:
        return 10 - depth
    if result == PLAYER:
        return depth - 10
    if result == "draw":
        return 0

    available = get_available(board)

    if is_maximizing:
        best = -100
        for idx in available:
            board[idx] = AI
            score = minimax(board, False, depth + 1)
            board[idx] = EMPTY
            best = max(best, score)
        return best
    else:
        best = 100
        for idx in available:
            board[idx] = PLAYER
            score = minimax(board, True, depth + 1)
            board[idx] = EMPTY
            best = min(best, score)
        return best


def ai_move(board: list[str]) -> int:
    """Return the best move index for the AI."""
    available = get_available(board)
    best_score = -100
    best_idx   = available[0]

    for idx in available:
        board[idx] = AI
        score = minimax(board, False)
        board[idx] = EMPTY
        if score > best_score:
            best_score = score
            best_idx   = idx

    return best_idx


# ─── Input Helpers ────────────────────────────────────────────────────────────

def get_player_move(board: list[str]) -> int:
    """
    Accept input as a number (1-9) or a natural-language position name.
    Returns a 0-based board index.
    """
    name_to_idx = {name: idx for idx, name in POSITION_NAMES.items()}

    while True:
        raw = input("\n> ").strip().lower()

        # Try numeric first
        if raw.isdigit():
            pos = int(raw)
            if 1 <= pos <= 9:
                idx = pos - 1
                if board[idx] == EMPTY:
                    return idx
                else:
                    print(f"  ✗ The {POSITION_NAMES[pos]} square is already taken. Try another.")
                    continue
            else:
                print("  ✗ Please enter a number between 1 and 9.")
                continue

        # Try natural-language match — exact first, then partial
        matched = [name for name in name_to_idx if raw == name]
        if not matched:
            matched = [name for name in name_to_idx if raw in name or name in raw]
        if len(matched) == 1:
            pos = name_to_idx[matched[0]]
            idx = pos - 1
            if board[idx] == EMPTY:
                print(f"  → Placing your mark at the {matched[0]}...")
                return idx
            else:
                print(f"  ✗ The {matched[0]} square is already taken. Try another.")
                continue
        elif len(matched) > 1:
            print(f"  ✗ Ambiguous! Did you mean: {', '.join(matched)}?")
            continue

        # Quit/help commands
        if raw in ("quit", "exit", "q"):
            print("\n  You abandon the game. Farewell, adventurer.\n")
            raise SystemExit

        if raw in ("help", "?", "h"):
            print_help()
            print_board(board)
            continue

        print("  ✗ I don't understand that. Try a number (1-9) or a position name like 'center' or 'top-left'.")


def print_help():
    print("""
  ┌─────────────────────────────────────────┐
  │              HOW TO PLAY                │
  ├─────────────────────────────────────────┤
  │ Enter a number 1–9 to place your mark,  │
  │ or type a position name, e.g.:          │
  │   "center", "top-left", "bottom-right"  │
  │                                         │
  │ Commands:  help | quit                  │
  └─────────────────────────────────────────┘""")


# ─── Narrative Strings ────────────────────────────────────────────────────────

INTRO = """\
You stand before a weathered wooden table.
On its surface, a grid of nine squares has been carved deep into the grain.

A mysterious opponent — part silicon, part shadow — sits across from you.

"X marks your fate," it whispers. "I shall be the O that undoes you."

The challenge is set. Three in a row wins all.
"""

WIN_MSG   = "Glory! You've outwitted the machine. The grid bows to your will."
LOSE_MSG  = "The AI's circles close around you. Defeat. But perhaps... a rematch?"
DRAW_MSG  = "A perfect stalemate. Neither fate nor algorithm could claim victory today."


def game_over_message(result: str, board: list[str]) -> None:
    print_board(board)
    print()
    if result == PLAYER:
        slow_print(f"  🏆  {WIN_MSG}")
    elif result == AI:
        slow_print(f"  💀  {LOSE_MSG}")
    else:
        slow_print(f"  🤝  {DRAW_MSG}")
    print()


# ─── Main Game Loop ───────────────────────────────────────────────────────────

def choose_difficulty() -> str:
    print("  Choose your difficulty:")
    print("    [1] Easy    — the AI plays randomly")
    print("    [2] Medium  — the AI plays smart sometimes")
    print("    [3] Hard    — the AI is unbeatable (Minimax)")
    while True:
        choice = input("\n> ").strip()
        if choice in ("1", "easy"):
            return "easy"
        if choice in ("2", "medium"):
            return "medium"
        if choice in ("3", "hard"):
            return "hard"
        print("  ✗ Please enter 1, 2, or 3.")


def ai_move_by_difficulty(board: list[str], difficulty: str) -> int:
    available = get_available(board)
    if difficulty == "easy":
        return random.choice(available)
    if difficulty == "medium":
        # 50% chance of best move, 50% random
        if random.random() < 0.5:
            return ai_move(board)
        return random.choice(available)
    # hard
    return ai_move(board)


def play_game():
    clear_screen()
    print_banner()
    slow_print(INTRO, delay=0.02)

    difficulty = choose_difficulty()
    print(f"\n  Difficulty set to: {difficulty.upper()}\n")
    time.sleep(0.8)

    board   = [EMPTY] * 9
    turn    = PLAYER   # Player always goes first
    move_no = 0

    print_board(board)

    while True:
        result = check_winner(board)
        if result:
            game_over_message(result, board)
            break

        if turn == PLAYER:
            move_no += 1
            print(f"  ─── Move {move_no}: Your turn (X) ───────────────")
            print("  Where do you place your X? (Enter 1-9 or position name, 'help' for guide)")
            idx = get_player_move(board)
            board[idx] = PLAYER
            print_board(board)

            result = check_winner(board)
            if result:
                game_over_message(result, board)
                break

            turn = AI

        else:
            print(f"  ─── The AI ponders its move (O) ──────────────")
            slow_print(f"  {random.choice(AI_FLAVOR)}", delay=0.025)
            time.sleep(0.5)
            idx = ai_move_by_difficulty(board, difficulty)
            board[idx] = AI
            pos_name = POSITION_NAMES[idx + 1]
            print(f"  The AI claims the \033[1;31m{pos_name}\033[0m square.")
            print_board(board)

            result = check_winner(board)
            if result:
                game_over_message(result, board)
                break

            turn = PLAYER


def main():
    while True:
        play_game()
        print("  Play again? [y/n]")
        again = input("> ").strip().lower()
        if again not in ("y", "yes"):
            slow_print("\n  The grid fades. Until next time, adventurer.\n", delay=0.025)
            break
        clear_screen()
        print_banner()


if __name__ == "__main__":
    main()