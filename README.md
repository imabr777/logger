# logger

A little module for Python that helps me write messages to a log file. Especially useful for longer runtimes

## Author

Abraham Im (github/imabr777)

## Documentation

### start_run(file_path)

Starts timer on this run and writes a starting line in the input file
*file_path: A file path to which the starting line in the log will be written*

### end_run(file_path)

Ends timer on this run and writes an ending line in the input file
*file_path: A file path to which the ending line in the log will be written*

## write_error(file_path, error_msg)

Writes an exception message to the input file
*file_path: A file path to which the exception will be written*
*error_msg: The error message to be written*

## write_log(file_path, log_msg)
Writes a log message to the input file
*file_path: A file path to which the log message will be written*
*log_msg: The log message to be written*