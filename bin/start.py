import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.src import src

if __name__ == '__main__':
    src.run()
