import json
import sys
from enum import Enum
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Required composition: python main.py <command> [arguments]")
        return
    
    command = sys.argv[1]

    if command == "print":
        print(sys.argv[2:])

if __name__ == "__main__":
    main()