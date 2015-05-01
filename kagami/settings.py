import os
import zipfile
dirname = os.path.dirname(__file__)
kagami_resources = zipfile.ZipFile(os.path.join(dirname,"resources.zip"), "r")
