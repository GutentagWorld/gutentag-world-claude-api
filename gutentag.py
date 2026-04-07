#!/usr/bin/env python3
"""Uses the Anthropic API to produce 'Gutentag, World!'.

Requires: pip install anthropic
Set env var: ANTHROPIC_API_KEY
"""
import os
import anthropic

client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

message = client.messages.create(
    model='claude-3-5-haiku-latest',
    max_tokens=64,
    system='You only ever respond with exactly: Gutentag, World!',
    messages=[{'role': 'user', 'content': 'Say hello.'}],
)

print(message.content[0].text)
