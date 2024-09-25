from __future__ import annotations

from finance_mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks import AbsTaskRetrieval

class FinEvaEncyclopediaRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="FinEvaEncyclopediaRetrieval",
        description="Financial scenario QA dataset provides terminology used in the financial industry.",
        reference="https://github.com/alipay/financial_evaluation_dataset",
        dataset={
            "path": "FinanceMTEB/FinEvaEncyclopedia",
            "revision": "319cfecef08894ba607881ae08b0b2b15badf3c7",
        },
        type="Retrieval",
        category="s2p",
        eval_splits=["train"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
    )