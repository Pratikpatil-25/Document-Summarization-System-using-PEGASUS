# from src.summarizer.logging import logger
# from src.summarizer.pipeline.stage_1_doc_ingestion import DocIngestionPipeline
# from src.summarizer.pipeline.stage_2_doc_validation import DocValidationPipeline
# # from src.summarizer.pipeline.stage_3_data_transformation import DataTransformationTrainingPipeline
# # from src.summarizer.pipeline.stage_4_model_trainer import ModelTrainerTrainingPipeline
# # from src.summarizer.pipeline.stage_5_model_evaluation import ModelEvaluationTrainingPipeline


# STAGE_NAME = "Document Ingestion stage"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
#    doc_ingestion = DocIngestionPipeline()
#    doc_ingestion.main()
#    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e

# STAGE_NAME = "Document Validation stage"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
#    doc_validation = DocValidationPipeline()
#    doc_validation.main()
#    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e