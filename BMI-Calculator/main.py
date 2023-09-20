import tkinter

def calculate():
    def check():
        if type(bmi) is int or type(bmi) is float:
            if bmi < 18.5:
                label3.config(text="Underweight")
            elif 18.5 <= bmi <= 24.9:
                label3.config(text="Normal range")
            elif 25 <= bmi < 30:
                label3.config(text="Overweight")
            else:
                label3.config(text="Obese")
    try:
        weight = float(entry.get().strip())
        height_cm = float(entry2.get().strip())  # Kullanıcıdan boyu santimetre cinsinden alın
        height = height_cm / 100  # Santimetre cinsinden alınan boyu metreye çevirin
        bmi = (weight / (height ** 2))
        print(bmi)
        result = f"{bmi:.2f}"
        check()
    except:
        label3.config(text="Sadece sayı giriniz.")


window = tkinter.Tk()
window.geometry("200x100")

label = tkinter.Label(text="Kilonuz : ")
label.grid(row=0, column=0)

entry = tkinter.Entry()
entry.grid(row=0, column=1)

label2 = tkinter.Label(text="Boyunuz : ")
label2.grid(row=1, column=0)

entry2 = tkinter.Entry()
entry2.grid(row=1, column=1)

label3 = tkinter.Label(text="Sonuç : ")
label3.grid(row=3)


button = tkinter.Button(text="Hesapla", command=calculate)
button.grid(row=2)

window.mainloop()