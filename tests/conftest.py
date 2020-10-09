from flask import Flask, jsonify
import sys
import os

sys.path.append(os.path.abspath('../'))

from json_db_client import JsonDbClient
import pytest

@pytest.fixture
def json_db_client():
    return JsonDbClient('./tickets_db_for_test.json')