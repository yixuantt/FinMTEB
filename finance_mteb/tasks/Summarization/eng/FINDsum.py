
from __future__ import annotations

from finance_mteb.abstasks.AbsTaskSummarization import AbsTaskSummarization
from finance_mteb.abstasks.TaskMetadata import TaskMetadata


class FINDsum(AbsTaskSummarization):
    metadata = TaskMetadata(
        name="FINDsum",
        description="A Large-Scale Dataset for Long Text and Multi-Table Summarization.",
        reference="https://aclanthology.org/2022.findings-emnlp.145/",
        dataset={
            "path": "FinanceMTEB/FINDsum",
            "revision": "0ca87ef0286fc1451841761a684548dc1ca36070",
        },
        type="Summarization",
        category="p2p",
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="cosine_spearman",
    )
    @property
    def metadata_dict(self) -> dict[str, str]:
        metadata_dict = super().metadata_dict
        metadata_dict["min_score"] = 0
        metadata_dict["max_score"] = 1
        return metadata_dict