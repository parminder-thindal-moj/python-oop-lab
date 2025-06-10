import os
import sys
from pprint import pprint

print(f"Current working directory: {os.getcwd()}")
print("\nPYTHONPATH:")

for path in sys.path:
    print(f"  - {path}")

pprint(sys.path)
