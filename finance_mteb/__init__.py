from __future__ import annotations

# from importlib.metadata import version

from finance_mteb.benchmarks import (
    MTEB_MAIN_EN,
    MTEB_MAIN_RU,
    MTEB_RETRIEVAL_LAW,
    MTEB_RETRIEVAL_WITH_INSTRUCTIONS,
)
from finance_mteb.evaluation import *
from finance_mteb.models import get_model, get_model_meta
from finance_mteb.overview import TASKS_REGISTRY, get_task, get_tasks

# __version__ = version("mteb")  # fetch version from install metadata

__version__ = "1.12.49"

__all__ = [
    "MTEB_MAIN_EN",
    "MTEB_MAIN_RU",
    "MTEB_RETRIEVAL_LAW",
    "MTEB_RETRIEVAL_WITH_INSTRUCTIONS",
    "TASKS_REGISTRY",
    "get_tasks",
    "get_task",
    "get_model",
    "get_model_meta",
]
