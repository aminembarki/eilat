#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
minimalistic browser levering off of Python, PyQt and Webkit

Original: https://code.google.com/p/foobrowser/
davydm@gmail.com

+ tabs
+ descargar con click derecho + menú: requiere auxiliar

+ click medio abre new tab
+ proxy
+ actualizar dirección al cambiar de página
+ ctrl-l: address bar
+ ctrl-q: salir
+ dirección destino, [title], ¿status bar?
+ ^J como Enter en address bar
+ zoom
+ buscar en página
+ detecta si es búsqueda o completa el http://
+ movimiento con jk (falta hl)
+ paste (y visita sitio) con 'y'
+ verifica no tráfico no solicitado

Pendiente:

* navegación con teclado
* historia en address bar
* ^H en address bar es backspace

  Copyright (c) 2012, Davyd McColl; 2013, Jaime Soffer

   All rights reserved.

   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are met:

   Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

   Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

   Neither the name of the involved organizations nor the names of its
   contributors may be used to endorse or promote products derived from this
   software without specific prior written permission.

   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
   ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
   LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
   SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
   INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
   CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
   ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
   THE POSSIBILITY OF SUCH DAMAGE.

"""

from PyQt4 import Qt, QtGui, QtCore, QtWebKit, QtNetwork
import sys
from libeilat import *

if __name__ == "__main__":
  # Proxy
  proxy = QtNetwork.QNetworkProxy()
  proxy.setType(QtNetwork.QNetworkProxy.HttpProxy)
  proxy.setHostName('localhost');
  proxy.setPort(3128)
  QtNetwork.QNetworkProxy.setApplicationProxy(proxy);

  app = QtGui.QApplication([])
  cb = app.clipboard()

  completer = Qt.QCompleter()

  app.setApplicationName("Eilat")
  app.setApplicationVersion("0.001")
  mainwin = MainWin(cb)
  mainwin.show()
  for arg in sys.argv[1:]:
    if arg not in ["-debug"]:
      mainwin.load(arg)
  app.exec_()
