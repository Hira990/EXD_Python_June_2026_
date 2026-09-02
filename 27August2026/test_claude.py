import os
from anthropic import Anthropic

CLAUDE_API_KEY = "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"

client = Anthropic(
    api_key=CLAUDE_API_KEY,
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude",
        }
    ],
    model="claude-opus-5",
)

for block in message.content:
    if block.type == "text":
        print(block.text)