import atheris
import sys

from lingua import Language, LanguageDetectorBuilder
detector = LanguageDetectorBuilder.from_all_languages().build()

@atheris.instrument_func
def TestOneInput(data):
    detector.detect_language_of(str(data))

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()