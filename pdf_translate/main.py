import utils
import sys
import os


MAIN_PATH = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    utils.make_docx_from_pdf(MAIN_PATH + "/static/GameAIPro3_Chapter05_Six_Factory_System_Tricks_for_Extensibility_and_Library_Reuse.pdf")