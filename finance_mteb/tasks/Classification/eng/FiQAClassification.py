from __future__ import annotations

from finance_mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks import AbsTaskClassification

class FiQAClassification(AbsTaskClassification):
    metadata = TaskMetadata(
        name="FiQAClassification",
        description="Polar sentiment dataset of sentences from financial news, categorized by sentiment into positive, negative, or neutral.",
        reference="https://sites.google.com/view/fiqa/home",
        dataset={
            "path": "FinanceMTEB/FiQA_ABSA",
            "revision": "afa907ab4c6441afb8ee70bd99802bb707d3d2ab",
        },
        type="Classification",
        category="s2s",
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="accuracy",
    )