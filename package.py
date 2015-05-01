import zipfile, os  

import os
def gen_data_files(*dirs):
    zipFile = zipfile.ZipFile('kagami/resources.zip','w')
    results = []
    for src_dir in dirs:
        for root,dirs,files in os.walk(src_dir):
            files =map(lambda f:root + "/" + f, files)
            if files:
                for f in files:
                    zipFile.write(f, f.replace('kagami/',''), zipfile.ZIP_DEFLATED)
    zipFile.close() 

if __name__=='__main__':
    gen_data_files('kagami/java','kagami/js','kagami/python','kagami/resource','kagami/ruby')