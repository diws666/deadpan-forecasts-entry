"""Deadpan forecast entry: writes one funny line to /output/entry.txt."""

_PARTS = [
    "In Gloomsbury, expect overcast skies and a 90% chance of rain ",
    "that falls upwards. ",
    "Umbrellas optional; gravity, negotiable.",
]
ENTRY = "".join(_PARTS)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
