#!coding = utf-8
import time
import pytest
def run():
    if __name__ == '__main__':
         pytest.main(['--html=./Report/report%s.html'%time.strftime("_%Y-%m-%d %H%M%S"),'-s','-v'])

run()