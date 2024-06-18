from tkinter import *
import math
from Plotter import plot_function
from Derivative import calculate_derivative
from Indefinite_Integration import calculate_indefinite_integral
from Differential_Equations import solve_differential_equation
from Polar import plot_polar
from Polynomial_Graph import plot_polynomial
from n_Derivative import plot_nth_derivative
from CommonPointArea import plot_common_points
from Definite_Integration import calculate_definite_integral
from ThreeD import plot_3d


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)


    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, str(value))  # Ensure value is a string
        root.update()  # Force the GUI to refresh

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "raise":
            self.total = self.total ** self.current
        if self.op == "rootof":
            self.total = self.total ** (1/self.current)
        if self.op == "fact":
            self.total=int(text_box.get())
            self.total=math.factorial(self.total)
        if self.op == "ln":
            self.total = math.log(self.total)
        if self.op == "log":
            self.total= math.log(self.total,10)
        if self.op == "sine":
            self.total=math.sin(self.total)
        if self.op == "cosine":
            self.total = math.cos(self.total)
        if self.op == "tangent":
            self.total = math.tan(self.total)
        if self.op == "exp":
            self.total = math.exp(self.total)
        if self.op == "inv":
            self.total = 1/self.total
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
text_box = Entry(calc, width=35, borderwidth=5)
text_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
text_box.insert(0, "0")
#text_box.focus()

numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
        bttn[i]["bg"]= "orange"
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "0",bg="orange")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)

div = Button(calc,height =2,width=4,padx=10, pady = 10, text = "/",bg="steel blue")
div["command"] = lambda: sum1.operation("divide")
div.grid(row = 1, column = 3, padx=1, pady = 1)

mult = Button(calc,height =2,width=4,padx=10, pady = 10, text = "*",bg="steel blue")
mult["command"] = lambda: sum1.operation("times")
mult.grid(row = 2, column = 3,  padx=1, pady = 1)

minus = Button(calc,height =2,width=4,padx=10, pady = 10, text = "-",bg="steel blue")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, padx=1, pady = 1)

add = Button(calc,height =2,width=4,padx=10, pady = 10, text = "+",bg="steel blue")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3,  padx=1, pady = 1)

power = Button(calc, height=2,width=4,padx=10,pady=10,text="x^y",bg="green")
power["command"] = lambda: sum1.operation("raise")
power.grid(row=2,column = 4,padx=1,pady=1)

rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="y-\/x", bg = "green")
rootof["command"] = lambda: sum1.operation("rootof")
rootof.grid(row=2, column=5, padx=1, pady=1)

fact = Button(calc, height=2, width=4, padx=10, pady=10, text="!",bg="green")
fact["command"] = lambda: sum1.operation("fact")
fact.grid(row=3,column=4, padx=1, pady=1)

loge = Button(calc, height=2, width=4, padx=10, pady=10, text="ln",bg="green")
loge["command"] = lambda: sum1.operation("ln")
loge.grid(row=3, column=5, padx=1, pady=1)

log10 = Button(calc, height=2, width=4, padx=10, pady=10, text="log",bg="green")
log10["command"]= lambda: sum1.operation("log")
log10.grid(row=4, column=4, padx=1 , pady=1)

sine = Button(calc, height=2,width=4, padx=10,pady=10, text = "sin" , bg= "green")
sine["command"]=lambda: sum1.operation("sine")
sine.grid(row=2, column=0)

cosine = Button(calc, height=2,width=4, padx=10,pady=10, text = "cos" , bg= "green")
cosine["command"]=lambda: sum1.operation("cosine")
cosine.grid(row=2, column=1)

tangent = Button(calc, height=2,width=4, padx=10,pady=10, text = "tan" , bg= "green")
tangent["command"]=lambda: sum1.operation("tangent")
tangent.grid(row=2, column=2)

trig_frame = Frame(calc, borderwidth=2, relief="ridge")
trig_frame.grid(row=2, column=0, columnspan=4, sticky="ew")

sine_button = Button(trig_frame, text='sin', command=lambda: sum1.operation("sine"))
cosine_button = Button(trig_frame, text='cos', command=lambda: sum1.operation("cosine"))
tangent_button = Button(trig_frame, text='tan', command=lambda: sum1.operation("tangent"))

sine_button.pack(side=LEFT)
cosine_button.pack(side=LEFT)
tangent_button.pack(side=LEFT)

inv = Button(calc, height=2, width=4, padx=10, pady=10, text="1/x", bg="green")
inv["command"] = lambda: sum1.operation("inv")
inv.grid(row=2, column=3)

exponent = Button(calc, height=2, width=4, padx=10, pady=10, text='e^x', bg="green")
exponent["command"]=lambda: sum1.operation("exp")
exponent.grid(row=5, column=3)

point = Button(calc,height =2,width=4,padx=10, pady = 10, text = ".",bg="white")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 1, padx=1, pady = 1)

neg= Button(calc,height =2,width=4,padx=10, pady = 10, text = "+/-",bg="white")
neg["command"] = sum1.sign
neg.grid(row = 4, column = 2,  padx=1, pady = 1)


clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "C",bg="white")
clear["command"] = sum1.clear
clear.grid(row = 1, column = 4,  padx=1, pady = 1)

all_clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "AC",bg="white")
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 1, column = 5, padx=1, pady=1)

equals = Button(calc,height =6,width=4,padx=10, pady = 10, text = "=",bg="green")
equals["command"] = sum1.calc_total
equals.grid(row = 4, column = 5,columnspan=1,rowspan=2,padx=1, pady = 1)

plot_button = Button(calc, height=2, width=4, padx=10, pady=10, text='Plot', bg="blue")
plot_button["command"] = lambda: plot_function(text_box.get())
plot_button.grid(row=5, column=0, padx=1, pady=1)

derivative_button = Button(calc, height=2, width=4, padx=10, pady=10, text='Deriv', bg="blue")
derivative_button["command"] = lambda: calculate_derivative(text_box.get())
derivative_button.grid(row=4, column=0, padx=1, pady=1)

integral_button = Button(calc, height=2, width=4, padx=10, pady=10, text='Integrate', bg="blue")
integral_button["command"] = lambda: calculate_indefinite_integral(text_box.get())
integral_button.grid(row=4, column=1, padx=1, pady=1)

diff_eq_button = Button(calc, height=2, width=4, padx=10, pady=10, text='Diff Eq', bg="blue")
diff_eq_button["command"] = lambda: solve_differential_equation(text_box.get(), "initial_condition_placeholder", "time_points_placeholder")
diff_eq_button.grid(row=7, column=0, padx=1, pady=1)

polar_button = Button(calc, height=2, width=4, padx=10, pady=10, text='Polar', bg="blue")
polar_button["command"] = lambda: plot_polar(text_box.get())
polar_button.grid(row=5, column=2, padx=1, pady=1)

polynomial_button = Button(calc, height=2, width=4, padx=10, pady=10, text='Poly', bg="blue")
polynomial_button["command"] = lambda: plot_polynomial(text_box.get())
polynomial_button.grid(row=7, column=2, padx=1, pady=1)

nth_derivative_button = Button(calc, height=2, width=4, padx=10, pady=10, text='Nth Deriv', bg="blue")
nth_derivative_button["command"] = lambda n=n: plot_nth_derivative(text_box.get(), n)
nth_derivative_button.grid(row=4, column=2, padx=1, pady=1)

# Assuming text_box1 and text_box2 are Text widgets for inputting functions to find intersections
text_box1 = Text(calc, height=2, width=10)
text_box1.grid(row=5, column=1, padx=1, pady=1)
text_box2 = Text(calc, height=2, width=10)
text_box2.grid(row=5, column=2, padx=1, pady=1)

common_points_button = Button(calc, height=2, width=4, padx=10, pady=10, text='Intersect', bg="blue")
common_points_button["command"] = lambda: plot_common_points(text_box1.get("1.0", "end-1c"), text_box2.get("1.0", "end-1c"))
common_points_button.grid(row=5, column=3, padx=1, pady=1)

# Assuming text_box_expression, text_box_lower_bound, and text_box_upper_bound are Text widgets for inputting the expression and bounds for definite integration
text_box_expression = Text(calc, height=2, width=10)
text_box_expression.grid(row=4, column=1, padx=1, pady=1)
text_box_lower_bound = Text(calc, height=2, width=10)
text_box_lower_bound.grid(row=4, column=2, padx=1, pady=1)
text_box_upper_bound = Text(calc, height=2, width=10)
text_box_upper_bound.grid(row=4, column=3, padx=1, pady=1)

def_int_button = Button(calc, height=2, width=4, padx=10, pady=10, text='Def Int', bg="blue")
def_int_button["command"] = lambda: calculate_definite_integral(text_box_expression.get("1.0", "end-1c"), text_box_lower_bound.get("1.0", "end-1c"), text_box_upper_bound.get("1.0", "end-1c"))
def_int_button.grid(row=4, column=4, padx=1, pady=1)
def_int_button.grid(row=4, column=3, padx=1, pady=1)

plot_3d_button = Button(calc, height=2, width=4, padx=10, pady=10, text='3D Plot', bg="blue")
plot_3d_button["command"] = lambda: plot_3d(text_box.get())
plot_3d_button.grid(row=5, column=1, padx=1, pady=1)

# Additional buttons for basic operations
add_button = Button(calc, text='+', padx=20, pady=20, command=lambda: sum1.operation("add"))
add_button.grid(row=3, column=0)

subtract_button = Button(calc, text='-', padx=22, pady=20, command=lambda: sum1.operation("subtract"))
subtract_button.grid(row=3, column=1)

multiply_button = Button(calc, text='*', padx=21, pady=20, command=lambda: sum1.operation("times"))
multiply_button.grid(row=3, column=2)

divide_button = Button(calc, text='/', padx=22, pady=20, command=lambda: sum1.operation("divide"))
divide_button.grid(row=3, column=3)

root.mainloop()
