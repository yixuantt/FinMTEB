import os

import logging
import argparse
from example_models.flag_dres_model import FlagDRESModel
from example_models.flag_icl_Model import FLAGICLModel
from example_models.openai_embed_model import OpenAIEmbedder
from example_models.e5_mistral_model import E5DRESModel
from task_list import RUNNING_TASK,TASK_LIST_RETRIEVAL
from finance_mteb import MTEB
from sentence_transformers import SentenceTransformer
from example_models.gte_model import GTERESModel
from eval_instruction import task2instruction

def _setup_logger():
    log_format = logging.Formatter("[%(asctime)s %(levelname)s] %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.handlers = [console_handler]

    return logger


logger = _setup_logger()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name_or_path', default="BAAI/bge-large-zh", type=str)
    parser.add_argument('--task_type', default=None, type=str)
    parser.add_argument('--add_instruction', action='store_true', help="whether to add instruction for query")
    parser.add_argument('--pooling_method', default='cls', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    if 'bge' in args.model_name_or_path and not 'icl' in args.model_name_or_path:
        model = FlagDRESModel(model_name_or_path=args.model_name_or_path,
                            query_instruction_for_retrieval=None,
                            pooling_method=args.pooling_method)
    elif 'icl' in args.model_name_or_path:
        model = FLAGICLModel(model_name_or_path=args.model_name_or_path,
                            query_instruction_for_retrieval="Given a web search query, retrieve relevant passages that answer the query.")
    elif 'text-embedding' in args.model_name_or_path:
        model = OpenAIEmbedder(engine=args.model_name_or_path)

    elif 'gte' in args.model_name_or_path or 'stella' in args.model_name_or_path:
        model = GTERESModel(model_name_or_path=args.model_name_or_path,
                            query_instruction_for_retrieval="Given a web search query, retrieve relevant passages that answer the query",
                            pooling_method=args.pooling_method)
    elif 'e5-mistral' in args.model_name_or_path:
        model = E5DRESModel(model_name_or_path=args.model_name_or_path,
                    query_instruction_for_retrieval=None,
                    pooling_method=args.pooling_method)
    else:
        model = SentenceTransformer(args.model_name_or_path, trust_remote_code=True)
        model.max_seq_length = 256

    for task in RUNNING_TASK:
        logger.info(f"Running task: {task}")
        if task in  task2instruction.keys():
            instruction = task2instruction[task]
            if hasattr(model, 'set_prompt'):
                model.set_prompt(instruction)
                logger.info(f'Setting Prompt: {instruction} For Task: {task}')

        evaluation = MTEB(tasks=[task])
        logger.info('Running evaluation for task: {}'.format(evaluation))
        evaluation.run(model, output_folder=f"results/{args.model_name_or_path.split('/')[-1]}",encode_kwargs={"batch_size": 64})