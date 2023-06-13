#!/usr/bin/env python
#SETMODE 777

#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    Nick Maclean

:synopsis:
    Script for generating blurry (low-resolution) images.

:description:
    This script can be run as-is. Make sure to install the Pillow python module first though.
"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Built-in
import inspect
import os
import sys
from typing import Callable

# Third party
try:
    from PIL import Image
except ModuleNotFoundError:
    print("The pillow module is a required dependency. Run 'pip install pillow', then try to run this file again.")
    sys.exit()

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#


def _log(label: str, message: str, indent: str, caller):
    caller_file = caller.f_back.f_code.co_filename
    caller_line = caller.f_back.f_lineno
    caller_name = caller.f_back.f_code.co_name

    print(f"{label}: {message}")
    print(f"{indent}  {caller_name}(): Line number {caller_line}")
    print(f"{indent}  File {caller_file}")


def log_message(message: str): _log("INFO", message, "    ", inspect.currentframe().f_back)
def log_warning(message: str): _log("WARNING", message, "       ", inspect.currentframe().f_back)
def log_error(message: str): _log("ERROR", message, "     ", inspect.currentframe().f_back)


def iterate_through_files(directory: str, callback: Callable[[str, str], None], ext: str = None) -> int:
    """
    Recursively search files under the directory and performs the callback on each file.

    :param directory: parent directory to search underneath
    :param callback: function performed on each file
    :param ext: all files must have this extension to be considered
    :return: number of files successfully iterated
    :type: int
    """
    if not os.path.isdir(directory):
        log_error(f"Provided directory is not valid: {directory}")
        return None

    count = 0
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            # apply extension filter, if provided
            if ext:
                if isinstance(ext, str):
                    ext = [ext]

                found = False
                for ex in ext:
                    if file.lower().endswith(ex):
                        found = True
                        break
                if not found:
                    continue

            try:
                callback(root, file)
            except:
                continue

            count += 1

    return count


def update_image_resolution(input_image_path: str, output_image_path: str, output_resolution: tuple[int, int]) -> bool:
    """
    Creates a copy of the input image with a new resolution.

    :param input_image_path:
    :param output_image_path:
    :param output_resolution:
    :return: success
    """
    if not os.path.isfile(input_image_path):
        log_error(f"Provided input path is not valid: {input_image_path}")
        return None

    input_ext = os.path.splitext(input_image_path)[1]
    output_ext = os.path.splitext(output_image_path)[1]
    if input_ext != output_ext:
        print(f"Input and output file extensions do not match: {input_image_path} and {output_image_path}")
        return None

    image = Image.open(input_image_path)
    image.thumbnail(output_resolution)

    try:
        image.save(output_image_path, progressive=True, quality=100)
    except OSError:
        log_error(f"Unable to write to path: {output_image_path}")
        return None

    return True


def smart_create_responsive_image(directory: str, file_name: str):
    """
    Creates a low resolution image (.blur) for the provided image. Handles file path creation
    and skips files according to custom logic.
    """
    # skip favicon
    if file_name == "favicon-256.png":
        return True

    # build/validate input path
    file_path = os.path.join(directory, file_name)
    if not os.path.isfile(file_path):
        log_error(f"Provided file could not be found: {file_path}")
        return None

    # handle .blur image
    # 1. delete if parent image no longer exists
    # 2. ignore if parent does exist
    file_ext = os.path.splitext(file_name)
    blur_ext = os.path.splitext(file_ext[0])
    if blur_ext[1] == ".blur":
        parent_path = os.path.join(directory, f"{blur_ext[0]}{file_ext[1]}")
        if os.path.isfile(parent_path):
            return True
        else:
            log_message(f"Deleting blurry image (its parent is missing): {file_path}")
            os.remove(file_path)
            return False

    # create output path
    input_split = os.path.splitext(file_path)
    output_file_path = f"{input_split[0]}.blur{input_split[1]}"

    # check if blurry image has already been created
    # skip this image, if the blurry image is up-to-date
    if os.path.isfile(output_file_path):
        if os.path.getmtime(output_file_path) > os.path.getmtime(file_path):
            # log_message(f"Skipping image, the blurry version is up to date: {file_path}")
            return True

    # create blurry image
    output_resolution = (64, 64)
    return update_image_resolution(file_path, output_file_path, output_resolution)


#----------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------- MAIN --#


def main():
    current_dir = os.path.abspath(os.getcwd())
    directory = os.path.join(current_dir, "assets", "images")
    iterate_through_files(directory, smart_create_responsive_image, ["png", "gif", "jpg"])


if __name__ == '__main__':
    main()
