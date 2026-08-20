"""Scratch module to trigger a real CodeQL py/ineffectual-statement finding for
OpenSRE's fix_github_security_alert tool verification. Deleted after."""

from __future__ import annotations

from typing import Protocol


class VerifyCodeqlProtocol(Protocol):
    def do_thing(self, value: int) -> int: ...
