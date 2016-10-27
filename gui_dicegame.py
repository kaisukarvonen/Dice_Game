from tkinter import *
from tkinter import messagebox
import random


class DiceGame:
    youTotal = 0
    youCurrentSum = 0
    cpuTotal = 0
    cpuCurrentSum = 0

    def __init__(self, master):
        self.master = master
        master.title(" Kaisu's Dice Game")
        self.title = Label(master, text="Kaisu's Dice Game")
        self.title.grid(row=0, columnspan=2)
        self.title.config(font=('Calibri', 19))
        self.info = Label(master,
                              text="\nRoll the dice to get to 100 points before the evil computer does!\n"
                                   "You can roll the dice as many times as you want during your turn but you'll lose all your points for the round if you roll a 1!\n"
                                   "So think carefully and have fun!\n", justify=LEFT, pady=10, width=60, wraplength=400)
        self.info.grid(row=1, columnspan=2)
        self.info.config(font=('Calibri', 12))
        self.start = Button(master, text='START', command=self.startGame, width=30, height=1, font=('Calibri', 15), bg='#4080bf', activebackground="#4080bf")
        self.start.grid(row=2, columnspan=2)

        self.whosturn = Label(master, text="Now playing:", font=('Calibri', 14))
        self.whosturn.grid(row=3, columnspan=2, pady=(35,0))
        self.cpuOryou = Label(master, text="(Game hasn't started yet)")
        self.cpuOryou.grid(row=4, columnspan=2, pady=(0,29))
        self.cpuOryou.config(font=('Calibri', 20), fg='#cc0000')

        self.dicenumberText = Label(master, text="Dice Number")
        self.dicenumberText.grid(row=5, column=0)
        self.dicenumberText.config(font=('Calibri', 18))

        self.dicenumber = Label(master, text="0")
        self.dicenumber.grid(row=6, column=0)
        self.dicenumber.config(font=('Calibri', 40))

        self.roll = Button(master, text="ROLL", state=DISABLED, command=self.rollDice, width=8, height=2, bg='#aaa', activebackground = '#aaa', font=('Calibri', 14))
        self.roll.grid(row=5, column=1, pady=(46,0))
        self.done = Button(master, text="DONE", state=DISABLED, command=self.cpuTurn, width=8, height=2, bg='#aaa', activebackground = '#aaa', font=('Calibri', 14))
        self.done.grid(row=6, column=1)

        self.currentText = Label(master, text="", font=('Calibri', 15))
        self.currentText.grid(row=8, columnspan=2, pady=(12,25))
        self.currentSum = Label(master, text="", font=('Calibri', 15))
        self.currentSum.grid(row=8, columnspan=2, pady=(12,25))

        self.totalText = Label(master, text="TOTAL SCORES")
        self.totalText.grid(row=9, columnspan=2, pady=(28,15))
        self.totalText.config(font=('Calibri', 17), fg='#cc0000')

        self.youtotalText = Label(master, text="YOU:", font=('Calibri', 16))
        self.youtotalText.grid(row=10, column=0)
        self.youtotalScore = Label(master, text="0", font=('Calibri', 16))
        self.youtotalScore.grid(row=11, column=0, pady=(10,55))

        self.cputotalText = Label(master, text="CPU:", font=('Calibri', 16))
        self.cputotalText.grid(row=10, column=1)
        self.cputotalScore = Label(master, text="0", font=('Calibri', 16))
        self.cputotalScore.grid(row=11, column=1, pady=(10,55))



    def startGame(self):
        self.roll.config(state='active', bg = '#00b300', activebackground = '#00b300')
        self.done.config(state='active', bg='#cc0000', activebackground='#cc0000')
        self.cpuOryou.config(text="YOU")
        self.dicenumber.config(text="0")
        self.youTotal = 0
        self.youCurrentSum = 0
        self.cpuTotal = 0
        self.cpuCurrentSum = 0
        self.currentText.config(text="Your current sum:                                    ")
        self.currentSum.config(text=self.youCurrentSum)
        self.youtotalScore.config(text=self.youTotal)
        self.cputotalScore.config(text=self.cpuTotal)



    def rollDice(self):

        number = random.randint(1, 6)
        self.dicenumber.config(text=number)

        if number == 1:
            messagebox.showinfo("Oopsis", "Oops, you rolled a 1! Lost your points for this round!")
            self.youTotal -= self.youCurrentSum
            self.youtotalScore.config(text=self.youTotal)
            self.currentSum.config(text="0")
            self.dicenumber.config(text="0")
            self.roll.config(state='disabled', bg='#aaa')
        else:
            self.youCurrentSum += number
            self.youTotal += number
            self.youtotalScore.config(text=self.youTotal)
            self.currentSum.config(text=self.youCurrentSum)
            if self.youTotal >= 100:
                messagebox.showinfo("Game over", "Congratulations! You have reached 100 points and won the game!")
                self.startGame()


        self.cpuCurrentSum = 0



    def cpuTurn(self):
        self.roll.config(state='disabled', bg='#aaa')
        self.done.config(text="DONE", state='disabled', bg='#aaa')
        self.cpuOryou.config(text="CPU")
        self.dicenumber.config(text="0")

        self.cpuRolls()



    def cpuRolls(self):
        self.currentText.config(text="CPU's current sum:                                    ")
        number = random.randint(1, 6)

        if self.cpuCurrentSum >= 10:
            if self.cpuTotal >= 100:
                messagebox.showinfo("Game over", "Cpu has reached 100 points and won the game!")
                self.startGame()
            elif self.cpuTotal <= self.youTotal - 5:
                self.caseCpuIsLosing()
                return
            else:
                self.currentSum.config(text=self.cpuCurrentSum)
                self.cputotalScore.config(text=self.cpuTotal)
                messagebox.showinfo("CPU wants to say something", "Cpu has ended his round, now it's your turn!")
                self.nollaa()
        elif 1 == number:
            self.dicenumber.config(text=number)
            self.cpuTotal-= self.cpuCurrentSum
            self.currentSum.config(text=self.cpuCurrentSum)
            messagebox.showinfo("CPU rolled 1", "Cpu has ended his round, now it's your turn!")
            self.cputotalScore.config(text=self.cpuTotal)
            self.nollaa()
        elif self.cpuTotal >= 100:
            messagebox.showinfo("Game over", "Cpu has reached 100 points and won the game!")
            self.startGame()

        else:
            self.dicenumber.config(text=number)
            self.cpuCurrentSum += number
            self.cpuTotal += number
            self.currentSum.config(text=self.cpuCurrentSum)
            self.cputotalScore.config(text=self.cpuTotal)
            self.master.after(900, self.cpuRolls)


    def caseCpuIsLosing(self):

        number = random.randint(1, 6)


        if self.cpuCurrentSum >= 15:
            if self.cpuTotal >= 100:
                messagebox.showinfo("Game over", "Cpu has reached 100 points and won the game!")
                self.startGame()
                return
            else:
                self.currentSum.config(text=self.cpuCurrentSum)
                self.cputotalScore.config(text=self.cpuTotal)
                messagebox.showinfo("CPU wants to say something", "Cpu has ended his round, now it's your turn!")
                self.nollaa()
                return
        elif number == 1:
            self.dicenumber.config(text=number)
            self.cpuTotal -= self.cpuCurrentSum
            self.currentSum.config(text=self.cpuCurrentSum)
            self.cputotalScore.config(text=self.cpuTotal)
            messagebox.showinfo("CPU rolled 1", "Cpu has ended his round, now it's your turn!")
            self.nollaa()
            return
        elif self.cpuTotal >= 100:
            messagebox.showinfo("Game over", "Cpu has reached 100 points and won the game!")
            return
        else:
            self.dicenumber.config(text=number)
            self.cpuCurrentSum += number
            self.cpuTotal += number
            self.currentSum.config(text=self.cpuCurrentSum)
            self.cputotalScore.config(text=self.cpuTotal)
            self.master.after(900, self.cpuRolls)


    def nollaa(self):
        self.roll.config(state='active', bg = '#00b300', activebackground = '#00b300')
        self.done.config(state='active', bg='#cc0000', activebackground='#cc0000')
        self.cpuOryou.config(text="YOU")
        self.youCurrentSum = 0
        self.currentSum.config(text=self.youCurrentSum)
        self.currentText.config(text="Your current sum:                                    ")
        self.dicenumber.config(text="0")







def main():
    root = Tk()
    game = DiceGame(root)
    root.mainloop()


if __name__ == "__main__": main()
