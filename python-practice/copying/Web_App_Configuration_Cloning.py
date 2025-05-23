import copy

default_config = {
    "theme": "light",
    "features": {
        "search": True,
        "notifications": True
    }
}

# Create a deep copy for user-specific config
user_config = copy.deepcopy(default_config)
user_config["features"]["notifications"] = False

print("Default Config:", default_config)
print("User Config:", user_config)