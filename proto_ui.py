from PySide2 import QtWidgets

# metas:
# rapido prototipo de UI que permite a un usuario seleccionar un archivo excel y decir SI o NO mandar invites

# 1- boton para seleccionar archivo, seccion para recordarle al usuario que archivo es
# 2- boton para ejecutar process_invites
# 3- seccion para ver el resultado del response del process:
# ------ 3b > detalles de invites rejected
# 4- seccion de botones para decidir si subir o no el invite
# 5- mensaje resultado del boton con carita feliz o triste


# 1- Vamos a crear nuestro propio widget que contiene cada parte mencionada
class ProtoInvites(QtWidgets.QWidget):
    """docstring for ProtoInvites"""
    def __init__(self, *args, **kwargs):
        super(ProtoInvites, self).__init__(*args, **kwargs)
        self.loadUI()

    def loadUI(self):
        # agregar todos los widgets mencionados aqui
        # 1
        self.source_file_pb = QtWidgets.QPushButton('Select Source File Path')
        self.source_file_le = QtWidgets.QLineEdit()
        self.source_file_le.setReadOnly(True)
        self.source_file_pb.clicked.connect(self.select_file)
        # layout: le >> pb
        source_file_layout = QtWidgets.QHBoxLayout()
        source_file_layout.addWidget(self.source_file_le)
        source_file_layout.addWidget(self.source_file_pb)

        # 2, 3
        self.process_pb = QtWidgets.QPushButton('Process Invites')
        self.process_result = QtWidgets.QTextBrowser()
        process_layout = QtWidgets.QVBoxLayout()
        process_layout.addWidget(self.process_pb)
        process_layout.addWidget(self.process_result)

        # 4
        self.submit_pb = QtWidgets.QPushButton('Submit!')
        self.abort_pb = QtWidgets.QPushButton('Abort!')
        decide_layout = QtWidgets.QHBoxLayout()
        decide_layout.addWidget(self.submit_pb)
        decide_layout.addWidget(self.abort_pb)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(source_file_layout)
        main_layout.addLayout(process_layout)
        main_layout.addLayout(decide_layout)

        self.setLayout(main_layout)

    def select_file(self):
        fpath, ext = QtWidgets.QFileDialog.getOpenFileName(filter="Excel Files (*.py)")
        if not fpath:
            return
        self.source_file_le.setText(fpath)

pi = ProtoInvites()
pi.show()