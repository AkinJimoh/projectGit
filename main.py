import os
ENVIRONMENT = os.getenv('TEST_STRING')

# print(f"The current environment is {ENVIRONMENT.lower()}")

main = "main.sh"
#replace_with = ENVIRONMENT.lower() + "." + main
replace_with = ENVIRONMENT + "." + main

with open(replace_with, "r") as f:
    data = f.read()

with open(main, "w") as f:
    f.write(data)