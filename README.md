# python-log-router

A package that allows logs to be routed to different log handlers based on a discriminant. Each unique value of the discriminant is managed by a distinct handler.

## Installation

`pip install logrouter`

## Usage

Call `logrouter.setup_logging()` to setup the logging configuration by providing the configuration yaml absolute file path. You can also set the configuration path using an environment variable. Specify the name of the env variable by setting the `env_path` parameter.

For an example of a configuration file, refer to the [default configuration file](https://github.com/IBM/python-log-router/blob/main/logrouter/default_logging_conf.yaml). You can specify the log handler to be used by replacing `handlers.single_handler_class` with the name of the handler. The default one is `logrouter.logrouter.DefaultHandler`, which inherits from `logging.FileHandler`.

The default logging configuration will route all the logs based on the `discriminator` field of the LogRecord object. To use the default configuration, call `logrouter.setup_logging(use_default_config=True)`.

## Examples

Run and look at the code and logs produced of the examples located at [`/examples`](https://github.com/IBM/python-log-router/blob/main/examples/) to experience what you can achieve with `logrouter`.

## Using different types of handlers

A new instance of `single_handler_class` handler class is used for each discriminator unique value. This instance receives the log level and the discriminator value when created. If you want to use a differnet handler class for some discriminant values, specify them in `handlers.handlers_dict` in the logging configuration file. See [this example](https://github.com/IBM/python-log-router/tree/main/examples/handlers_by_discriminant_value).
