from __future__ import print_function
import shutil
from PIL import Image
from builtins import object
from builtins import str
from qgis.PyQt.QtWidgets import QMessageBox
from ..db.pyarchinit_conn_strings import *

class Media_utility(object):
    """

        # import the Image module
        import Image

        # assign the image path to a variable using a raw string
        image_path = r"C:\test\snake.png"

        # open the image
        image = Image.open(image_path)

        # resize the image to 150x110
        width, height = (150, 110)

        # assign width and height to size variable
        size = (width, height)

        # create a new image path for the thumbnail
        new_image_thumbnail = r"C:\test\snake_small.png"

        # create the thumbnail using the Image.thumbnail method with the Image.ANTIALIAS filter
        image.thumbnail(size, Image.ANTIALIAS)

        # save the new thumbnail image
        image.save(new_image_thumbnail)

        #The class uses the Image module from the Python Imaging Library(PIL) to open, resize and save the image, the class uses the method thumbnail to create the thumbnail and it uses the Image.ANTIALIAS filter to smooth the image. The class also uses the method save to save the new thumbnail image.


    """

    def resample_images(self, mid, ip, i, o, ts):
        self.max_num_id = mid
        self.input_path = ip
        self.infile = i
        self.outpath = o
        self.thumb_suffix = ts

        size = 150, 150
        infile = str(self.input_path)
        outfile = ('%s%s_%s%s') % (
        self.outpath, str(self.max_num_id), os.path.splitext(self.infile)[0], self.thumb_suffix)
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(outfile, dpi=(100, 100))


if __name__ == '__main__':
    m = Media_utility()
    conn = Connection()
    thumb_path = conn.thumb_path()
    thumb_path_str = thumb_path['thumb_path']
    print(thumb_path_str)
    

class Media_utility_resize(object):


    def resample_images(self, mid, ip, i, o, ts):
        self.max_num_id = mid
        self.input_path = ip
        self.infile = i
        self.outpath = o
        self.thumb_suffix = ts

        size = 2008, 1417
        infile = str(self.input_path)
        outfile = ('%s%s_%s%s') % (
        self.outpath, str(self.max_num_id), os.path.splitext(self.infile)[0], self.thumb_suffix)
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(outfile, dpi=(300, 300))


if __name__ == '__main__':
    m = Media_utility_resize()
    conn = Connection()
    thumb_resize = conn.thumb_resize()
    thumb_resize_str = thumb_resize['thumb_resize']
    print(thumb_resize_str)
    
class Video_utility(object):


    def resample_images(self, mid, ip, i, o, ts):
        self.max_num_id = mid
        self.input_path = ip
        self.infile = i
        self.outpath = o
        self.thumb_suffix = ts

        #size = 2008, 1417
        infile = str(self.input_path)
        outfile = ('%s%s_%s%s') % (
        self.outpath, str(self.max_num_id), os.path.splitext(self.infile)[0], self.thumb_suffix)
        shutil.move(infile, outfile)
            

if __name__ == '__main__':
    m = Video_utility()
    conn = Connection()
    thumb_path = conn.thumb_path()
    thumb_path_str = thumb_path['thumb_path']
    print(thumb_path_str)   
    
class Video_utility_resize(object):


    def resample_images(self, mid, ip, i, o, ts):
        self.max_num_id = mid
        self.input_path = ip
        self.infile = i
        self.outpath = o
        self.thumb_suffix = ts

        #size = 2008, 1417
        infile = str(self.input_path)
        outfile = ('%s%s_%s%s') % (
        self.outpath, str(self.max_num_id), os.path.splitext(self.infile)[0], self.thumb_suffix)
        shutil.copy(infile, outfile)
            

if __name__ == '__main__':
    m = Video_utility_resize()
    conn = Connection()
    thumb_resize = conn.thumb_resize()
    thumb_resize_str = thumb_resize['thumb_resize']
    print(thumb_resize_str)   
