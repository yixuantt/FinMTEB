
from __future__ import annotations

from finance_mteb.abstasks.AbsTaskSummarization import AbsTaskSummarization
from finance_mteb.abstasks.TaskMetadata import TaskMetadata


class Ectsum(AbsTaskSummarization):
    metadata = TaskMetadata(
        name="Ectsum",
        description="A Dataset For Bullet Point Summarization of Long Earnings Call Transcripts.",
        reference="https://arxiv.org/abs/2210.12467",
        dataset={
            "path": "FinanceMTEB/ECTsum",
            "revision": "036a3cbc49ce9e77af1832693a32bfdf6207bb57",
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