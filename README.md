# Basic Chatbot

A simple rule-based chatbot built with Python — a CodeAlpha internship task.

It runs in the terminal and replies to common phrases (greetings, "how are you", "thank you", "bye") using keyword matching. Anything it doesn't recognize gets a polite fallback response.

## Run it

```bash
python "Basic Chatbot.py"
```

Then chat — type `bye` to exit:

```
Chatbot: Hello! Type 'bye' to exit.
You: hello
Chatbot: Hi! How can I help you?
You: bye
Chatbot: Goodbye! Have a great day!
```

## How it works

- `chatbot_response()` lowercases your input and matches it against known keywords
- `main()` runs the conversation loop until you say bye

No libraries needed — pure Python.
