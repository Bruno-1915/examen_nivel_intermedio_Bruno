import logging


def config_logging(level: int):
    """Config the logging settings
    
    Parameters
    ----------
    level: int
        The level for the loggings to be printed 
        it can be specified with the loggin module (logging.DEBUG,
                                                    logging.INFO, etc)
    """
    logging.basicConfig(level=level,
                        format='%(levelname)-8s :: %(message)s'
                        # format=' %(name)s :: %(levelname)-8s :: %(message)s'
                        )