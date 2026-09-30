# LLM Observability & Distributed Tracing with OpenLLMetry

An end-to-end LLM pipeline instrumented using OpenLLMetry (OpenTelemetry standard) and Traceloop SDK.

## Architecture
- **Instrumentation**: OpenLLMetry / OpenTelemetry
- **Tracing Platform**: Traceloop
- **Inference Engine**: Groq API (`openai/gpt-oss-20b`)
- **Granular Spans**: Handled via `@workflow` and `@task` decorators

## Features
- Real-time latency tracking across preprocessing and model execution.
- Granular token counting and trace span trees.
- Production-grade error tracing and status validation.

## How to Run
1. Install dependencies:
   ```bash
   pip install traceloop-sdk groq python-dotenv