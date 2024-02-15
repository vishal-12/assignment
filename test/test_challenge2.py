
"""
        Unit test script - Data Driven
        Execute command:- pytest for executing the test cases

        This will execute all the test cases staring or ending with test
"""

import os
import pytest
from challenge2.challenge2 import Challenge2
from logger.logger import logging
import os

logging = logging()
logging.set_log_file("")

@pytest.fixture
def obj():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(os.path.dirname(current_dir), "config", "test.json")
    return Challenge2(config=config_file)

def test_authentication_create_user(obj):
    baseUrl = obj.getBaseUrl()
    pk = obj.getPk(baseUrl)
    if pk == -1:
        assert obj.runAllApiMethods(url=baseUrl, method='POST', body=obj.getbody()) != -1
    else:
        pytest.skip("User already exists")

def test_retrieve_profile_info(obj):
    baseUrl = obj.getBaseUrl()
    assert baseUrl is not None
    pk = obj.getPk(baseUrl)
    assert pk != -1
    obj.concatInBaseUrl(pk)
    newUrl = obj.getNewUrl()
    assert newUrl is not None
    assert obj.runAllApiMethods(url=newUrl) != -1
#
def test_put_method(obj):
    baseUrl = obj.getBaseUrl()
    assert baseUrl is not None
    pk = obj.getPk(baseUrl)
    assert pk != -1
    obj.concatInBaseUrl(pk)
    newUrl = obj.getNewUrl()
    assert newUrl is not None
    body = obj._vConfig.get("putCall")
    obj.patchBody(body)
    assert obj.runAllApiMethods(url=newUrl, method='PUT', body=obj.getbody()) != -1

def test_patch_method(obj):
    baseUrl = obj.getBaseUrl()
    assert baseUrl is not None
    pk = obj.getPk(baseUrl)
    assert pk != -1
    obj.concatInBaseUrl(pk)
    newUrl = obj.getNewUrl()
    assert newUrl is not None
    body = obj._vConfig.get("patchCall")
    obj.patchBody(body)
    assert obj.runAllApiMethods(url=newUrl, method='PATCH', body=obj.getbody()) != -1
#
def test_validate_profile_info(obj):
    body = obj._vConfig.get("patchCall")
    obj.patchBody(body)
    baseUrl = obj.getBaseUrl()
    pk = obj.getPk(baseUrl)
    assert pk != -1
    obj.concatInBaseUrl(pk)
    newUrl = obj.getNewUrl()
    assert newUrl is not None
    assert obj.runAllApiMethods(url=newUrl) != -1
#
def test_delete_user(obj):
    body = obj._vConfig.get("putCall")
    obj.patchBody(body)
    body = obj._vConfig.get("patchCall")
    obj.patchBody(body)
    baseUrl = obj.getBaseUrl()
    pk = obj.getPk(baseUrl)
    assert pk != -1
    obj.concatInBaseUrl(pk)
    newUrl = obj.getNewUrl()
    assert newUrl is not None
    assert obj.runAllApiMethods(url=newUrl, method="DELETE") != -1
