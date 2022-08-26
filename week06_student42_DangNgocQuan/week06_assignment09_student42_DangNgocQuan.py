import os
import math
import random
from turtle import width
from manim import *

class AnalogClockImage(Scene):
    def construct(self):
        radius = 3
        circle = Circle(radius, color=WHITE)
        centerDot = Dot([0, 0, 0], color=WHITE)
        clock = Group(circle, centerDot)

        marks = []
        for i in range(60):
            alpha = math.pi/2 - math.pi*2 * i/60
            if i % 5 == 0:
                startDot = [0.85 * radius * math.cos(alpha), 0.85 * radius * math.sin(alpha), 0]
                endDot = [0.95 * radius * math.cos(alpha), 0.95 * radius * math.sin(alpha), 0]
                line = Line(startDot, endDot, buff=0, color=GREEN)
                marks.append(line)
            else:
                startDot = [0.9 * radius * math.cos(alpha), 0.9 * radius * math.sin(alpha), 0]
                endDot = [0.95 * radius * math.cos(alpha), 0.95 * radius * math.sin(alpha), 0]
                line = Line(startDot, endDot, buff=0, color=GREEN)
                marks.append(line)
        for mark in marks:
            clock.add(mark)
        
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        clock.add(Text(f"{hour:0>2}h{minute:0>2}m{second:0>2}s", font_size=32, color=RED).next_to(circle, DOWN))
        
        hourDot = ((hour%12) + minute/60 + second/3600)*5 * math.pi * 2 / 60
        minuteDot = (minute + second/60) * math.pi * 2 / 60
        secondDot = second * math.pi * 2 / 60
        
        hourDot = [0.5 * radius * math.cos(math.pi/2 - hourDot), 0.5 * radius * math.sin(math.pi/2 - hourDot), 0]
        minuteDot = [0.65 * radius * math.cos(math.pi/2 - minuteDot), 0.65 * radius * math.sin(math.pi/2 - minuteDot), 0]
        secondDot = [0.8 * radius * math.cos(math.pi/2 - secondDot), 0.8 * radius * math.sin(math.pi/2 - secondDot), 0]
        
        hourLine = Line(ORIGIN, hourDot, buff=0, stroke_width=3, color=RED)
        minuteLine = Line(ORIGIN, minuteDot, buff=0, stroke_width=3, color=BLUE)
        secondLine = Line(ORIGIN, secondDot, buff=0, stroke_width=3, color=GRAY)
        clock.add(hourLine, minuteLine, secondLine)
        
        self.add(clock)     
'''
Chạy lệnh ở command line
manim week06_assignment09_student42_DangNgocQuan.py AnalogClockImage -p -ql --media_dir "./additionalFolder/assignment09/output" 
Kết quả được lưu ở:
./additionalFolder/assignment09/output/images/week06_assignment09_student42_DangNgocQuan/
'''

class DigitalClockImage(Scene):
    def construct(self):
        height = 3
        width = 12
        rectangle1 = Rectangle(WHITE, height, width, stroke_width=3)
        rectangle2 = Rectangle(WHITE, height-0.16, width-0.16, stroke_width=3)
        clock = Group(rectangle1, rectangle2)
        
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        
        timeText = Text(f"{hour:0>2}:{minute:0>2}:{second:0>2}",font="times",
                        height=height*0.6, color=WHITE).next_to([0, height/2, 0], DOWN, buff=0.2*height)
        clock.add(timeText)
        self.add(clock)
        
'''
Chạy lệnh ở command line
manim week06_assignment09_student42_DangNgocQuan.py DigitalClockImage -p -ql --media_dir "./additionalFolder/assignment09/output" 
Kết quả được lưu ở:
./additionalFolder/assignment09/output/images/week06_assignment09_student42_DangNgocQuan/
'''

class AnalogClockVideo(Scene):
    def construct(self):
        radius = 3
        circle = Circle(radius, color=WHITE)
        centerDot = Dot([0, 0, 0], color=WHITE)
        clock = Group(circle, centerDot)
        self.wait(1)
        self.play(GrowFromCenter(clock))
        self.wait(1)
        
        marks = []
        for i in range(60):
            alpha = math.pi/2 - math.pi*2 * i/60
            if i % 5 == 0:
                startDot = [0.85 * radius * math.cos(alpha), 0.85 * radius * math.sin(alpha), 0]
                endDot = [0.95 * radius * math.cos(alpha), 0.95 * radius * math.sin(alpha), 0]
                line = Line(startDot, endDot, buff=0, color=GREEN)
                marks.append(line)
            else:
                startDot = [0.9 * radius * math.cos(alpha), 0.9 * radius * math.sin(alpha), 0]
                endDot = [0.95 * radius * math.cos(alpha), 0.95 * radius * math.sin(alpha), 0]
                line = Line(startDot, endDot, buff=0, color=GREEN)
                marks.append(line)
        for mark in marks:
            self.play(Animation(mark), run_time = 1/60)
        
        hourLine = Line(ORIGIN, [0, radius*0.7, 0], buff=0, color=RED, stroke_width=3)
        minuteLine = Line(ORIGIN, [0, radius*0.8, 0], buff=0, color=BLUE, stroke_width=3)
        secondLine = Line(ORIGIN, [0, radius*0.95, 0], buff=0, color=GRAY, stroke_width=3)
        for totalSecond in range(3600):
            self.play(Rotate(secondLine, -6*DEGREES, about_point=[0, 0, 0],run_time=1),
                      Rotate(minuteLine, -0.1*DEGREES, about_point=[0, 0, 0],run_time=1),
                      Rotate(hourLine, -(0.1/12)*DEGREES, about_point=[0, 0, 0],run_time=1))
        self.wait(1)   
'''
Chạy lệnh ở command line
manim week06_assignment09_student42_DangNgocQuan.py AnalogClockVideo -p -ql --media_dir "./additionalFolder/assignment09/output" 
Kết quả được lưu ở:
./additionalFolder/assignment09/output/videos/week06_assignment09_student42_DangNgocQuan/
'''


class DigitalClockVideo(Scene):
    def construct(self):
        height = 3
        width = 12
        rectangle1 = Rectangle(WHITE, height, width, stroke_width=3)
        rectangle2 = Rectangle(WHITE, height-0.16, width-0.16, stroke_width=3)
        clock = Group(rectangle1, rectangle2)
        self.wait(1)
        self.play(Animation(clock, runtime=1))
        self.wait(1)
        
        hour = 0
        minute = 0
        second = 0
        timeText = None
        for totalSecond in range(3600):
            second += 1
            if second >= 60:
                second = 0
                minute += 1
                if minute >= 60:
                    minute = 0
                    hour += 1
                    hour %= 24
            timeText = Text(f"{hour:0>2}:{minute:0>2}:{second:0>2}",font="times",
                        height=height*0.6, color=WHITE).next_to([0, height/2, 0], DOWN, buff=0.2*height)
            self.play(Animation(timeText, run_time=1, remover=True))
        self.wait(1)
        
'''
Chạy lệnh ở command line
manim week06_assignment09_student42_DangNgocQuan.py DigitalClockVideo -p -ql --media_dir "./additionalFolder/assignment09/output" 
Kết quả được lưu ở:
./additionalFolder/assignment09/output/videos/week06_assignment09_student42_DangNgocQuan/
'''