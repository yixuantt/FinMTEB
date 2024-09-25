from __future__ import annotations

from finance_mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks import AbsTaskRetrieval

class AlphaFinRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="AlphaFinRetrieval",
        description="A financial Q&A dataset including NLI, financial QA, and stock trend predictions.",
        reference="https://github.com/AlphaFin-proj/AlphaFin",
        dataset={
            "path": "FinanceMTEB/AlphaFin",
            "revision": "f901493ea0dcb2faaad9624f586ece8238b06a52",
        },
        type="Retrieval",
        category="s2p",
        eval_splits=["train"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
    )