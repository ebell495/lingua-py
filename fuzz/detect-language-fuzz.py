#!/usr/local/bin/python3
import atheris
import sys

from lingua import Language, LanguageDetectorBuilder
detector = LanguageDetectorBuilder.from_all_languages().build()

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    detector.detect_language_of(fdp.ConsumeUnicode(len(data)))

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()