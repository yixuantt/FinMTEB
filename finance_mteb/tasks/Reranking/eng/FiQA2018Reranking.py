from __future__ import annotations

from finance_mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskReranking import AbsTaskReranking


class FiQA2018Reranking(AbsTaskReranking):
    metadata = TaskMetadata(
        name="FiQA2018Reranking",
        description="Financial opinion mining and question answering",
        reference="https://sites.google.com/view/fiqa/",
        dataset={
            "path": "FinanceMTEB/FiQA-reranking",
            "revision": "f6934c7980c19a3acb8aeba3b66b4766fbb4b9db",
        },
        type="Reranking",
        category="s2s",
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="map",
    )
