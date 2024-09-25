from __future__ import annotations

from finance_mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks import AbsTaskRetrieval

class FiQA2018Retrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="FiQA2018Retrieval",
        description="Financial opinion mining and question answering",
        reference="https://arxiv.org/pdf/2311.11944",
        dataset={
            "path": "FinanceMTEB/FiQA",
            "revision": "d52555df9c5c856a01931c112e03eaa0f2d8d6d4",
        },
        type="Retrieval",
        category="s2p",
        eval_splits=["train"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
    )