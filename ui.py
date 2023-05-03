from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Brain")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.texto_puntos = Label(text=f"Puntos: {self.quiz.score}", font=("Arial", 20), fg="white", bg=THEME_COLOR)
        self.texto_puntos.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)  # Aca cambia el color
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some question text",
                                                     width=280,
                                                     font=("Arial", 15, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # pady añade distancia en el lienzo eje Y

        imagen_verdadera = PhotoImage(file="images/true.png")  # No se le da self porque no lo necesito en ningun otro lado
        self.true_boton = Button(image=imagen_verdadera, highlightthickness=0, command=self.boton_correcto)
        self.true_boton.grid(row=2, column=0)

        imagen_falsa = PhotoImage(file="images/false.png")  # No se le da self porque no lo necesito en ningun otro lado
        self.false_boton = Button(image=imagen_falsa, highlightthickness=0, command=self.boton_incorrecto)
        self.false_boton.grid(row=2, column=1)

        self.get_next_question()
        self.quiz.still_has_questions()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # Siempre vuelve a cambiar a blanco el programa despues de la respuesta
        if self.quiz.still_has_questions():
            self.texto_puntos.config(text=f"Puntos: {self.quiz.score}")  # Refresca la puntuacion
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Has llegado al final del juego")
            self.true_boton.config(state="disabled")
            self.false_boton.config(state="disabled")


    def cambio_de_color(self, valor):
        if valor:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)  # Despues de un cierto tiempo cambia a la funcion siguiente preg

    def boton_correcto(self):
        self.cambio_de_color(self.quiz.check_answer("True"))

    def boton_incorrecto(self):
        self.cambio_de_color(self.quiz.check_answer("False"))
