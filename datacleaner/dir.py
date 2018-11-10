"""
dir.py

Clean and edit data directory
"""

import os, sys, time
import json
import tornado.web
from stat import S_ISREG, ST_MTIME, ST_MODE, ST_CTIME, ST_ATIME


class DirManager:

    def run(self, args):
        WebServer(args[0]).start()


class WebServer(tornado.web.Application):

    def __init__(self, data_path):
        if not os.path.exists(data_path):
            raise ValueError('The path {} does not exist.'.format(data_path))

        this_dir = os.path.dirname(os.path.realpath(__file__))
        static_file_path = os.path.join(this_dir, 'dir_web', 'static')
        print(static_file_path)



        handlers = [
            (r"/", tornado.web.RedirectHandler, dict(url="/dirs")),
            (r"/dirs", DirsView, dict(data_path=data_path)),
            (r"/dirs/?(?P<dir_id>[^/]+)?", DirView),
            (r"/api/dirs/?(?P<dir_id>[^/]+)?", DirApi, dict(data_path=data_path)),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": static_file_path}),
            (r"/dir_data/(.*)", tornado.web.StaticFileHandler, {"path": data_path}),
            ]

        settings = {'debug': True}

        super().__init__(handlers, **settings)

    def start(self, port=8886):
        self.port = int(port)
        self.listen(self.port)
        print('Listening on {}...'.format(port))
        tornado.ioloop.IOLoop.instance().start()


class DirsView(tornado.web.RequestHandler):

    def initialize(self, data_path):
        self.data_path = data_path

    def get(self):
        import fnmatch
        dir_list = fnmatch.filter(os.listdir(self.data_path), '*')
        dir_list.sort()
        data = {"dirs": dir_list}
        print(data)
        self.render("dir_web/dirs.html", **data)


class DirView(tornado.web.RequestHandler):

    def get(self, dir_id):
        data = {}
        self.render("dir_web/dir.html", **data)


class DirApi(tornado.web.RequestHandler):

    def initialize(self, data_path):
        self.data_path = data_path

    def image_path(self, dir_path, frame_id):  #fl_name):
        #return os.path.join(dir_path, str(frame_id) + "_cam-image_array_.jpg")
        return os.path.join(dir_path, str(frame_id) + ".png")
        

    def clips_of_dir(self, dir_path):
        #dirFiles = os.listdir(dir_path)
        #dirFiles.sort(key=lambda f: int(filter(str.isdigit, f)))
        #seqs = [ int(f.split("_")[0]) for f in os.listdir(tub_path) if f.endswith('.jpg') ]
        #seqs.sort()

        dirFiles = [ int(f.split(".")[0]) for f in os.listdir(dir_path) if f.endswith('.png') ]
        dirFiles.sort()

        entries = ((os.stat(self.image_path(dir_path, dir))[ST_ATIME], dir) for dir in dirFiles)

        (last_ts, dir) = next(entries)
        clips = [[dir]]
        for next_ts, next_seq in entries:
            if next_ts - last_ts > 100:  #greater than 1s apart
                clips.append([next_seq])
            else:
                clips[-1].append(next_seq)
            last_ts = next_ts

        return clips

    def get(self, dir_id):
        clips = self.clips_of_dir(os.path.join(self.data_path, dir_id))

        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json.dumps({'clips': clips}))

    def post(self, dir_id):
        #tub_path = os.path.join(self.data_path, tub_id)
        dir_path = os.path.join(self.data_path, dir_id)
        #old_clips = self.clips_of_tub(tub_path)
        old_clips = self.clips_of_dir(dir_path)
        new_clips = tornado.escape.json_decode(self.request.body)

        import itertools
        old_frames = list(itertools.chain(*old_clips))
        new_frames = list(itertools.chain(*new_clips['clips']))
        frames_to_delete = [str(item) for item in old_frames if item not in new_frames]
        for frm in frames_to_delete:
            #os.remove(self.image_path(tub_path, frm))
            os.remove(self.image_path(dir_path, frm))
