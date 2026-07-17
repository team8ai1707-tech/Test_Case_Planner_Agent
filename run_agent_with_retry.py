# retry_utils.py
import time

def run_agent_with_retry(agent, prompt, max_retries=4):
    base_wait_time = 5
    for attempt in range(max_retries):
        try:
            return agent.run(prompt)
        except Exception as e:
            error_message = str(e)
            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                if attempt < max_retries - 1:
                    wait_time = base_wait_time * (2 ** attempt)
                    print(f"⚠️ Rate limit hit. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    raise e
            else:
                raise e