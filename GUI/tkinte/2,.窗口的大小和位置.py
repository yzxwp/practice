from tkinter import *
from tkinter import messagebox


#   居中显示方法
def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    root.geometry(size)
    root.update()
    print(root.winfo_x())
    
root = Tk()
root.title('第一个开发工具')

# 第一个是指窗口的宽度，第二个窗口的高度，第三个窗口左上点离左屏幕边界距离，第四个窗口左上点离上面屏幕边界距离
# root.geometry("1000x700+500+300")
center_window(root, 1000, 700)
btn01 = Button(root)
btn01["text"] = "获得一个身份证号码"
btn01.pack()


def way():
    return '1221211212'


def get_car(e):
    messagebox.showinfo("身份证号码", way())
    print("1111")


# 调用组件的mainloop()方法，进入事件循环
btn01.bind("<Button-1>", get_car)
root.mainloop()
