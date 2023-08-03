import sys

def increment_version(version):
    parts = version.split('.')
    for i in range(len(parts)):
        if parts[i].isdigit():
            parts[i] = str(int(parts[i]) + 1)
        else:
            # Handle the case when the version starts with non-numeric characters
            parts[i] = str(int(parts[i][1:]) + 1)
            parts[i] = 'v' + parts[i]
    return '.'.join(parts)

def main():
    if len(sys.argv) != 2:
        print("Usage: python semantic_versioning.py <latest_tag>")
        sys.exit(1)

    latest_tag = sys.argv[1]
    if not latest_tag:
        latest_tag = "0.0.0"

    next_version = increment_version(latest_tag)

    print(f"Next Version: {next_version}")

if __name__ == "__main__":
    main()
