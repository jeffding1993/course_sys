import os, sys
from core.src import src

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == '__main__':
    src.run()
