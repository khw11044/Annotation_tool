"""
Start the web server.

$ python run.py \
--debug \
--port 8008
"""

"""
python3 -m annotation_tools.db_dataset_utils --action load \
    --dataset /home/khw11044/golf/me/extract_data/f_frame_pose/f_00517.json \
        --normalize 
"""
# http://localhost:8008/edit_task/?category_id=1

import argparse
import json

from annotation_tools.annotation_tools import app

DEFAULT_PORT = 8008
DEFAULT_HOST = '127.0.0.1'


def parse_args():

    parser = argparse.ArgumentParser(
        description='Visipedia Annotation Toolkit')

    parser.add_argument('--debug', dest='debug',
                        help='Run in debug mode.',
                        required=False, action='store_true', default=False)

    parser.add_argument('--port', dest='port',
                        help='Port to run on.', type=int,
                        required=False, default=DEFAULT_PORT)

    parser.add_argument('--host', dest='host',
                        help='Host to run on, set to 0.0.0.0 for remote access', type=str,
                        required=False, default=DEFAULT_HOST)

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
