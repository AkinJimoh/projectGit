import os
ENVIRONMENT = os.getenv('TEST_STRING').lower()
# DIR = "config/"

ConfigFile = "main.sh"

# DynamicFile = os.path.join("one", "two", "three", ConfigFile)
#REPLACEMENT = ENVIRONMENT.lower() + "." + DynamicFile
REPLACEMENT = "main" + "." + ENVIRONMENT + "." + "sh"
# REPLACEMENT = f"main.{ENVIRONMENT}.sh"

with open(REPLACEMENT, "r") as f:
    data = f.read()

with open(ConfigFile, "w") as f:
    f.write(data)