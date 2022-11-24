# python-log-router

A package that allows logs to be routed to different log handlers based on a discriminant.

## Installation

`pip install logrouter`

## Usage

Call `logrouter.setup_logging()` to setup the logging configuration by providing the configuration yaml absolute file path. You can also set the configuration path using an environment variable. Specify the name of the env variable by setting the `env_path` parameter.

For an example of a configuration file, refer to the [default configuration file](https://github.com/IBM/python-log-router/blob/main/logrouter/default_logging_conf.yaml). You can specify the log handler to be used by replacing `handlers.single_handler_class` with the name of your handler. Default is `logrouter.logrouter.DefaultHandler`.

The default logging configuration will route the logs based on the `discriminator` field of the LogRecord object.
To use the default configuration, call `logrouter.setup_logging(use_default_config=True)`.

## Examples

Run and look at the logs of the examples located at [`/examples`](https://github.com/IBM/python-log-router/blob/main/examples/)

