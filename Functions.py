import tkinter
import tkinter.messagebox
import cv2
import requests
import subprocess
import time
import sys
import PIL
import random
import pygame
import calendar
import webbrowser
def A1():

    text = (
        '1. Features                                                                                         '
        "2. Calculator                                                                                      "
        '3. Say -                                                                                             '
        "4. Make a new file                                                                             "
        "5. Read a file                                                                                   "
        "6. Stop                                                                                                "
        "8. How are you                                                                               "
        "9. Open my camera                                                                          "
        "10. Calender                                                                                 "
        "11. Month lookup                                                                         "                                                     
        '12. Open Gmail                                                                            '
        '13. What is the weather                                                               '
        '14. What time is it                                                                        '
        '15. Where is -                                                                                  '
        '16. Search -                                                                                       '
        '17. Play Snake                                                                                '
        '18. Take a photo                                                                               '
        '19. Shutdown my computer   '
    )
    result = tkinter.messagebox.showinfo('Features', text)
def A3():
    def c():
        class Calculator:

            def __init__(self, master):

                '''
                DOCSTRING: Define what to do on initializationd
                '''

                # Assign reference to the main window of the application
                self.master = master

                # Add a name to our application
                master.title("Python Calculator")

                # Create a line where we display the equation
                self.equation = tkinter.Entry(master, width=36, borderwidth=5)

                # Assign a position for the equation line in the grey application window
                self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

                # Execute the .creteButton() method
                self.createButton()

            def createButton(self):

                '''
                DOCSTRING: Method that creates the buttons
                INPUT: nothing
                OUTPUT: creates a button
                '''

                # We first create each button one by one with the value we want
                # Using addButton() method which is described below
                b0 = self.addButton(0)
                b1 = self.addButton(1)
                b2 = self.addButton(2)
                b3 = self.addButton(3)
                b4 = self.addButton(4)
                b5 = self.addButton(5)
                b6 = self.addButton(6)
                b7 = self.addButton(7)
                b8 = self.addButton(8)
                b9 = self.addButton(9)
                b_add = self.addButton('+')
                b_sub = self.addButton('-')
                b_mult = self.addButton('*')
                b_div = self.addButton('/')
                b_clear = self.addButton('c')
                b_equal = self.addButton('=')

                # Arrange the buttons into lists which represent calculator rows
                row1 = [b7, b8, b9, b_add]
                row2 = [b4, b5, b6, b_sub]
                row3 = [b1, b2, b3, b_mult]
                row4 = [b_clear, b0, b_equal, b_div]

                # Assign each button to a particular location on the GUI
                r = 1
                for row in [row1, row2, row3, row4]:
                    c = 0
                    for buttn in row:
                        buttn.grid(row=r, column=c, columnspan=1)
                        c += 1
                    r += 1

            def addButton(self, value):

                '''
                DOCSTRING: Method to process the creation of a button and make it clickable
                INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
                OUTPUT: returns a designed button object
                '''
                return tkinter.Button(self.master, text=value, width=9, command=lambda: self.clickButton(str(value)))

            def clickButton(self, value):

                '''
                DOCSTRING: Method to program the actions that will happen in the calculator after a click of each button
                INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
                OUTPUT: what action will be performed when a particular button is clicked
                '''

                # Get the equation that's entered by the user
                current_equation = str(self.equation.get())

                # If user clicked "c", then clear the screen
                if value == 'c':
                    self.equation.delete(-1, END)

                # If user clicked "=", then compute the answer and display it
                elif value == '=':
                    answer = str(eval(current_equation))
                    self.equation.delete(-1, END)
                    self.equation.insert(0, answer)

                # If user clicked any other button, then add it to the equation line
                else:
                    self.equation.delete(0, END)
                    self.equation.insert(-1, current_equation + value)

        # Execution
        if __name__ == '__main__':
            # Create the main window of an application
            root = tkinter.Tk()

            # Tell our calculator class to use this window
            my_gui = Calculator(root)

            # Executable loop on the application, waits for user input
            root.mainloop()
    c()
def A6():

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Photo")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:

            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC presseduj8imn

            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)

            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()
    from PIL import Image

    # ...

    img = Image.open(img_name)
    img.show()
def A2(a):
    dataact = a.replace("Say", " ")
    tkinter.messagebox.showinfo("A'ight", dataact)

def A7():


    root = tkinter.Tk()
    root.title("New File")
    root.geometry("550x400")
    entry1 = tkinter.Entry(root)
    entry2 = tkinter.Entry(root)
    entry1.place(x=200,y=140)
    entry2.place(x=225,y=170)
    L = tkinter.Label(root, text="File name:")
    L1 = tkinter.Label(root, text="What do you wanna Write:")
    L.place(x=100, y=140)
    L1.place(x=100,y=170)

    def Write():
        a = entry1.get()
        ab = entry2.get()
        file = open(a + ".txt", "w")
        file.write(ab)
        file.close()

    Nmaer = tkinter.Button(root, text='Submit', command=Write)
    Nmaer.place(x=200,y=250)

    root.mainloop()


def A8():
    root = tkinter.Tk()
    root.title("Read a file")
    root.geometry("550x400")

    entry1 = tkinter.Entry(root)

    entry1.place(x=200,y=140)

    L = tkinter.Label(root, text="File name:")

    L.place(x=100,y=140)

    def type():
        x1 = entry1.get()
        c = open(x1, "r")
        label = tkinter.Label(root, text=c.read())
        label.pack()

    button1 = tkinter.Button(root, text='Submit', command=type)
    button1.place(x=200,y=200)

    root.mainloop()
def A9():

    sys.exit()
def A10():
    tkinter.messagebox.showinfo('Great!',"Thanks for asking!")

def A11():

    # define a video capture object

    vid = cv2.VideoCapture(0)

    while (True):

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Display the resulting frame)
        cv2.imshow('frame', frame)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
def A12():


    root = tkinter.Tk()
    root.title("Month Lookupper")
    root.geometry("550x400")
    entry1 = tkinter.Entry(root)
    entry2 = tkinter.Entry(root)
    entry1.place(x= 200 ,y= 140)
    entry2.place(x=200, y=170)
    ly = tkinter.Label(root, text="Year?")
    lm = tkinter.Label(root, text="Month?")
    ly.place(x=200, y=140)
    lm.place(x=200, y=170)

    def type():
        y = entry1.get()
        m = entry2.get()
        Month = tkinter.Label(root, text=calendar.month(int(y), int(m)))
        Month.place(x=200, y=300)

    button1 = tkinter.Button(root, text='Submit', command=type)
    button1.place(x=200, y=200)

    root.mainloop()
def A13():


    root = tkinter.Tk()
    root.title("Calender")
    root.geometry("550x400")

    entry1 = tkinter.Entry(root)

    entry1.place(x=200, y=140)

    ly = tkinter.Label(root, text="Year?")

    ly.place(x=100, y=140)

    def type():
        y = entry1.get()

        Month = tkinter.Label(root, text=calendar.calendar(int(y)))
        Month.place(x=200,y=250)

    button1 = tkinter.Button(root, text='Submit', command=type)
    button1.place(x=200, y=200)

    root.mainloop()
def A14():
    webbrowser.open_new_tab('https://www.gmail.com')
def A15():

    root = tkinter.Tk()
    c = tkinter.Canvas(root, width=1000, height=50)
    c.pack()
    # Enter your API key here
    api_key = "d79d8b56a560a9780a3774069683753f"
    # base_url variable to store ur
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    city_name = "Richmond, TX, US"

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values

        a = (" Temperature (in farhenhiet unit) = " + str(
            ((int(current_temperature) - 273.15) * 1.8) + 32) + " atmospheric pressure (in hPa unit) = " + str(
            current_pressure) + " humidity (in percentage) = " + str(current_humidiy) + " description = " + str(
            weather_description))

        l = tkinter.Label(root, text=a)
        c.create_window(500, 20, window=l)
    root.mainloop()
def A16():
    tkinter.messagebox.showinfo('Time','It is ' + time.ctime())
def A17(dataa):
    data1 = dataa.replace("Where is", "")
    location = data1

    tkinter.messagebox.showinfo('Looking',"I'ma seee where that is")

    webbrowser.open_new_tab('https://www.google.com/maps/place/' + location)
def A18(dataa1):
    data1 = dataa1.replace("Search", "")
    webbrowser.open('https://www.google.com/search?q=' + data1)
def A19():
    tkinter.messagebox.showinfo('Shutting Down',"Make sure anything thats open is saved")
    time.sleep(10)
    subprocess.call(["shutdown", "/l"])
def A20():
    import pygame
    import time
    import random

    pygame.init()

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 600
    dis_height = 400

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game by Me')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, yellow)
        dis.blit(value, [0, 0])

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(blue)
                message("You Lost! Press C-Play Again or Q-Quit", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    gameLoop()
