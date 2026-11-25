"""Two Robots in an Elevator — make.fun program/v1 entry.

Writes one line of awkward robot small talk to /output/entry.txt.
"""

import os

LINE = (
    "I have simulated this conversation 14,000 times. "
    "In every version I open with 'nice shaft' and you pretend to reboot."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
