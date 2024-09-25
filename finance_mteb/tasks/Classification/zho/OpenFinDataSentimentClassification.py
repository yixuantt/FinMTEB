from __future__ import annotations

from finance_mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks import AbsTaskClassification

class OpenFinDataSentimentClassification(AbsTaskClassification):
    metadata = TaskMetadata(
        name="OpenFinDataSentimentClassification",
        description="Financial scenario QA dataset incuding sentiment task.",
        reference="https://github.com/open-compass/OpenFinData",
        dataset={
            "path": "FinanceMTEB/OpenFinDataSentiment",
            "revision": "3494bbd2c652c8e1f021f7e60e9ab79faeec257b",
        },
        type="Classification",
        category="s2s",
        eval_splits=["test"],
        eval_langs=["cmn-Hans"],
        main_score="accuracy",
    )
    def dataset_transform(self):
        self.dataset = self.dataset.rename_column("sentence", "text")