import pypandoc
import os
from pathlib import Path
import shutil
import glob
import shutil

LECTURE_DIR = "./lecture_notes"
TRACK_DIRS = (
    LECTURE_DIR,
    "./course_literature/seminars"
)

MARKDOWN_PATTERN = "*.md"
OUT_DIR = "dist"
compile_summary = True

if __name__ == "__main__":
    combined = []
    shutil.rmtree(OUT_DIR)  # Clear up old files
    for folder in TRACK_DIRS:
        folder = Path(folder)
        for f in folder.rglob(MARKDOWN_PATTERN):
            out_dir = Path(f"{OUT_DIR}/" + str(folder))

            if not os.path.exists(out_dir):  # Make dir if not exist.
                os.makedirs(out_dir)
            output_file = os.path.basename(f).split(".")[0]
            out_dir = out_dir/f"{output_file}.pdf"
            print(f, "\n", out_dir)
            pypandoc.convert_file(os.path.abspath(
                f), to="pdf", outputfile=str(out_dir))

    tex_file = glob.glob('tex2pdf.*')
    for file in tex_file:
        shutil.rmtree(file)
