import os

from kfai_env.env import Environment

if __name__ == "__main__":
    print("Simple Python App Example")

    e = Environment('./env')
    e.load_env()
    print(os.getenv("TEST_ENV"))
