# Self-Review: Kasparro Agentic Analyst v1.1

## 🏗 Architecture Decisions

### 1. The Planner-Evaluator Loop
I transitioned from a linear script to a **Planner-based architecture** to optimize token usage and latency.
- **Why:** Not every query requires every tool. If a user simply asks "Why is spend down?", invoking the Creative Generator is inefficient.
- **Implementation:** The `PlannerAgent` assesses user intent and dynamically constructs an execution graph (e.g., `['analyze_metrics']` vs `['analyze_metrics', 'generate_creatives']`).

### 2. Quantitative Validation (The "Evaluator")
To mitigate LLM hallucinations, I implemented a strict **Quantitative Validation Layer**.
- **Logic:** The `EvaluatorAgent` acts as a critic, cross-referencing the Insight Agent's textual hypothesis against the deterministic data summary from Pandas.
- **Guardrail:** If the confidence score falls below **0.5**, the Orchestrator triggers a reflection loop, forcing the Insight Agent to retry with a stricter "Data-Driven" prompt.

### 3. Self-Healing Data Layer
The provided dataset contained inconsistent naming conventions (e.g., `Men-Athleisure` vs `Men Athleisure` vs `Cooli-g`).
- **Solution:** Instead of fragile Regex rules, I implemented a **Map-Reduce cleaning step** using the LLM. The Data Agent extracts unique entities and asks the LLM to standardize them, making the system robust to future data errors without code changes.

## ✅ Verification & Quality Assurance

- **Unit Tests:** `tests/test_evaluator.py` passes, verifying the Data Agent's calculation logic and LLM connectivity.
- **Observability:** All steps are logged to `logs/execution.jsonl` in machine-readable JSON format for easier debugging.
- **Reproducibility:** Random seeds are pinned in `config.yaml` to ensure deterministic outputs.
- **Planner Logic:** Verified that diagnostic queries trigger single-agent workflows, while complex queries trigger multi-agent workflows.