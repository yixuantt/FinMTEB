
from __future__ import annotations

from finance_mteb.abstasks.AbsTaskClustering import AbsTaskClustering
from finance_mteb.abstasks.AbsTaskClusteringFast import clustering_downsample
from finance_mteb.abstasks.TaskMetadata import TaskMetadata


class CCKS2022Clustering(AbsTaskClustering):
    metadata = TaskMetadata(
        name="CCKS2022Clustering",
        description="Clustering of financial events.",
        reference="https://www.biendata.xyz/competition/ccks2022_eventext/",
        dataset={
            "path": "FinanceMTEB/CCKS2022",
            "revision": "109293c66467e029ad33a11ee398791fa002aaac",
        },
        type="Clustering",
        category="p2p",
        eval_splits=["test"],
        eval_langs=["cmn-Hans"],
        main_score="v_measure",
    )
