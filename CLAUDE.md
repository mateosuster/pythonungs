# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational repository for "Introducción a Python" at UNGS (Universidad Nacional de General Sarmiento), taught as part of the MPE III (Matemática para Economistas III) program. Published as a GitHub Pages site at https://mateosuster.github.io/pythonungs/.

All course content lives in Jupyter notebooks (`.ipynb`). There is no build system, test suite, or package to install — the workflow is editing notebooks and updating the course index.

## Repository Structure

```
codigos/           # All course notebooks, organized by topic
  introduccion_a_python/    # Syntax, data types, OOP, error handling
  programacion_funcional/   # Control flow (if/while/for), functions
  manipulacion_de_datos/    # Pandas, matplotlib, plotly, Yahoo Finance
  pandas/                   # Additional pandas notebooks
  mate_financiera/          # Present/future value, bonds
  EDOs/                     # Differential equations
  TPs/                      # Student assignments and exams
  parciales/                # Partial exam materials
anthropic/         # LLM/AI prompting notebooks and HTML tutorials
documents/         # LaTeX-generated PDF slides
data/              # CSV datasets (restaurant data) used in exercises
index.md           # Main course page rendered by GitHub Pages
_config.yml        # Jekyll theme config (jekyll-theme-minimal)
```

## Common Tasks

**Open a notebook locally:**
```bash
jupyter notebook codigos/introduccion_a_python/<notebook>.ipynb
```

**Update the course index** — edit `index.md` directly; it is the GitHub Pages homepage.

**Add a new notebook to the index** — add a Colab link under the relevant section in `index.md`. Colab links follow the pattern:
```
https://colab.research.google.com/github/mateosuster/pythonungs/blob/master/<path-to-notebook>.ipynb
```

## Notebook Conventions

- Notebooks are written in Spanish (course language is Spanish).
- Student-facing notebooks mix explanatory markdown cells with executable code cells.
- Assignment notebooks (`TPs/`) include problem statements and sometimes solution proposals.
- The `anthropic/` directory contains bilingual (English/Spanish) materials on AI prompting.

## Course Topics & Notebook Organization

Notebooks are versioned with suffixes like `_v1`, `_v2` when revised. The most recent version is canonical. Some topics have both a main notebook and an `_ejercicios` (exercises) companion.

Data files in `data/` are restaurant CSVs (`restaurant_customers.csv`, `restaurant_foods.csv`, `restaurant_week_1_sales.csv`, `restaurant_week_2_sales.csv`, `restaurant_week_1_times.csv`) used in pandas exercises.
