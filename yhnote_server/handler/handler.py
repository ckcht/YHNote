from abc import ABCMeta,abstractmethod,abstractproperty
import sys
sys.path.append('../')
from common.yh_helper import get_uuid

class Handler(object):
    __metaclass__ = ABCMeta

    def get_uuid(self):
        return get_uuid()

    @abstractmethod
    def handler(self, request, db): pass