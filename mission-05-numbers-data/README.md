
# Mission 5 — Numbers and Data

## 1. Task / objective
The objective was to understand decimal, binary and hexadecimal number systems, verify conversions using Python, create a number converter and learn about text encoding.

## 2. Work completed
- Converted decimal, binary and hexadecimal numbers manually.
- Checked conversions using Python.
- Created `number_converter.py` (implementation completed as part of this repository review).
- Tested the converter using three positive numbers.
- Studied ASCII and UTF-8 encoding.

### Manual conversions
| Conversion | Answer |
|---|---:|
| Decimal 13 to binary | 1101 |
| Decimal 25 to binary | 11001 |
| Binary 1010 to decimal | 10 |
| Binary 1101 to decimal | 13 |
| Hexadecimal A to decimal | 10 |
| Hexadecimal 1F to decimal | 31 |
| Binary 1111 to hexadecimal | F |

### Python verification
| Python expression | Result |
|---|---|
| `bin(13)` | `0b1101` |
| `bin(25)` | `0b11001` |
| `int("1010", 2)` | `10` |
| `int("1101", 2)` | `13` |
| `int("A", 16)` | `10` |
| `int("1F", 16)` | `31` |
| `hex(15)` | `0xf` |

### Converter test results
| Input | Binary | Hexadecimal |
|---:|---|---|
| 10 | 1010 | A |
| 13 | 1101 | D |
| 25 | 11001 | 19 |

### Text encoding
- ASCII code for uppercase A: 65
- ASCII code for lowercase a: 97
- Example of a character outside basic ASCII: ₹

An encoding standard tells a computer how characters are represented as numbers and bytes. ASCII represents a basic set of characters, while UTF-8 supports a much wider range of characters.

## 3. Commands / tools used
- `python3` — runs Python programs.
- `bin()` — converts an integer to a binary string.
- `hex()` — converts an integer to a hexadecimal string.
- `int(value, base)` — converts a string in a specified base into an integer.
- `input()` — accepts user input.
- `print()` — displays output.

## 4. My understanding
I learned that computers use binary digits (0 and 1) to represent data. Decimal uses base 10, binary uses base 2 and hexadecimal uses base 16. Python provides built-in functions to convert numbers between these systems.

## 5. Difficulties faced
At first, converting a number into binary by hand was challenging because I had to keep track of the powers of two.

## 6. How I resolved them
I broke the number into powers of two and then checked the result with Python’s `bin()` function.

## 7. Evidence / files
- `number_converter.py` (accepts non-negative integers and prints binary and hexadecimal representations)
- Manual conversion working
- Python verification and test results
- Text encoding notes

## 8. Commit details
Commit message: Build number converter and practise data representation.
GitHub repository: [cherryx18/digital-detective-8455](https://github.com/cherryx18/digital-detective-8455).
