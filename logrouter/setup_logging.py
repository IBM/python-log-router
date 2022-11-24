import os
import yaml
import logging.config

def setup_logging(
    cfg_path : str = None,
    default_level : int = logging.DEBUG,
    env_path : str ='LOG_CFG',
    use_default_config : bool = False
):
    """ Setup logging configuration

    Args:
        cfg_path (str, optional): yaml configuration file. Must be an absolute path. Defaults to 'default_logging_conf'.
        default_level (_type_, optional): logging level to use if no conf is provided. Defaults to logging.DEBUG.
        env_path (str, optional): environment variable with the path to the yaml configuration file. Defaults to 'LOG_CFG_PATH'.
        use_default_config (bool, optional): use default config. Defaults to False.
    """
    if use_default_config:
        default_path = 'default_logging_conf.yaml' 
        path = os.path.abspath(os.path.join(__file__, os.pardir, default_path))
    else:
        if (cfg_path):
            path = cfg_path
        elif env_path:
            path = os.getenv(env_path, None)
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f)
        logging.config.dictConfig(config)
        logging.info(f'Configured logging using the yaml file {path}')
    else:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=default_level)
        logging.warning(f"The specified path {path} wasn't found")
        logging.info(f'Configured logging using the basic configuration')
