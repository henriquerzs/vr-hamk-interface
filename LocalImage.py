#!/usr/bin/env python


import cgi
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3

print 'Content-type: text/html'
print ''
print '<html>'
print ('''
    <head>
        <!--Import Google Icon Font-->
        <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <!--Import materialize.css-->
        <link type="text/css" rel="stylesheet" href="static/css/materialize.min.css"  media="screen,projection"/>
        <link href="static/css/css-base.css" rel="stylesheet" type="text/css"/>
        <!--Let browser know website is optimized for mobile-->
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    </head>
''')
print ('''
<body>
        <nav class="nav-extended">
            <div class="nav-wrapper">
                <a href="#" class="brand-logo"><img id="imglogo" src="static/imgs/hamkW2.png" /></a>

                <a href="#" data-activates="mobile-demo" class="button-collapse"><i class="material-icons">menu</i></a>
                <ul id="nav-mobile" class="right hide-on-med-and-down">
					<li><a href="index.py">Home</a></li>
                    <li><a href="#">About Project</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">GitHub</a></li>

                </ul>
                <ul class="side-nav" id="mobile-demo">
                    <li><a href="sass.html">Sass</a></li>
                    <li><a href="badges.html">Components</a></li>
                    <li><a href="collapsible.html">JavaScript</a></li>
                </ul>
            </div>
            <div class="nav-content">
                <ul class="tabs tabs-transparent">                    
                    <li class="tab"><a class="active" href="#test2">Visual Recognition Project</a></li>
                    <li class="tab disabled"><a href="#test3">Disabled Tab</a></li>

                </ul>
            </div>
        </nav>

        

        
''')

#formulario = cgi.FieldStorage()
#nome = formulario.getvalue("nome")
#url_image = formulario.getvalue("url")

# Configuracao da API
VR = VisualRecognitionV3(version='2016-05-20', api_key='8b916c3ab946fd1da094dd1a48cb8b3e9ac46a3f')

from upload import upload
upload = upload()
dados = upload.upload_image()
nome = dados[0]
imagem = dados[1]

with open(join(dirname(__file__), 'files/'+imagem),'rb') as image_file:
	Resultados = VR.classify(images_file=image_file)

#Mostra o resultado no formato json
ResultJson = json.dumps(Resultados, indent=2)

StringA = ""
#Mostra os resultados individuais por classe
for i in Resultados['images'][0]['classifiers'][0]['classes']:
    # if i['score']>=0.85:
    StringA = StringA + '\n Score: '+str(i['score'])+' Ha ' + str(i['score']*100) + ' % de chances da imagem conter(Classe): '+ i['class']+"<br>"


substituir = '''
<div class="row">
            <div class="col s12"><h3>Result about the image:</h3></div>
            <div class="col s4"><img class="materialboxed" data-caption="%s -> (%s)" width="350px" src="%s"></div>

            <div class="col s8">
                <div class="card">
                    <div class="card-content">
                        <p>Choose your prefered option.</p>
                    </div>
                    <div class="card-tabs">
                        <ul class="tabs tabs-fixed-width">
                            <li class="tab"><a href="#test6">Informations</a></li>
                            <li class="tab"><a href="#test5">Classes</a></li>
                            <li class="tab"><a href="#test4">JSON</a></li>
                            
                            
                        </ul>
                    </div>
                    <div class="card-content grey lighten-4">
                        <div id="teste6">
                            <h5>Image Name:</h5><p>%s</p>
                            <h5>Image URL:</h5><p>%s</p>
                        </div>
                        <div id="test5"><h5>Classes:</h5><p>%s</p></div>
                        <div id="test4"><h5>JSON:</h5><p>%s</p></div>
                        
                    </div>
                </div>
            </div>
        </div>         

'''

#StringA = "CLASSES"
#ResultJson = "CLASSES EM JSON"
print substituir % (nome,imagem,'files/'+imagem,nome, imagem,StringA,ResultJson)





print ('''
<footer class="page-footer">
            <div class="container">
                <div class="row">
                    <div class="col l6 s12">
                        <h5 class="white-text">Footer Content</h5>
                        <p class="grey-text text-lighten-4">Any text ...</p>
                    </div>
                    <div class="col l4 offset-l2 s12">
                        <h5 class="white-text">Links</h5>
                        <ul>
                            <li><a class="grey-text text-lighten-3" href="#">Link 1</a></li>
                            <li><a class="grey-text text-lighten-3" href="#">Link 2</a></li>
                            <li><a class="grey-text text-lighten-3" href="#">Link 3</a></li>
                            <li><a class="grey-text text-lighten-3" href="#">Link 4</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="footer-copyright">
                <div class="container">
                     2017 Copyright HAMK University
                    <a class="grey-text text-lighten-4 right" href="#">More Links</a>
                </div>
            </div>
        </footer>
		<!--Import jQuery before materialize.js-->
        <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
        <script type="text/javascript" src="static/js/materialize.min.js"></script>
    </body>
''')
print '</html>'