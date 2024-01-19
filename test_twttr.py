#import twttr
import sys
from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"

def test_shorten_wo_aouiy():
    assert shorten("twttr") == "twttr"

def test_shorten_only_aouiy():
    assert shorten("aouiy") == ""

def test_shorten_other_char():
    assert shorten("kakosd-joklu4jyekl") == "kksd-jkl4jkl"

def test_shorten_capitalized():
    assert shorten("kakOsd-jOklU4jYEkl") == "kksd-jkl4jkl"

def test_shorten_nostring():
    assert shorten("") == ""

sys.exit(0)
