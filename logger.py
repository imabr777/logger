#!usr/bin/env python3

import os
from datetime import datetime


def start_run(file_path):
	"""Starts timer on this run and writes a starting line in the input file
	:param file_path: A file path to which the starting line in the log will be written
	:return:
	"""
	_write_helper("START {0} at {1}".format(os.path.basename(file_path), datetime.now().strftime("%Y/%m/%d %H:%M:%S")))


def end_run(file_path):
	"""Ends timer on this run and writes an ending line in the input file
	:param file_path: A file path to which the ending line in the log will be written
	:return:
	"""
	_write_helper("END {0} at {1}".format(os.path.basename(file_path), datetime.now().strftime("%Y/%m/%d %H:%M:%S")))


def write_error(file_path, error_msg):
	"""Writes an exception message to the input file
	:param file_path: A file path to which the exception will be written
	:param error_msg: The error message to be written
	:return:
	"""
	_write_helper("ERROR - {0} at {1}".format(error_msg, datetime.now().strftime("%Y/%m/%d %H:%M:%S")))


def write_log(file_path, log_msg):
	"""Writes a log message to the input file
	:param file_path: A file path to which the log message will be written
	:param log_msg: The log message to be written
	:return:
	"""
	_write_helper("LOG - {0} at {1}".format(log_msg, datetime.now().strftime("%Y/%m/%d %H:%M:%S")))


def _write_helper(file_path, msg):
	"""Does actual work of writing to the log file
	:param file_path: A file path to which the log message will be written
	:param msg: The full log message
	:return:
	"""
	with open(file_path, "a") as log:
		log.writelines(msg)
		print(msg)