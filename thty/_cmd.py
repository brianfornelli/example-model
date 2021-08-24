import argparse
from typing import Optional, Dict, Sequence, Callable, Any, Union

DEBUG = False


def _add_command(command: Optional[Dict[str, Callable]]=None) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="THTY model")
    if isinstance(command, Dict):
        parser.add_argument('command', type=str, choices=command.keys(), help=f"Command to run")
    parser.add_argument('--debug',
                        default=DEBUG,
                        type=_str2bool,
                        help=f"Debug run (default:{DEBUG})")
    return parser


def _str2bool(v: Union[bool, str]) -> bool:
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def _kv_parser(val: str) -> Dict[str, Any]:
    d = dict()
    for k in val:
        s = k.replace(" ", "").split("=")
        d.update({s[0]: s[1]})
    return d


class Command(object):
    def __init__(self, command: Union[Optional[Dict[str, Callable]], Callable]=None):
        """
        Command for parsing arbitrary functions
        :param command:
        """
        self.command = command

    def run(self, arguments: Optional[Sequence[str]] = None) -> None:
        """
        Sets up and runs the parser
        :param arguments: Optional[Sequence[str]] = None
        :return: None
        """
        parser = _add_command(self.command)
        args, params = parser.parse_known_args(arguments)
        arg_dict = args.__dict__
        param_dict = _kv_parser(params)
        arg_dict.update(param_dict)

        if isinstance(self.command, Dict):
            self.command[args.command](**arg_dict)
        elif isinstance(self.command, Callable):
            self.command(**arg_dict)
