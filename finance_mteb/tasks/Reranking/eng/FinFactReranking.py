from __future__ import annotations

from finance_mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskReranking import AbsTaskReranking


class FinFactReranking(AbsTaskReranking):
    metadata = TaskMetadata(
        name="FinFactReranking",
        description="A Benchmark Dataset for Financial Fact Checking and Explanation Generation",
        reference="https://arxiv.org/pdf/2309.08793",
        dataset={
            "path": "FinanceMTEB/FinFact-reranking",
            "revision": "70435b4984c687051ecf38b9d2686f33345dcced",
        },
        type="Reranking",
        category="s2s",
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="map",
    )
