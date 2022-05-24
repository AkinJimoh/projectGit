import os
ENVIRONMENT = os.getenv('TEST_STRING')
# DIR = "config/"

ConfigFile = "main.sh"

# DynamicFile = os.path.join("one", "two", "three", ConfigFile)
#REPLACEMENT = ENVIRONMENT.lower() + "." + DynamicFile
# REPLACEMENT = DIR + ENVIRONMENT + "." + ConfigFile
REPLACEMENT = ENVIRONMENT + "." + ConfigFile

with open(REPLACEMENT, "r") as f:
    data = f.read()

with open(ConfigFile, "w") as f:
    f.write(data)