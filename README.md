# Web sockets - Threading - Qt Designer.

<div align="justify">
  Este repositorio tiene código para generar un servidor con tecnología web socket. Atiende los mensajes de 2 clientes, quienes juegan <b>piedra, papel o tijera</b>. La respuesta es enviada desde los clientes y el servidor es el encargado de hacer la lógica para escoger al ganador. 
  Para atender los mensajes enviados por los 2 clientes se utiliza el módulo threading, esto permite asignar un hilo de trabajo a cada uno. Se usa un 3er hilo para manejar las respuestas de los clientes.
</div>

# CONTENIDO.
* [Servidor](#servidor)
* [Cliente](#cliente)
* [GUI (PySide2)](#gui)
