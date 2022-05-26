import os
ENVIRONMENT = os.getenv('TEST_STRING').lower()
# DIR = "config/"



# DynamicFile = os.path.join("one", "two", "three", ConfigFile)
#REPLACEMENT = ENVIRONMENT.lower() + "." + DynamicFile
# REPLACEMENT = f"main.{ENVIRONMENT}.sh"

ConfigFile = "main.sh"

if ENVIRONMENT == "test":
    REPLACEMENT = "main" + "." + "dev" + "." + "sh"
else:
    REPLACEMENT = "main" + "." + ENVIRONMENT + "." + "sh"
print("Your Selected Environment Is:" + ENVIRONMENT)


with open(REPLACEMENT, "r") as f:
    data = f.read()

with open(ConfigFile, "w") as f:
    f.write(data)