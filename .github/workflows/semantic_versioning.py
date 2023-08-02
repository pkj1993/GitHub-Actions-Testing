import sys
import os

def increment_version(version, position):
    parts = version.split('.')
    parts[position] = str(int(parts[position]) + 1)
    for i in range(position + 1, len(parts)):
        parts[i] = '0'
    return '.'.join(parts)

def main():
    if len(sys.argv) != 2:
        print("Usage: python semantic_versioning.py <latest_tag>")
        sys.exit(1)

    latest_tag = sys.argv[1]
    if not latest_tag:
        latest_tag = "0.0.0"

    next_major = increment_version(latest_tag, 0)
    next_minor = increment_version(latest_tag, 1)
    next_patch = increment_version(latest_tag, 2)

    print(f"Next Major Version: {next_major}")
    print(f"Next Minor Version: {next_minor}")
    print(f"Next Patch Version: {next_patch}")

if __name__ == "__main__":
    main()
