from src.summarizer.logging import logger
from src.summarizer.pipeline.stage_1_doc_ingestion import DocIngestionPipeline
# from src.summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from src.summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from src.summarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from src.summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   doc_ingestion = DocIngestionPipeline()
   doc_ingestion.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e