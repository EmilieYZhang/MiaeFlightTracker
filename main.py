from api import utils
from api import fetcher

# Let's start in main.py showing some wrapper patterns and depicting method attributes.
# Explore with pushes and pulls and view on GitHub!
# git remote add new_origin https://github.com/mowglu/MIAE-Python and then use git pull new_origin <<commit>>


def main_wrapper():
    # intrinsic methods
    print(f"This is the start of our python project, we will be starting off with this wrapper main function called {main_wrapper.__name__}")
    fetcher.states_accessor()
    print("This is the end of our python project")


if __name__ == "__main__":
    main_wrapper()
