import matplotlib.pyplot as plt
def display_line (x, y):
    plt.plot(x,y, marker="o",linestyle="-",color="blue")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()

def run_task1():
    x_values = [1,2,3,4,5]
    y_values = [1,4,9,16,25]

    display_line(x_values,y_values)

if __name__ == "__main__":
    run_task1()
# import matplotlib.pyplot as plt
#
# def coordinate():
#     x = float(input("enter an x value: " ))
#     y = float(input("engter an y "))
