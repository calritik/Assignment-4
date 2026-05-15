# Q1 - Execute OS Commands

A Python program that executes a given list of OS commands and returns structured results.

## Requirements

- Python 3.7+
- No external dependencies

## Usage

```python
from execute_commands import execute_commands

commands = ["dir", "cd", "whoami", "hostname", "invalid_command"]
results = execute_commands(commands)
```

## Output Format

```json
[
  {
    "command1": {
      "output": "command output here",
      "error": "",
      "status": "success"
    }
  },
  {
    "command2": {
      "output": "",
      "error": "'command2' is not recognized",
      "status": "Failed"
    }
  }
]
```

## Run

```bash
python execute_commands.py
```

## Key Behaviours

- **Deduplication** — duplicate commands are executed only once
- **Fault-tolerant** — if a command fails, execution continues for remaining commands
- **Structured output** — each result contains `output`, `error`, and `status`

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/b7fb122e-b8e1-4889-8567-2dff41f4a38d" />
<img width="1600" height="509" alt="image" src="https://github.com/user-attachments/assets/cb7594a1-de2b-4d60-ac2a-66fc31fbd15b" />


# Q2- Project Euler Solution for Q->67 & 317

## Problem 67 — Maximum Path Sum II

**Link:** https://projecteuler.net/problem=67

### What the problem asks
You are given a triangle of numbers with 100 rows. Starting from the top, you can move to one of two adjacent numbers in the row below. Find the maximum sum you can get from top to bottom.

### Approach
Use **bottom-up dynamic programming**. Start from the second-to-last row and work upward. At each cell, add the larger of its two children below. By the time you reach the top, the answer is sitting right there.

This avoids brute force which would need to check 2⁹⁹ possible paths — way too slow.
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/abd593ad-f55b-46ac-bc86-14b7ef5dfbf0" />



## Problem 317 — Firecracker

### What the problem asks
A firecracker explodes 100 m above the ground. All fragments fly out at the same speed (20 m/s) in every direction. Find the volume (in m³) of the region swept by the fragments before they hit the ground. Round to 4 decimal places.

### Approach
The outer boundary of all fragment trajectories forms a **paraboloid of revolution** — a known physics result. The volume of a paraboloid is simply:

```
Volume = (1/2) × π × r² × H
```

where `H` is the apex height and `r` is the base radius at ground level.

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/099f3941-629d-4988-9201-9587eae9c97a" />
