# from src.summarizer.config.configuration import ConfigurationManager
# from src.summarizer.components.doc_validation import DocValidation
# from src.summarizer.logging import logger

# STAGE_NAME = "Document Validation stage"

# class DocValidationPipeline:
#     def __init__(self):
#         pass

#     def main(self):
#         config = ConfigurationManager()     # object creation
#         doc_validation_config = config.get_doc_validation_config()      # stored output of config object's method
#         doc_validation = DocValidation(config = doc_validation_config)     # object creation
#         doc_validation.validate_all()


# if __name__ == '__main__':
#     try:
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = DocValidationPipeline()
#         obj.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logger.exception(e)
#         raise e