<div align="center">
    <img src="source/main.png" alt="Logo" width="60%" />
</div>

# FinMTEB: Finance Massive Text Embedding Benchmark
Finance Massive Text Embedding Benchmark (FinMTEB), an embedding benchmark consists of **64 financial domain-specific text datasets**, across **English and Chinese**, spanning **seven different tasks**. All datasets in FinMTEB are finance-domain specific, either previously used in financial NLP research or newly developed by the authors.

* Paper Link: [Do We Need Domain-Specific Embedding Models? An Empirical Investigation](https://arxiv.org/pdf/2409.18511v1)
* 🤗 [Leaderboard](https://huggingface.co/spaces/FinanceMTEB/FinanceMTEB_Leaderboard)
## Usage 
* The basic pipeline is built upon [MTEB](https://github.com/embeddings-benchmark/mteb). 

---
### News
* 🎆 We open source a new **finance-adapted** LLM-based embedding model [FinE5]([https://github.com/embeddings-benchmark/mteb](https://huggingface.co/yixuantt/Fin-e5)). 
### Install

```
conda create -n finmteb python=3.10
git clone https://github.com/yixuantt/FinMTEB.git
cd FinMTEB
pip install -r requirements.txt
```

### Task selection
FinMTEB offers 7 tasks and 64 datasets, which you can choose according to your needs.

```
import finance_mteb 

tasks = finance_mteb.get_tasks(task_types=["Clustering", "Retrieval","PairClassification","Reranking","STS","Summarization","Classification"]) # All 7 Tasks
```

### Running a Benchmark

```
from finance_mteb import MTEB
task = "FinSTS"
evaluation = MTEB(tasks=[task])
evaluation.run(model, output_folder=f"results/{model_name_or_path.split('/')[-1]}")
```

## Example Usage
* There is an example Python script for your reference:
```
python eval_FinanceMTEB.py --model_name_or_path BAAI/bge-en-icl --pooling_method last
```

## Citation
```
@misc{tang2024needdomainspecificembeddingmodels,
      title={Do We Need Domain-Specific Embedding Models? An Empirical Investigation}, 
      author={Yixuan Tang and Yi Yang},
      year={2024},
      eprint={2409.18511},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2409.18511}, 
}
```
--------
Thanks to the [MTEB](https://github.com/embeddings-benchmark/mteb) Benchmark.
