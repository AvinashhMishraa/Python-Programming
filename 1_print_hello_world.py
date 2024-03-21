# pip install loguru
#from loguru import logger  
#logger.info("This is a debug message") 





import logging 
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')
#logging.debug("This is a debug message")
logging.info("This is a debug message")
