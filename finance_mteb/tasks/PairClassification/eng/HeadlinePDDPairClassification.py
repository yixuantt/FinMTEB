from __future__ import annotations

from finance_mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class HeadlinePDDPairClassification(AbsTaskPairClassification):
    metadata = TaskMetadata(
        name="HeadlinePDDPairClassification",
        description="Financial text sentiment categorization dataset.",
        reference="",
        dataset={
            "path": "FinanceMTEB/HeadlinePDD-PairClassification",
            "revision": "ad0150ed63940e88846659e46be5138aa0db6c85",
        },
        type="PairClassification",
        category="s2s",
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="ap",
    )
    def dataset_transform(self):
        self.dataset = self.dataset.rename_column("sent1", "sentence1")
        self.dataset = self.dataset.rename_column("sent2", "sentence2")