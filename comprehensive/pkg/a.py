from typing import Dict
from typing import Union

from pkg._internal import ExposedClass2
from pkg._internal import ExposedClass3
from pkg._internal import ExposedClass5
from pkg._internal import ExposedClass6
from pkg._internal import ExposedClass7
from pkg._internal import ExposedClass8
from pkg._internal import ExposedClass9
from pkg._internal import ExposedClass10
from pkg._internal import ExposedClass11
from pkg._internal import ExposedClass12
from pkg._internal import InternalClass
from pkg._internal import _InternalClass
from pkg._internal2 import Internal


class A:
    def __init__(self, a: int, b: str, c: float = 1.0) -> None:
        self.a = a
        self._b = b
        self._c: InternalClass = InternalClass(a, b)
        self.d: ExposedClass2 = ExposedClass2()
        self.e: Dict[str, ExposedClass11] = dict()

    def public_method(self):
        pass

    def public_method2(self) -> int:
        return 5

    def _private_method(self):
        pass

    def public_method_internal_return(self) -> ExposedClass3:
        return ExposedClass3()

    def public_method_internal_argument(self, arg: ExposedClass5) -> None:
        return

    def public_method_internal_return_union(
        self,
    ) -> Union[ExposedClass6, ExposedClass7]:
        return ExposedClass6()

    @property
    def public_propery_internal_return(self) -> ExposedClass10:
        return ExposedClass10()


class _A:
    pass


def hello() -> int:
    return 3


def public_function_internal_return() -> ExposedClass9:
    return ExposedClass9()


def _hello():
    return


var = ExposedClass8()  # type: ExposedClass8

pub_var1 = pub_var2 = ExposedClass12()  # type: ExposedClass12

_var = _InternalClass()

_x = [0]
_x[0] = 4
