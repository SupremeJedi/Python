from pathlib import Path
path = Path("emails")
for file in path.glob("*.py"):
    print(file)