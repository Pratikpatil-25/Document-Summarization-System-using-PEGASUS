# from src.summarizer.config.configuration import ConfigurationManager
# from src.summarizer.components.doc_ingestion import DocIngestion
# from src.summarizer.logging import logger

# STAGE_NAME = "Document Ingestion stage"

# class DocIngestionPipeline:
#     def __init__(self):
#         pass

#     def main(self):
#         config = ConfigurationManager()     # object creation
#         doc_ingestion_config = config.get_doc_ingestion_config()      # stored output of config object's method
#         doc_ingestion = DocIngestion(config = doc_ingestion_config)     # object creation
#         doc_ingestion.validate_document()
#         doc_ingestion.save_document()


# if __name__ == '__main__':
#     try:
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = DocIngestionPipeline()
#         obj.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logger.exception(e)
#         raise e