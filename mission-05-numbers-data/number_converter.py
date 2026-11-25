"""Convert a non-negative decimal integer to binary and hexadecimal."""


def convert_number(number: int) -> tuple[str, str]:
    """Return the binary and hexadecimal representations of *number*."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 0:
        raise ValueError("number must be non-negative")
    return format(number, "b"), format(number, "X")


def main() -> None:
    """Read a decimal integer and display its base-2 and base-16 forms."""
    raw_value = input("Enter a non-negative decimal integer: ").strip()
    try:
        number = int(raw_value, 10)
        binary, hexadecimal = convert_number(number)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    print(f"Binary: {binary}")
    print(f"Hexadecimal: {hexadecimal}")


if __name__ == "__main__":
    main()
