import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


from datetime import datetime, timezone
def test_iso_utc():
    dt = datetime(2020,1,1,12,0,0,tzinfo=timezone.utc)
    assert mod.iso_utc(dt).endswith("+00:00")
    assert "2020-01-01T12:00:00" in mod.iso_utc("2020-01-01T12:00:00")
