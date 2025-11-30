Kasparro Agentic Architecture v1.1

This diagram illustrates the multi-agent workflow, highlighting the Planner's decision-making logic and the Evaluator's validation loop.

graph TD
    %% -- Input --
    User([User Query]) --> Planner{Planner Agent}

    %% -- Orchestration --
    Planner -->|'analyze_metrics'| Insight[Insight Agent]
    Planner -->|'generate_creatives'| Creative[Creative Agent]

    %% -- Data Layer --
    subgraph "Data Layer (Deterministic)"
        Raw[(Raw CSV)] --> Data[Data Agent]
        Data -->|Map-Reduce Cleaning| LLM_Data[LLM Normalization]
        LLM_Data --> Data
    end

    %% -- Analysis Loop --
    subgraph "Intelligence Layer"
        Data -->|Performance Summary| Insight
        Insight -->|Hypothesis| Evaluator{Evaluator Agent}
        
        Evaluator -- Validated (Score > 0.5) --> Report[Final Report]
        Evaluator -- Rejected (Score < 0.5) --> Retry[Retry Loop]
        Retry -.-> Insight
    end

    %% -- Creative Loop --
    subgraph "Creative Layer"
        Data -->|Low CTR Ads| Creative
        Creative -->|Draft New Copy| LLM_Creative[LLM (Llama-3)]
        LLM_Creative --> NewAds[New Creatives]
        NewAds --> Report
    end

    %% -- Styling --
    classDef agent fill:#f9f,stroke:#333,stroke-width:2px;
    classDef decision fill:#bbf,stroke:#333,stroke-width:2px;
    classDef data fill:#dfd,stroke:#333,stroke-width:2px;
    
    class Planner,Evaluator decision;
    class Data,Insight,Creative agent;
    class Raw,Report,NewAds data;
