#!coding = utf-8
import time
import pytest
def run():
    if __name__ == '__main__':
         pytest.main(['--html=./report%s.html'%time.strftime("_%Y-%m-%d %H%M%S"),'-s','-v','test_deme.py'])

run()