import logging 

#----------------
#----Logger------

# Custom logger
logger = logging.getLogger('Spectrogram')

# Set level
logger.setLevel(logging.INFO)

# Create handler
handler = logging.StreamHandler()

# Set formatter
format = '%(asctime)s - %(levelname)s - %(filename)s - %(message)s'
formatter = logging.Formatter(format)
handler.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(handler)