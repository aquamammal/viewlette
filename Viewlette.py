import sys, random, datetime
from PyQt5 import QtWidgets, QtGui

randommovie = ' her'

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        with open("movieslist.txt") as file:
            movieliststring = file.read()
        movielist = movieliststring.splitlines()
        listlength = str(len(movielist))

        font = QtGui.QFont()
        self.EnterMovieLineEdit = QtWidgets.QLineEdit()
        font.setPointSize(25)
        self.EnterMovieLineEdit.setFont(font)
        
        self.Movieaddedstatuslabel = QtWidgets.QLabel('No Movie Added')
        self.Movielistlength = QtWidgets.QLabel('List Length:' + listlength)
        self.b1 = QtWidgets.QPushButton('Add Movie to List')
        self.moviesuggestion = QtWidgets.QLabel('Random Movie Is')
        self.moviesuggestion.setFont(font)
        self.moviestatus = QtWidgets.QLabel('')
        self.b2 = QtWidgets.QPushButton('Seen')
        self.b3 = QtWidgets.QPushButton('Next Movie')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.EnterMovieLineEdit)
        v_box.addWidget(self.Movieaddedstatuslabel)
        v_box.addWidget(self.Movielistlength)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.moviesuggestion)
        v_box.addWidget(self.moviestatus)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.b3)

        self.setLayout(v_box)
        self.setWindowTitle('VIEWLETTE')

        self.b1.clicked.connect(self.btn_clk)
        self.b2.clicked.connect(self.btn_clk)
        self.b3.clicked.connect(self.btn_clk)
        self.EnterMovieLineEdit.returnPressed.connect(self.b1.click)

        self.show()

    def btn_clk(self):
        sender = self.sender()
        global randommovie
        
        with open("movieslist.txt") as file:
            movieliststring = file.read()
        movielist = movieliststring.splitlines()

        if sender.text() == 'Add Movie to List':

            newmovieinput = self.EnterMovieLineEdit.text()

            if newmovieinput == "":
                self.Movieaddedstatuslabel.setText("No Movie Added")
                newmovielist = movielist
            else:
                movielist.append(newmovieinput)
                self.Movieaddedstatuslabel.setText( newmovieinput + " Added")
                newmovielist = movielist

            nonduplicatenewmovielist = list(dict.fromkeys(newmovielist)) #checkforduplicates

            movielistfile = open("movieslist.txt","w")
            for element in nonduplicatenewmovielist:
                movielistfile.write(element)
                movielistfile.write('\n')
            movielistfile.close()

            listlength = str(len(nonduplicatenewmovielist))
            self.Movielistlength.setText('List Length:' + listlength)
            self.EnterMovieLineEdit.setText("")
            
            
        if sender.text() == 'Seen':
            if randommovie == " her":
                self.moviesuggestion.setText("Generate your random movie first!")

            else:
                d = datetime.datetime.today()
                datetimestring = d.strftime("%Y %m %d %H")
                self.moviestatus.setText(randommovie + " removed")
                movielist.remove(randommovie)
                
                with open("seenmovielist.txt", "a") as file_object:

                    file_object.write(datetimestring + " |" + randommovie )
                    file_object.write('\n')
                
                movielistfile = open("movieslist.txt","w")
                nonduplicatenewmovielist = list(dict.fromkeys(movielist))
                for element in nonduplicatenewmovielist:
                    movielistfile.write(element)
                    movielistfile.write('\n')
                movielistfile.close()


                randommovie = random.choice(movielist)
                self.moviesuggestion.setText(randommovie)

                listlength = str(len(nonduplicatenewmovielist))
                self.Movielistlength.setText('List Length:' + listlength)
            

        if sender.text() == 'Next Movie':
            with open('movieslist.txt') as file:
                movieliststring = file.read()
            movielist = movieliststring.splitlines()
            if len(movielist) == 0:
                self.moviesuggestion.setText("No more movies on your list!")
            else:
                randommovie = random.choice(movielist)

                self.moviesuggestion.setText(randommovie)
            

        

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())