import controllers
import views
import models

def main():
    controllers.controller(views.StandardView(), models.StandardModel())

if __name__ == "__main__":
    main()