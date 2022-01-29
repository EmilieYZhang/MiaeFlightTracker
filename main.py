from api import utils
# Let's start in main.py showing some wrapper patterns and depicting method attributes.
# Explore with pushes and pulls and view on GitHub!
# git remote add new_origin https://github.com/mowglu/MIAE-Python and then use git pull new_origin <<commit>>
def main_wrapper():
    # intrinsic methods
    print(f"This is the start of our python project, we will be starting off with this wrapper main function called {main_wrapper.__name__}")

    utils.solid_example_1(example_param_1="a", example_param_2="a")
    utils.solid_example_2(3.4)
    utils.solid_example_3()

    print("This is the end of our python project")


if __name__ == "__main__":
    main_wrapper()