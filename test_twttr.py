#import twttr
from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"

def test_shorten_wo_aouiy():
    assert shorten("twttr") == "twttr"

def test_shorten_only_aouiy():
    assert shorten("aoui") == ""

def test_shorten_other_char():
    assert shorten("kakosd-joklu4jyekl") == "kksd-jkl4jykl"
