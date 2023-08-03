import sys

def increment_version(version):
    parts = version.split('.')
    parts[2] = str(int(parts[2]) + 1)
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
