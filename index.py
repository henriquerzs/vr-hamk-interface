#!/usr/bin/env python

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
<div id="test2" class="col s12">
            <div id="central">
                <div class="card">
                    <div class="card-content">
                        <p>Select how you want to classify your image.</p>
                    </div>
                    <div class="card-tabs">
                        <ul class="tabs tabs-fixed-width">
                            <li class="tab"><a href="#test4">Local Image</a></li>
                            <li class="tab"><a class="active" href="#test5">URL Image</a></li>
                            <li class="tab"><a href="#test6">Example</a></li>
                        </ul>
                    </div>
                    <div class="card-content grey lighten-4">
                        <div id="test4">
                            <form action="LocalImage.py" enctype="multipart/form-data" method="post">
                                <div class="input-field col s6">
                                    <i class="material-icons prefix">stars</i>
                                    <input id="icon_prefix" type="text" class="validate" name="nome">
                                    <label for="icon_prefix">Image Name</label>
                                </div>
                                <div class="file-field input-field">
                                    <div class="btn">
                                        <span>File</span>
                                        <input type="file" name="file">
                                    </div>
                                    <div class="file-path-wrapper">
                                        <input class="file-path validate" type="text" name="url">
                                    </div>
                                
                                </div>
                                <button class="btn waves-effect waves-light" type="submit" name="action">Submit
                                    <i class="material-icons right">send</i>
                                </button>
                            </form>
                        </div>
                        <div id="test5"><form action="UrlImage.py">
                                <div class="input-field col s6">
                                    <i class="material-icons prefix">stars</i>
                                    <input id="icon_prefix" type="text" class="validate" name="nome">
                                    <label for="icon_prefix">Image Name</label>
                                </div>
                                <div class="input-field col s6">
                                    <i class="material-icons prefix">picture_in_picture</i>
                                    <input id="icon_prefix" type="text" class="validate" name="url">
                                    <label for="icon_prefix">Image URL</label>
                                </div>
                                <button class="btn waves-effect waves-light" type="submit" name="action">Submit
                                    <i class="material-icons right">send</i>
                                </button>
                            </form></div>
                        <div id="test6">Test 3</div>
                    </div>
                </div>
            </div>

        </div>
        

        <!--Import jQuery before materialize.js-->
        <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
        <script type="text/javascript" src="static/js/materialize.min.js"></script>
    </body>
''')
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
''')
print '</html>'