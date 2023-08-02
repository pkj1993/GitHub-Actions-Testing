import os
import subprocess
import re

def get_current_version():
    try:
        with open('version.txt', 'r') as version_file:
            version = version_file.read().strip()
            return version
    except FileNotFoundError:
        return '0.1.0'  # Default version if version.txt doesn't exist

def bump_version(version, part='patch'):
    major, minor, patch = map(int, version.split('.'))
    
    if part == 'major':
        major += 1
        minor = 0
        patch = 0
    elif part == 'minor':
        minor += 1
        patch = 0
    else:
        patch += 1
    
    new_version = f"{major}.{minor}.{patch}"
    return new_version

def create_tag_and_release(new_version):
    # Create a Git tag
    subprocess.run(['git', 'tag', new_version])
    
    # Create a GitHub release using 'hub' command (make sure you have 'hub' installed)
    release_notes = f'Release {new_version}'
    subprocess.run(['hub', 'release', 'create', new_version, '-m', release_notes])

def main():
    current_version = get_current_version()
    print(f'Current version: {current_version}')
    
    new_version = bump_version(current_version, 'patch')
    print(f'New version: {new_version}')
    
    # Write the new version back to version.txt
    with open('version.txt', 'w') as version_file:
        version_file.write(new_version)
    
    create_tag_and_release(new_version)

if __name__ == "__main__":
    main()
