import aiofiles

def call_llm(prompt):
    # Placeholder: Connect to your real LLM endpoint (OpenAI, Claude, Gemini, etc.)
    # Example for OpenAI:
    # response = openai.Completion.create(model="gpt-4o", prompt=prompt, max_tokens=1024)
    # return response.choices[0].text.strip()
    return "Simulated LLM output for: " + prompt

async def score_text(text, file):
    if file:
        async with aiofiles.open(file.file, 'r', encoding='utf-8') as f:
            content = await f.read()
    else:
        content = text
    if not content.strip():
        score = 0
        label = "Empty text"
    else:
        score = min(100, max(1, int(len(content.split()) % 101)))
        label = "Likely Human" if score < 60 else "Likely AI"
    return {"score": score, "label": label}

async def deai_text(text, level, file):
    if file:
        async with aiofiles.open(file.file, 'r', encoding='utf-8') as f:
            content = await f.read()
    else:
        content = text

    base_prompt = (
        "Rewrite this text to sound as if it was produced by a real human, not AI. "
        "Break up any patterns typical to AI, add small mistakes, informal phrasing, narrative, and style changes. "
        "Make it inconsistent, subjective, and natural. Avoid perfect grammar. "
        "Target is to evade the top 2025 AI detectors (Copyleaks, Sapling, GPTZero, Winston AI, Pangram, ZeroGPT)."
    )

    if level == 1:
        prompt = base_prompt + " Only mild humanization needed: " + content
    elif level == 2:
        prompt = base_prompt + " Add informal tone, personal anecdotes, and some errors: " + content
    elif level == 3:
        prompt = base_prompt + " Go all out—add narrative, contradictions, slang, typos, and creative storytelling: " + content
    else:
        prompt = base_prompt + content

    candidate = call_llm(prompt)
    for attempt in range(3):
        if attempt == 2 or not candidate:
            break
        candidate = call_llm(prompt + " Try again, make it even more human and less AI-like.")

    return {"deai_text": candidate}