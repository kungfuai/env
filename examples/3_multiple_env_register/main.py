import os

from src.environment.register import Environment

# Set the env to be test
os.environ['ENV'] = 'TEST'


if __name__ == "__main__":
    print("Multiple Environments Example")
    e = Environment('./env')

    # Register the expected environment
    e.register_environment('TEST')

    # Load it
    e.load_env()

    print(os.getenv("TEST_ENV"))
