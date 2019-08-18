REDIS_URL = "redis://localhost:6379"

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "last_name": {"type": "string"},
        "age": {"type": "number"},
    },
    "required": ["name"]
}
