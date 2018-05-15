import os
import sys

from mapillary_tools.process_import_meta_properties import process_import_meta_properties


class Command:
    name = 'extract_import_meta_data'
    help = "Extract import meta data."

    def add_arguments(self, parser):
        # general arguments
        parser.add_argument(
            'path', help='path to your photos, or in case of video, path where the photos from video sampling will be saved')
        parser.add_argument(
            '--skip_subfolders', help='Skip all subfolders and import only the images in the given directory path.', action='store_true', default=False, required=False)
        # force rerun process, will rewrite the json and update the processing
        parser.add_argument(
            '--verbose', help='print debug info', action='store_true', default=False, required=False)
        parser.add_argument(
            '--rerun', help='rerun the processing', action='store_true', required=False)

        # command specific args
        parser.add_argument(
            "--device_make", help="Specify device manufacturer. Note this input has precedence over the input read from the import source file.", default=None, required=False)
        parser.add_argument(
            "--device_model", help="Specify device model. Note this input has precedence over the input read from the import source file.", default=None, required=False)
        parser.add_argument(
            '--add_file_name', help="Add original file name to EXIF. Note this input has precedence over the input read from the import source file.", action='store_true', required=False)
        parser.add_argument(
            '--add_import_date', help="Add import date.", action='store_true', required=False)
        parser.add_argument('--orientation', help='Specify the image orientation in degrees. Note this might result in image rotation. Note this input has precedence over the input read from the import source file.',
                            choices=[0, 90, 180, 270], type=int, default=None, required=False)
        parser.add_argument(
            "--GPS_accuracy", help="GPS accuracy in meters. Note this input has precedence over the input read from the import source file.", default=None, required=False)
        parser.add_argument(
            '--import_meta_source', help='Provide the source of import properties.', action='store',
            choices=['exif', 'json'], default=None, required=False)
        parser.add_argument(
            '--import_meta_source_path', help='Provide the path to the file source of import specific information. Note, only JSON format is supported.', action='store',
            default=None, required=False)

    def run(self, args):

        # basic check for all
        import_path = os.path.abspath(args.path)
        if not os.path.isdir(import_path):
            print("Error, import directory " + import_path +
                  " doesnt not exist, exiting...")
            sys.exit()

        process_import_meta_properties(import_path,
                                       args.orientation,
                                       args.device_make,
                                       args.device_model,
                                       args.GPS_accuracy,
                                       args.add_file_name,
                                       args.add_import_date,
                                       args.import_meta_source,
                                       args.import_meta_source_path,
                                       args.verbose,
                                       args.rerun,
                                       args.skip_subfolders)
