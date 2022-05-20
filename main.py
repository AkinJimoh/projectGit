import os
ENVIRONMENT = os.getenv('TEST_STRING')

print(f"The current environment is {ENVIRONMENT.lower()}")