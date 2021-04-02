import os

from kfai_env.environment.register import Environment

if __name__ == "__main__":
    print("Simple Python App Example")

    e = Environment()
    e.load_env()
    print(os.getenv("TEST_ENV"))
