from typing import (Dict, Any)

from ._cmd import (Command, _str2bool)
from .thty import (score_dense, score_sparse)


def _score_dense(idb: str, itbl: str, odb: str, otbl: str, prediction: str, **kwargs: Dict[str, Any]) -> None:
    score_dense(idb=idb, itbl=itbl, odb=odb, otbl=otbl, prediction=prediction)


def _score_sparse(idb: str, itbl: str, odb: str, otbl: str, prediction: str, **kwargs: Dict[str, Any]) -> None:
    score_sparse(idb=idb, itbl=itbl, odb=odb, otbl=otbl, prediction=prediction)


COMMAND = dict(score_dense=_score_dense, score_sparse=_score_sparse)


def main() -> None:
    cmd = Command(COMMAND)
    cmd.run()


if __name__ == '__main__':
    main()
