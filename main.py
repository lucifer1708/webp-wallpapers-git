from flask import Flask, abort, render_template, send_file
import os
# from flask_autoindex import AutoIndex
app = Flask(__name__)


@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = './images/'

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('files.html', files=files)


# ppath = "/home/lucifer/Pictures/walls/images"  # update your own parent directory here

# AutoIndex(app, browse_root=ppath)

# if __name__ == "__main__":
#     app.run()
