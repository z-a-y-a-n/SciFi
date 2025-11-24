import sys
import numpy as np
from sympy import symbols, sympify, diff, integrate, lambdify, pi, E, N, latex
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class PlotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plotter")
        self.resize(1000, 700)
        fig = Figure(facecolor="#0f0f0f")
        self.canvas = FigureCanvasQTAgg(fig)
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)
        self.ax = fig.add_subplot(111)
        self.ax.set_facecolor("#1e1e1e")
        self.ax.grid(True, alpha=0.3)
        for spine in self.ax.spines.values():
            spine.set_color("white")
        self.ax.tick_params(colors="white")

    def plot(self, expr):
        try:
            x = symbols('x')
            f = lambdify(x, sympify(expr, locals={'pi':pi, 'e':E}), 'numpy')
            xs = np.linspace(-10, 10, 1000)
            ys = np.real(f(xs)) if np.iscomplexobj(f(xs)) else f(xs)
            self.ax.clear()
            self.ax.plot(xs, ys, color="#00ff99", linewidth=3)
            self.ax.set_title(f"y = {latex(sympify(expr))}", color="white", fontsize=16)
            self.canvas.draw()
            self.show()
        except Exception as e:
            QMessageBox.critical(self, "Plot Error", str(e))


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pro Scientific Calculator")
        self.resize(1000, 700)
        self.x = symbols('x')

        central = QWidget()
        self.setCentralWidget(central)
        main = QHBoxLayout(central)
        main.setContentsMargins(15, 15, 15, 15)
        main.setSpacing(16)

        # LEFT — Calculator
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setSpacing(12)

        # Display
        self.display = QLineEdit()
        self.display.setFixedHeight(80)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont("Jetbrains Mono", 32, QFont.Bold))
        self.display.setStyleSheet("""
            background:#1e1e1e; color:#00ff99; border:3px solid #333;
            border-radius:16px; padding:0 16px; font-weight:bold;
        """)
        self.display.setPlaceholderText("expression goes here")
        left_layout.addWidget(self.display)

        # Grid
        grid = QGridLayout()
        grid.setSpacing(10)

        BTN_SIZE = 70

        buttons = [
            ("C",0,0,"#e74c3c"), ("<-",0,1,"#f39c12"), ("Plot",0,2,"#9b59b6"), ("÷",0,3,"#34495e"),
            ("sin",1,0,"#2c3e50"), ("cos",1,1,"#2c3e50"), ("tan",1,2,"#2c3e50"), ("×",1,3,"#34495e"),
            ("7",2,0,"#2c3e50"), ("8",2,1,"#2c3e50"), ("9",2,2,"#2c3e50"), ("-",2,3,"#34495e"),
            ("4",3,0,"#2c3e50"), ("5",3,1,"#2c3e50"), ("6",3,2,"#2c3e50"), ("+",3,3,"#34495e"),
            ("1",4,0,"#2c3e50"), ("2",4,1,"#2c3e50"), ("3",4,2,"#2c3e50"), ("^",4,3,"#34495e"),
            ("0",5,0,"#2c3e50"), (".",5,1,"#2c3e50"), ("(",5,2,"#34495e"), (")",5,3,"#34495e"),
            ("=",6,0,4,"#27ae60"),
        ]

        for btn in buttons:
            text = btn[0]
            b = QPushButton(text)
            if len(btn) == 5:  # equals
                b.setFixedSize(BTN_SIZE * 4, BTN_SIZE)
                grid.addWidget(b, btn[1], btn[2], 1, btn[3])
                b.clicked.connect(self.evaluate)
            else:
                b.setFixedSize(BTN_SIZE, BTN_SIZE)
                grid.addWidget(b, btn[1], btn[2])
                b.clicked.connect(lambda _, t=text: self.on_btn(t))

            b.setStyleSheet(f"""
                QPushButton {{ background:{btn[-1]}; color:white; font-weight:bold;
                              border-radius:14px; font-size:18px; }}
                QPushButton:hover {{ background:{self.lighten(btn[-1])} }}
            """)

        left_layout.addLayout(grid)
        left_layout.addStretch(1)
        main.addWidget(left, stretch=3)

        # RIGHT — Super Clean Panel (No History!)
        right = QWidget()
        r = QVBoxLayout(right)
        r.setSpacing(6)

        r.addWidget(QLabel("<b>Functions</b>"))
        funcs = ["sin(x)","cos(x)","tan(x)","asin(x)","acos(x)","atan(x)",
                 "ln(x)","log10(x)","√x","x²","x³","e^x","π","e","abs(x)"]
        ins = ["sin","cos","tan","asin","acos","atan","ln","log","sqrt","**2","**3","exp","pi","E","abs"]
        for label, txt in zip(funcs, ins):
            b = QPushButton(label)
            b.setFixedHeight(44)
            b.setStyleSheet("background:#263238; color:#00ff99; border-radius:10px; font-size:13px;")
            b.clicked.connect(lambda _, x=txt: self.display.insert(x))
            r.addWidget(b)

        r.addWidget(QLabel("<b>Calculus</b>"))
        calc = QHBoxLayout()
        diff = QPushButton("d/dx")
        integ = QPushButton("∫ dx")
        for btn in (diff, integ):
            btn.setFixedHeight(50)
            btn.setStyleSheet("color:white; font-weight:bold; border-radius:12px; font-size:14px;")
        diff.setStyleSheet(diff.styleSheet() + "background:#9c27b0;")
        integ.setStyleSheet(integ.styleSheet() + "background:#3498db;")
        diff.clicked.connect(self.differentiate)
        integ.clicked.connect(self.integrate)
        calc.addWidget(diff)
        calc.addWidget(integ)
        r.addLayout(calc)

        main.addWidget(right, 1)

        self.plot_win = PlotWindow()
        self.setStyleSheet("QMainWindow{background:#121212} QLabel{color:#00ff99; font-weight:bold;}")

    def lighten(self, c):
        v = int(c[1:], 16)
        return f"#{min(0xffffff, v + 0x333333):06x}"

    def on_btn(self, t):
        m = {"÷":"/", "×":"*", "^":"**", "<-":"<-", "C":"C", "Plot":"Plot"}
        a = m.get(t, t)
        if a == "C": self.display.clear()
        elif a == "<-": self.display.setText(self.display.text()[:-1])
        elif a == "Plot": self.plot_win.plot(self.display.text())
        else: self.display.insert(a)

    def evaluate(self):
        e = self.display.text().strip()
        if not e: return
        try:
            res = sympify(e, locals={'pi':pi, 'e':E})
            out = str(res) if res.free_symbols else str(N(res, 15))
            out = out.rstrip("0").rstrip(".") if "." in out and not res.free_symbols else out
            self.display.setText(out)
        except Exception as ex:
            QMessageBox.critical(self, "Error", str(ex))

    def differentiate(self):
        e = self.display.text().strip()
        if e:
            try: self.display.setText(str(diff(sympify(e), self.x)))
            except Exception as ex: QMessageBox.critical(self, "Error", str(ex))

    def integrate(self):
        e = self.display.text().strip()
        if e:
            try: self.display.setText(str(integrate(sympify(e), self.x)))
            except Exception as ex: QMessageBox.critical(self, "Error", str(ex))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = Calculator()
    w.show()
    sys.exit(app.exec())