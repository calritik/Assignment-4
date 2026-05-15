import subprocess
import json


def execute_commands(commands):
    # Deduplicate while preserving order
    seen = set()
    unique_commands = []
    for cmd in commands:
        if cmd not in seen:
            seen.add(cmd)
            unique_commands.append(cmd)

    results = []

    for cmd in unique_commands:
        try:
            proc = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True
            )
            if proc.returncode == 0:
                results.append({
                    cmd: {
                        "output": proc.stdout.strip(),
                        "error": "",
                        "status": "success"
                    }
                })
            else:
                results.append({
                    cmd: {
                        "output": proc.stdout.strip(),
                        "error": proc.stderr.strip(),
                        "status": "Failed"
                    }
                })
        except Exception as e:
            results.append({
                cmd: {
                    "output": "",
                    "error": str(e),
                    "status": "Failed"
                }
            })

    return results


if __name__ == "__main__":
    commands = ["ls", "df", "pwd", "ls", "invalidcmd123", "pwd"]
    output = execute_commands(commands)
    print(json.dumps(output, indent=2))