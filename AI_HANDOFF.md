# IT Career Agent - AI Handoff

## Purpose

AI-powered IT career intelligence platform that analyzes resumes against job descriptions and produces career improvement recommendations.

---

# Current Status

## Development State

- Main branch clean
- GitHub synchronized
- 35 tests passing
- Latest milestone: Improvement Plan integration and enhanced career reporting

---

# Technology Stack

## Backend

- Python
- FastAPI
- Pytest

## AI / LLM

- CrewAI
- Ollama
- Production model:
  - ollama/qwen2.5:14b
- Testing model:
  - ollama/qwen2.5:7b

## RAG

- ChromaDB
- LangChain utilities
- Ollama embeddings
- nomic-embed-text

---

# Current Architecture

Resume PDF
|
v
ResumeService
|
v
ResumeData

Job Description
|
v
JobService
|
v
JobData

AnalysisService
|
+--> ATSService
| |
| v
| ATSResult
|
+--> CareerIntelligenceService
| |
| v
| CareerIntelligence
|
+--> ImprovementPlannerService
|
v
ImprovementPlan

CareerContext
|
v
ReportGenerator
|
v
CareerReport


---

# Completed Features

## RAG Pipeline

- Document loading
- PDF parsing
- Chunking
- Embeddings
- ChromaDB vector storage
- Retrieval testing

## Career Analysis

- Resume parsing
- Job description parsing
- ATS matching
- Skill gap analysis
- Career intelligence generation

## Improvement Planning

- Priority gaps
- Improvement recommendations
- Impact scoring

## Reporting

- Markdown career analysis reports
- Executive summary
- Skill analysis
- Improvement plans

---

# Important Files

app/
|
+-- models/
| |
| +-- career_context.py
| +-- ats_result.py
| +-- career_intelligence.py
| +-- improvement_plan.py
| +-- report.py
|
+-- services/
| |
| +-- analysis_service.py
| +-- report_generator.py
| +-- improvement_planner.py
|
+-- api/
|
+-- routes.py

tests/

scripts/


---

# Current Development Focus

Next planned phase:

API refinement.

Goal:

Create a clean API response model suitable for:

- frontend application
- future SaaS product
- report visualization

---

# Development Commands

## Activate environment

```powershell
.\.venv\Scripts\Activate.ps1