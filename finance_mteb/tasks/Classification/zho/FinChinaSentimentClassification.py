from __future__ import annotations

from finance_mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks import AbsTaskClassification

class FinChinaSentimentClassification(AbsTaskClassification):
    metadata = TaskMetadata(
        name="FinChinaSentimentClassification",
        description="Polar sentiment dataset of sentences from financial domain, categorized by sentiment into positive, negative, or neutral.",
        reference="https://arxiv.org/abs/2306.14096",
        dataset={
            "path": "FinanceMTEB/FinChinaSentiment",
            "revision": "97eef2264cdadab25f5ba218355e75cb7b4d44ef",
        },
        type="Classification",
        category="s2s",
        eval_splits=["test"],
        eval_langs=["cmn-Hans"],
        main_score="accuracy",
    )
    def dataset_transform(self):
        self.dataset = self.dataset.rename_column("sentence", "text")