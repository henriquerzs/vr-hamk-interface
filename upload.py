#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import cgi, os
import cgitb
import sys

class upload:
    def upload_image(selfZ):
        cgitb.enable()

        try: # Windows needs stdio set for binary mode.
            import msvcrt
            msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
            msvcrt.setmode (1, os.O_BINARY) # stdout = 1
        except ImportError:
            pass

        form = cgi.FieldStorage()

        # A nested FieldStorage instance holds the file
        fileitem = form['file']
        nome = form.getvalue('nome')
        image = os.path.basename(fileitem.filename)

        # Test if the file was uploaded
        if fileitem.filename:

            # strip leading path from file name
            # to avoid directory traversal attacks
            fn = os.path.basename(fileitem.filename)
            open('files/' + fn, 'wb').write(fileitem.file.read())
            message = 'The file "' + fn + '" was uploaded successfully'

        else:
            message = 'No file was uploed'

        # print """
        # Conte# -Type: text/htm# n
        # <html><body>
        # <p>%s</p>
        # <p>%s</p>
        # <p>%s</p>
        # </body></html>
        # """ % (message, nome,image)

        return nome,image


