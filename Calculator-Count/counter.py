"""
countdown_calculator.py
=======================
Calculate the time difference between two dates/datetimes.

Features
--------
- Accepts dates (YYYY-MM-DD) or full datetimes (YYYY-MM-DD HH:MM:SS)
- Breaks the difference down into years, months, weeks, days, hours, minutes, seconds
- Shows total values in each unit (e.g. total hours between the two moments)
- Indicates whether the second date is in the past, present, or future relative to the first
- "Countdown mode": omit the second date to compare against right now
- Built-in self-tests (python countdown_calculator.py test)

Usage examples
--------------
  # Difference between two dates
  python countdown_calculator.py "2000-01-01" "2025-03-20"

  # Difference between two datetimes
  python countdown_calculator.py "2025-01-01 08:00:00" "2025-03-20 17:30:00"

  # Countdown from NOW to a future date
  python countdown_calculator.py "2025-12-31"

  # Run self-tests
  python countdown_calculator.py test
"""

import argparse
import sys
from datetime import datetime, timezone

# ── Date parsing ─────────────────────────────────────────────────────────────

DATE_FORMATS = [
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d",
    "%d/%m/%Y %H:%M:%S",
    "%d/%m/%Y %H:%M",
    "%d/%m/%Y",
    "%m/%d/%Y %H:%M:%S",
    "%m/%d/%Y %H:%M",
    "%m/%d/%Y",
]


def parse_date(text: str) -> datetime:
    """Try multiple formats and return the first that parses successfully."""
    text = text.strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    raise ValueError(
        f"Cannot parse date/time: {text!r}\n"
        "Accepted formats: YYYY-MM-DD, YYYY-MM-DD HH:MM:SS, DD/MM/YYYY, MM/DD/YYYY, etc."
    )


# ── Core calculation ──────────────────────────────────────────────────────────

class Countdown:
    """Holds the decomposed difference between two datetime objects."""

    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end

        # Total signed delta in seconds (positive = end is after start)
        delta = end - start
        self.total_seconds: int = int(delta.total_seconds())
        self.is_future: bool = self.total_seconds > 0
        self.is_same: bool = self.total_seconds == 0

        abs_seconds = abs(self.total_seconds)

        # ── Totals in each unit ───────────────────────────────────────────
        self.total_minutes: int = abs_seconds // 60
        self.total_hours: int = abs_seconds // 3600
        self.total_days: int = abs_seconds // 86400
        self.total_weeks: int = abs_seconds // (7 * 86400)

        # ── Broken-down components (largest-first decomposition) ──────────
        remaining = abs_seconds

        # Years (approximate: 365.2425 days)
        YEAR_SECS = 365.2425 * 86400
        self.years: int = int(remaining / YEAR_SECS)
        remaining -= int(self.years * YEAR_SECS)

        # Months (approximate: 30.436875 days)
        MONTH_SECS = 30.436875 * 86400
        self.months: int = int(remaining / MONTH_SECS)
        remaining -= int(self.months * MONTH_SECS)

        self.weeks: int = remaining // (7 * 86400)
        remaining -= self.weeks * 7 * 86400

        self.days: int = remaining // 86400
        remaining -= self.days * 86400

        self.hours: int = remaining // 3600
        remaining -= self.hours * 3600

        self.minutes: int = remaining // 60
        self.seconds: int = remaining % 60


def _plural(n: int, unit: str) -> str:
    return f"{n} {unit}{'s' if n != 1 else ''}"


def format_breakdown(cd: Countdown) -> str:
    """Return a multi-line human-readable report."""
    lines = []

    # ── Header ────────────────────────────────────────────────────────────
    lines.append("=" * 56)
    lines.append("  COUNTDOWN CALCULATOR")
    lines.append("=" * 56)
    lines.append(f"  From : {cd.start.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"  To   : {cd.end.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 56)

    if cd.is_same:
        lines.append("  ⏱  The two dates are identical.")
        lines.append("=" * 56)
        return "\n".join(lines)

    direction = "FUTURE  ▶" if cd.is_future else "◀  PAST"
    lines.append(f"  Direction : {direction}")
    lines.append("")

    # ── Decomposed breakdown ──────────────────────────────────────────────
    lines.append("  ── Broken down ─────────────────────────────────")
    parts = []
    if cd.years:   parts.append(_plural(cd.years,   "year"))
    if cd.months:  parts.append(_plural(cd.months,  "month"))
    if cd.weeks:   parts.append(_plural(cd.weeks,   "week"))
    if cd.days:    parts.append(_plural(cd.days,    "day"))
    if cd.hours:   parts.append(_plural(cd.hours,   "hour"))
    if cd.minutes: parts.append(_plural(cd.minutes, "minute"))
    if cd.seconds: parts.append(_plural(cd.seconds, "second"))

    if not parts:
        parts = ["less than 1 second"]

    lines.append("  " + ", ".join(parts))
    lines.append("")

    # ── Totals in each unit ───────────────────────────────────────────────
    lines.append("  ── Totals ──────────────────────────────────────")
    lines.append(f"  {cd.total_days:>12,}  days")
    lines.append(f"  {cd.total_hours:>12,}  hours")
    lines.append(f"  {cd.total_minutes:>12,}  minutes")
    lines.append(f"  {abs(cd.total_seconds):>12,}  seconds")
    lines.append("=" * 56)
    return "\n".join(lines)


# ── Self-tests ────────────────────────────────────────────────────────────────

def run_tests() -> None:
    failures: list[str] = []

    def check(label: str, got, expected):
        if got != expected:
            failures.append(f"  FAIL [{label}]\n    got {got!r}, expected {expected!r}")
        else:
            print(f"  PASS [{label}]")

    print("\n── parse_date tests ──")
    check("ISO date", parse_date("2025-03-20"), datetime(2025, 3, 20))
    check("ISO datetime", parse_date("2025-03-20 14:30:00"), datetime(2025, 3, 20, 14, 30, 0))
    check("ISO datetime HH:MM", parse_date("2025-03-20 14:30"), datetime(2025, 3, 20, 14, 30))
    check("DD/MM/YYYY", parse_date("20/03/2025"), datetime(2025, 3, 20))
    check("MM/DD/YYYY", parse_date("03/20/2025"), datetime(2025, 3, 20))

    try:
        parse_date("not-a-date")
        failures.append("  FAIL [bad date should raise ValueError]")
    except ValueError:
        print("  PASS [bad date raises ValueError]")

    print("\n── Countdown arithmetic tests ──")
    # Exactly 1 day
    cd = Countdown(datetime(2025, 1, 1), datetime(2025, 1, 2))
    check("1 day: total_days", cd.total_days, 1)
    check("1 day: total_hours", cd.total_hours, 24)
    check("1 day: total_minutes", cd.total_minutes, 1440)
    check("1 day: total_seconds", abs(cd.total_seconds), 86400)
    check("1 day: is_future", cd.is_future, True)
    check("1 day: days component", cd.days, 1)
    check("1 day: hours component", cd.hours, 0)

    # Exactly 0
    cd0 = Countdown(datetime(2025, 6, 15), datetime(2025, 6, 15))
    check("same date: is_same", cd0.is_same, True)
    check("same date: total_seconds", cd0.total_seconds, 0)

    # Past direction
    cd_past = Countdown(datetime(2025, 3, 20), datetime(2020, 1, 1))
    check("past direction: is_future", cd_past.is_future, False)
    check("past direction: is_same", cd_past.is_same, False)

    # Exactly 1 hour
    cd_hr = Countdown(datetime(2025, 1, 1, 12, 0, 0), datetime(2025, 1, 1, 13, 0, 0))
    check("1 hour: total_hours", cd_hr.total_hours, 1)
    check("1 hour: total_minutes", cd_hr.total_minutes, 60)
    check("1 hour: hours component", cd_hr.hours, 1)
    check("1 hour: days component", cd_hr.days, 0)

    # Mixed hours and minutes
    cd_mix = Countdown(datetime(2025, 1, 1, 0, 0, 0), datetime(2025, 1, 1, 2, 30, 45))
    check("2h30m45s: total_seconds", abs(cd_mix.total_seconds), 9045)
    check("2h30m45s: hours component", cd_mix.hours, 2)
    check("2h30m45s: minutes component", cd_mix.minutes, 30)
    check("2h30m45s: seconds component", cd_mix.seconds, 45)

    # Milestone: New Year 2000 → 2025-03-20  (9210 days)
    cd_ny = Countdown(datetime(2000, 1, 1), datetime(2025, 3, 20))
    check("2000-01-01 → 2025-03-20: total_days", cd_ny.total_days, 9210)
    check("2000-01-01 → 2025-03-20: total_hours", cd_ny.total_hours, 9210 * 24)

    # Leap year: 2024-02-28 → 2024-03-01 = 2 days (2024 is a leap year)
    cd_leap = Countdown(datetime(2024, 2, 28), datetime(2024, 3, 1))
    check("leap year 2024-02-28 → 2024-03-01: total_days", cd_leap.total_days, 2)

    # Non-leap year: 2023-02-28 → 2023-03-01 = 1 day
    cd_nonleap = Countdown(datetime(2023, 2, 28), datetime(2023, 3, 1))
    check("non-leap 2023-02-28 → 2023-03-01: total_days", cd_nonleap.total_days, 1)

    print()
    if failures:
        print(f"❌  {len(failures)} test(s) FAILED:")
        for f in failures:
            print(f)
        sys.exit(1)
    else:
        print("✅  All tests passed.")


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="countdown_calculator",
        description="Calculate the time between two dates/datetimes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "start",
        nargs="?",
        help=(
            "Start date/datetime  (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS). "
            "If this is the only date supplied it is treated as the TARGET and "
            "compared against NOW."
        ),
    )
    parser.add_argument(
        "end",
        nargs="?",
        default=None,
        help="End date/datetime. Omit to use the current date/time.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # ── test mode ─────────────────────────────────────────────────────────
    if args.start and args.start.lower() == "test":
        run_tests()
        return

    # ── need at least one date ─────────────────────────────────────────────
    if not args.start:
        parser.print_help()
        sys.exit(0)

    try:
        start = parse_date(args.start)
        if args.end:
            end = parse_date(args.end)
        else:
            # Countdown mode: compare against now (strip microseconds for clean display)
            end = datetime.now().replace(microsecond=0)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    cd = Countdown(start, end)
    print(format_breakdown(cd))


if __name__ == "__main__":
    main()

#---------------------------------------------------------------------------------
# Sample command line code.
#---------------------------------------------------------------------------------
# Between two specific dates
#python counter.py "2000-01-01" "2025-12-31"

# Full datetime precision
#python counter.py "2025-01-01 09:00:00" "2025-06-30 17:00:00"

# Countdown from a target date to RIGHT NOW
#python counter.py "2025-12-25"

# Self-tests
#python counter.py test
#---------------------------------------------------------------------------------