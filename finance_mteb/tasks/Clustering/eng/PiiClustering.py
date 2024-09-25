
from __future__ import annotations

from finance_mteb.abstasks.AbsTaskClustering import AbsTaskClustering
from finance_mteb.abstasks.AbsTaskClusteringFast import clustering_downsample
from finance_mteb.abstasks.TaskMetadata import TaskMetadata


class PiiClustering(AbsTaskClustering):
    metadata = TaskMetadata(
        name="PiiClustering",
        description="Synthetic financial documents containing Personally Identifiable Information (PII)",
        reference="https://huggingface.co/datasets/gretelai/synthetic_pii_finance_multilingual",
        dataset={
            "path": "FinanceMTEB/synthetic_pii_finance_en",
            "revision": "5021671d60a324d576a7b57e4c4e13bfcf857a4d",
        },
        type="Clustering",
        category="p2p",
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="v_measure",
    )
