import os
ENVIRONMENT = os.getenv('TEST_STRING')

# print(f"The current environment is {ENVIRONMENT.lower()}")

mainName = "main.sh"

main = os.path.join("one", "two", mainName)
#replace_with = ENVIRONMENT.lower() + "." + main
replace_with = ENVIRONMENT + "." + mainName

with open(replace_with, "r") as f:
    data = f.read()

with open(main, "w") as f:
    f.write(data)