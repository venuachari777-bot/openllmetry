import os
from dotenv import load_dotenv
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow, task
from groq import Groq

load_dotenv()

# Traceloop Observability Init
Traceloop.init(
    app_name="groq-observability-pipeline",
    disable_batch=True
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@task(name="preprocess_prompt_task")
def preprocess_prompt(user_topic: str) -> str:
    """Task 1: Preprocessing and formatting the user prompt."""
    return f"Explain {user_topic} in 2 sentences for a developer."

@task(name="llm_inference_task")
def call_llm(formatted_prompt: str) -> str:
    """Task 2: Performing actual inference via Groq."""
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": formatted_prompt}]
    )
    return response.choices[0].message.content

@workflow(name="main_query_pipeline")
def run_pipeline(topic: str):
    """Parent Workflow orchestrating both tasks."""
    prompt = preprocess_prompt(topic)
    result = call_llm(prompt)
    return result

if __name__ == "__main__":
    topic_input = "Distributed Tracing in AI"
    print(f"Triggering pipeline for topic: '{topic_input}'...")
    
    output = run_pipeline(topic_input)
    
    print("\n--- Pipeline Completed ---")
    print("Response:\n", output)