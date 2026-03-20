"""
text_encryptor.py
=================
A substitution-cipher text encryption/decryption tool.

Supports three cipher modes:
  1. Caesar Cipher     – shift each letter by a fixed number of positions
  2. ROT13             – a fixed Caesar shift of 13 (self-inverse)
  3. Custom Key Cipher – supply a full 26-letter substitution alphabet

Usage examples
--------------
  # Caesar cipher, shift = 3
  python text_encryptor.py encrypt "Hello, World!" --mode caesar --shift 3

  # Decrypt a Caesar-encoded message
  python text_encryptor.py decrypt "Khoor, Zruog!" --mode caesar --shift 3

  # ROT13 (encrypt and decrypt are identical)
  python text_encryptor.py encrypt "Hello, World!" --mode rot13

  # Custom key cipher
  python text_encryptor.py encrypt "Hello, World!" --mode custom \
      --key "ZYXWVUTSRQPONMLKJIHGFEDCBA"

  # Run built-in self-tests
  python text_encryptor.py test
"""

import argparse
import string
import sys


# ---------------------------------------------------------------------------
# Core cipher helpers
# ---------------------------------------------------------------------------

ALPHABET = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def _validate_key(key: str) -> str:
    """Return the key in uppercase after verifying it is a valid 26-letter permutation."""
    key = key.upper()
    if len(key) != 26:
        raise ValueError(f"Custom key must be exactly 26 letters; got {len(key)}.")
    if set(key) != set(ALPHABET):
        raise ValueError("Custom key must contain every letter A-Z exactly once.")
    return key


def _build_table(key: str, encrypt: bool) -> dict[str, str]:
    """
    Build a character-translation mapping.

    encrypt=True  : plaintext  → ciphertext
    encrypt=False : ciphertext → plaintext
    """
    if encrypt:
        return {p: c for p, c in zip(ALPHABET, key)}
    else:
        return {c: p for p, c in zip(ALPHABET, key)}


def _apply_table(text: str, table: dict[str, str]) -> str:
    """Apply a substitution table to *text*, preserving case and non-alpha chars."""
    result = []
    for ch in text:
        upper = ch.upper()
        if upper in table:
            substituted = table[upper]
            # Preserve original case
            result.append(substituted if ch.isupper() else substituted.lower())
        else:
            result.append(ch)  # spaces, digits, punctuation unchanged
    return "".join(result)


# ---------------------------------------------------------------------------
# Cipher modes
# ---------------------------------------------------------------------------

def caesar_key(shift: int) -> str:
    """Generate the substitution key for a Caesar cipher with the given shift."""
    shift = shift % 26
    return ALPHABET[shift:] + ALPHABET[:shift]


def rot13_key() -> str:
    """ROT13 is simply a Caesar cipher with shift=13."""
    return caesar_key(13)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def encrypt(text: str, mode: str = "caesar", shift: int = 3, key: str = "") -> str:
    """
    Encrypt *text* using the chosen cipher mode.

    Parameters
    ----------
    text  : plaintext string
    mode  : 'caesar' | 'rot13' | 'custom'
    shift : shift amount (Caesar only)
    key   : 26-letter substitution alphabet (custom only)

    Returns
    -------
    Encrypted string with non-alpha characters unchanged.
    """
    cipher_key = _resolve_key(mode, shift, key)
    table = _build_table(cipher_key, encrypt=True)
    return _apply_table(text, table)


def decrypt(text: str, mode: str = "caesar", shift: int = 3, key: str = "") -> str:
    """
    Decrypt *text* using the chosen cipher mode.

    Parameters
    ----------
    text  : ciphertext string
    mode  : 'caesar' | 'rot13' | 'custom'
    shift : shift amount used during encryption (Caesar only)
    key   : 26-letter substitution alphabet used during encryption (custom only)

    Returns
    -------
    Decrypted string with non-alpha characters unchanged.
    """
    cipher_key = _resolve_key(mode, shift, key)
    table = _build_table(cipher_key, encrypt=False)
    return _apply_table(text, table)


def _resolve_key(mode: str, shift: int, key: str) -> str:
    mode = mode.lower()
    if mode == "caesar":
        return caesar_key(shift)
    elif mode == "rot13":
        return rot13_key()
    elif mode == "custom":
        if not key:
            raise ValueError("A --key value is required for custom mode.")
        return _validate_key(key)
    else:
        raise ValueError(f"Unknown mode '{mode}'. Choose: caesar, rot13, custom.")


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def run_tests() -> None:
    """Run a suite of correctness checks and print a summary."""
    failures: list[str] = []

    def check(label: str, got, expected):
        if got != expected:
            failures.append(f"  FAIL [{label}]\n    got:      {got!r}\n    expected: {expected!r}")
        else:
            print(f"  PASS [{label}]")

    print("\n── Caesar cipher tests ──")
    check("caesar encrypt shift=3", encrypt("Hello, World!", "caesar", 3), "Khoor, Zruog!")
    check("caesar decrypt shift=3", decrypt("Khoor, Zruog!", "caesar", 3), "Hello, World!")
    check("caesar encrypt shift=0 (identity)", encrypt("ABC", "caesar", 0), "ABC")
    check("caesar encrypt shift=26 (full wrap)", encrypt("ABC", "caesar", 26), "ABC")
    check("caesar preserves digits", encrypt("abc123", "caesar", 1), "bcd123")
    check("caesar preserves punctuation", encrypt("Hi!", "caesar", 1), "Ij!")
    check("caesar case preservation lower", encrypt("hello", "caesar", 3), "khoor")
    check("caesar case preservation upper", encrypt("HELLO", "caesar", 3), "KHOOR")
    check("caesar round-trip shift=13", decrypt(encrypt("Test message.", "caesar", 13), "caesar", 13), "Test message.")
    check("caesar round-trip shift=7", decrypt(encrypt("Python 3.12!", "caesar", 7), "caesar", 7), "Python 3.12!")

    print("\n── ROT13 tests ──")
    check("rot13 encrypt", encrypt("Hello, World!", "rot13"), "Uryyb, Jbeyq!")
    check("rot13 is self-inverse", decrypt(encrypt("Hello, World!", "rot13"), "rot13"), "Hello, World!")
    check("rot13 round-trip full sentence",
          decrypt(encrypt("The quick brown fox jumps over the lazy dog.", "rot13"), "rot13"),
          "The quick brown fox jumps over the lazy dog.")

    print("\n── Custom key cipher tests ──")
    atbash = "ZYXWVUTSRQPONMLKJIHGFEDCBA"  # A↔Z, B↔Y, …
    check("atbash encrypt A→Z", encrypt("ABC", "custom", key=atbash), "ZYX")
    check("atbash decrypt Z→A", decrypt("ZYX", "custom", key=atbash), "ABC")
    check("atbash is self-inverse",
          decrypt(encrypt("Hello World", "custom", key=atbash), "custom", key=atbash),
          "Hello World")
    check("custom preserves non-alpha", encrypt("Hi, 2024!", "custom", key=atbash), "Sr, 2024!")

    print("\n── Edge-case tests ──")
    check("empty string", encrypt("", "caesar", 3), "")
    check("all non-alpha", encrypt("1234 !@#$", "caesar", 5), "1234 !@#$")
    check("full pangram round-trip",
          decrypt(encrypt("The quick brown fox jumps over the lazy dog", "caesar", 17), "caesar", 17),
          "The quick brown fox jumps over the lazy dog")

    print("\n── Validation tests ──")
    try:
        _validate_key("ABCDEFGHIJKLMNOPQRSTUVWXY")   # only 25 chars
        failures.append("  FAIL [short key should raise ValueError]")
    except ValueError:
        print("  PASS [short key raises ValueError]")

    try:
        _validate_key("AABCDEFGHIJKLMNOPQRSTUVWX")   # duplicate 'A'
        failures.append("  FAIL [duplicate-letter key should raise ValueError]")
    except ValueError:
        print("  PASS [duplicate-letter key raises ValueError]")

    # Summary
    print()
    if failures:
        print(f"❌  {len(failures)} test(s) FAILED:")
        for f in failures:
            print(f)
        sys.exit(1)
    else:
        print("✅  All tests passed.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="text_encryptor",
        description="Substitution-cipher text encryptor/decryptor.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Shared arguments for encrypt / decrypt
    def add_cipher_args(p):
        p.add_argument("text", help="Text to process (wrap in quotes if it contains spaces).")
        p.add_argument(
            "--mode", choices=["caesar", "rot13", "custom"], default="caesar",
            help="Cipher mode (default: caesar).",
        )
        p.add_argument(
            "--shift", type=int, default=3,
            help="Shift amount for Caesar cipher (default: 3).",
        )
        p.add_argument(
            "--key", default="",
            help="26-letter substitution key for custom mode (e.g. ZYXWVUTSRQPONMLKJIHGFEDCBA).",
        )

    enc = subparsers.add_parser("encrypt", help="Encrypt plaintext.")
    add_cipher_args(enc)

    dec = subparsers.add_parser("decrypt", help="Decrypt ciphertext.")
    add_cipher_args(dec)

    subparsers.add_parser("test", help="Run built-in self-tests.")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "test":
        run_tests()
        return

    try:
        if args.command == "encrypt":
            result = encrypt(args.text, args.mode, args.shift, args.key)
            label = "Encrypted"
        elif args.command == "decrypt":
            result = decrypt(args.text, args.mode, args.shift, args.key)
            label = "Decrypted"
        else:
            run_tests()
            return
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Input   : {args.text}")
    print(f"{label}: {result}")


if __name__ == "__main__":
    main()
    
#---------------------------------------------------------------------------------
# Sample command line code.
#---------------------------------------------------------------------------------
# Test run
# python generator.py 'test'
# -or-
# python generator.py

# Encrypt
# python generator.py 'encrypt' 'sample text'

# Decrypt
# python generator.py 'decrypt' 'sample text'