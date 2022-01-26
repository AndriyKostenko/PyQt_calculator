import sys
from PyQt5.QtWidgets import QApplication
from app.calculator_view_2_22_1 import CalcView
from app.calculator_controller_2_22_1 import CalcController
from app.calculator_model_2_22_1 import CalcModel


def main():
    app = QApplication(sys.argv)

    view = CalcView()
    model = CalcModel()
    CalcController(view=view, model=model)


    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
