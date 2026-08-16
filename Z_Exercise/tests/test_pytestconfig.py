import pytest

def test_options(pytestconfig):
    print('args: {}'.format(pytestconfig.args))
    print('inifile :', pytestconfig.inifile)
    print('invocation_dir :', pytestconfig.invocation_dir)
    #assert pytestconfig.getoption('foo') == 'bar'
    #assert pytestconfig.getoption('opt') == False