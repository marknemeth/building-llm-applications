# Copilot instructions for this repository

This repository is a multi-chapter book project for building LLM applications with Python and LangChain. It is not a single application; it is a collection of chapter-based examples and experiments. Treat each chapter folder as a separate project with its own setup and dependencies unless the task explicitly targets the repo root.

## Repo structure and conventions
- The root contains chapter folders such as `ch01` through `ch11` plus general project docs.
- Each chapter typically contains its own README, requirements, scripts, notebooks, and supporting modules.
- Work should be scoped to the relevant chapter unless the request explicitly says otherwise.
- Do not assume a single root-level build, test, or lint command exists. Setup and commands are usually chapter-specific.

## Technology stack
- Primary language: Python.
- Major frameworks: LangChain, LangGraph, LangChain OpenAI, LangChain Community, and related ecosystem packages.
- Environment variables are frequently loaded with `python-dotenv` and may require an `OPENAI_API_KEY`.
- Some chapters use `.env` files, local services, or external APIs; be careful about chapter-specific runtime dependencies.

## Working style for future tasks
- Start by identifying the target chapter and reading the chapter-local README or requirements file before making changes.
- Prefer the smallest relevant file or module for the requested behavior instead of broad repo-wide edits.
- Keep changes aligned with the chapter’s example style and architecture.
- If a task involves LLM workflows, model configuration, prompts, or agents, inspect the chapter’s model/prompt modules before changing logic.
- Preserve the educational, example-oriented nature of the code rather than introducing enterprise framework patterns unless the task explicitly calls for them.

## Validation guidance
- Use the narrowest validation command that checks the touched behavior.
- Because this repo is chapter-oriented, validation may mean executing the relevant chapter script or a focused test rather than a monorepo-wide suite.
- When a chapter uses a local service or external API, verify the task with the most direct available local check and document any missing environment dependencies.

## Important project-specific assumptions
- This repo is example-driven and instructional, not production-oriented.
- Many examples depend on chapter-local files and environment configuration.
- Some chapters may require additional packages or runtime services that are not installed globally at the repo root.
- When in doubt, inspect the target chapter’s `requirements.txt`, README, and entry-point scripts before editing code.
