from __future__ import annotations

from finance_mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks import AbsTaskRetrieval

class THUCNewsRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="THUCNewsRetrieval",
        description="Chinese finance news dataset.",
        reference="http://thuctc.thunlp.org/",
        dataset={
            "path": "FinanceMTEB/THUCNews",
            "revision": "e80c8838c291b31e3335064b6463947b9d178667",
        },
        type="Retrieval",
        category="s2p",
        eval_splits=["train"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
    )