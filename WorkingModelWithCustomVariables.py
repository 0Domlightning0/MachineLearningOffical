import tensorflow as tf

#py -m pip install tensorflow

import numpy as np
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)



EnrolledStudents    = np.array([675, 225, 150, 165, 220, 275, 295, 255, 215, 190, 225, 140, 235, 305, 275, 210, 275, 230, 410, 325, 125, 210, 270, 235, 405, 165, 255, 530, 125, 215, 350, 420, 320, 630, 240, 135, 355, 
225, 245, 180, 260, 185, 345, 320, 255, 355, 280, 200, 155, 630, 315, 175, 180, 560, 250, 150, 365, 500, 195, 175, 285, 180, 235, 275, 290, 325, 495, 265, 475, 165, 390, 325, 265, 545, 290, 290, 120, 355, 210, 155, 165, 170, 285, 240, 265, 255, 355, 150, 440, 225, 280, 365, 450, 315, 130, 195, 175, 150, 205, 125, 145, 325, 295, 470, 230, 125, 285, 385, 170, 235, 200, 125, 185, 325, 275, 255, 370, 210, 410, 340, 170, 195, 190, 140, 250, 150, 220, 415, 200, 130, 225, 130, 250, 135, 135, 160, 255, 270, 165, 185, 100, 340, 335, 125, 210, 250, 285, 260, 180, 250, 230, 245, 235, 200, 280, 210, 210, 130, 430, 380, 225, 245, 95, 200, 340, 170, 145, 85, 145, 180, 125, 260, 245, 400, 405, 520, 400, 435, 250, 265, 360, 450, 90, 125, 270, 510, 160, 145, 460, 420, 255, 595, 240, 305, 715, 690, 365, 115, 620, 320, 215, 230, 225, 455, 
235, 365, 250, 245, 380, 410, 695, 230, 465, 215, 360, 475, 160, 230, 375, 310, 660, 235, 280, 280, 575, 160, 590, 400, 325, 390, 285, 420, 295, 350, 190, 235, 345, 325, 390, 380, 315, 285, 320, 445, 245, 225, 435, 390, 435, 490, 330, 220, 525, 190, 340, 410, 335, 195, 315, 520, 245, 275, 225, 220, 255, 195, 130, 355, 365, 385, 410, 425, 265, 265, 395, 270, 215, 305, 515, 280, 320, 445, 490, 375, 300, 490, 235, 470, 300, 140, 205, 240, 355, 590, 150, 345, 230, 380, 325, 485, 350, 475, 465, 555, 350, 265, 500, 255, 240, 520, 315, 460, 270, 625, 205, 310, 265, 360, 340, 310, 480, 485, 265, 540, 240, 325, 255, 445, 400, 240, 650, 275, 490, 270, 345, 205, 305, 315, 385, 255, 285, 175, 400, 520, 220, 310, 325, 290, 310, 370, 510, 270, 270, 280, 410, 265, 335, 275, 500, 350, 460, 290, 595, 305, 420, 490, 575, 615, 395, 555, 325, 160, 450, 390, 610, 390, 565, 335, 195, 300, 235, 365, 360, 605, 205, 545, 490, 230, 340, 210, 330, 170, 195, 195, 460, 220, 310, 250, 390, 500, 145, 375, 370, 410, 315, 270, 360, 435, 280, 440, 365, 170, 
540, 330, 365, 305, 185, 165, 220, 355, 270, 335, 240, 215, 300, 150, 345, 260, 495, 215, 445, 600, 245, 450, 555, 620, 255, 705, 630, 185, 435, 285, 455, 300, 295, 130, 350, 170, 450, 225, 325, 165, 380, 395, 475, 415, 260, 235, 180, 315, 235, 490, 310, 525, 445, 300, 245, 230, 255, 290, 235, 125, 520, 410, 450, 285, 370, 530, 230, 425, 335, 370, 570, 470, 175, 350, 155, 380, 280, 415, 315, 350, 355, 570, 380, 325, 420, 300, 400, 245, 245, 265, 415, 430, 315, 385, 275, 275, 570, 475, 475, 460, 250, 470, 300, 300, 190, 170, 165, 235, 225, 390, 340, 250, 130, 430, 420, 160, 285, 275, 530, 170, 140, 90, 145, 190, 205, 
240, 270, 265, 305, 220, 500, 160, 230, 375, 235, 210, 360, 225, 170, 180, 180, 170, 170, 195, 510, 230, 355, 180, 390, 200, 330, 465, 335, 210, 485, 430, 505, 720, 895, 210, 325, 260, 235, 200, 325, 480, 250, 295, 575, 400, 590, 480, 325, 385, 275, 470, 390, 305, 270, 545, 520, 335, 355, 445, 570, 955, 350, 395, 270, 320, 500, 260, 1020, 570, 245, 505, 460, 530, 215, 795, 435, 955, 875, 510, 625, 315, 305, 400, 
875, 405, 215, 410, 505, 740, 750, 410, 280, 935, 570, 735, 780, 940, 940, 390, 875, 760, 370, 635, 390, 340, 575, 605, 405, 315, 530, 335, 195, 385, 390, 830, 455, 260, 545, 290, 355, 640, 365, 370, 565, 185, 300, 550, 1060, 995, 1095, 290, 345, 1145, 500, 795, 615, 810, 495, 815, 1085, 625, 515, 645, 595, 995, 620, 1045, 615, 645, 680, 890, 240, 565, 555, 440, 990, 485, 1010, 565, 815, 490, 805, 600, 465, 400, 
465, 310, 300, 1085, 795, 675, 255, 170, 415, 490, 385, 390, 550, 355, 300, 250, 295, 735, 240, 190, 315, 270, 305, 150, 225, 280, 285, 460, 565, 410, 545, 370, 400, 365, 365, 420, 270, 325, 375, 375, 445, 515, 290, 670, 455, 335, 430, 220, 330, 475, 685, 300, 580, 345, 470, 460, 300, 860, 315, 335, 410, 190, 360, 375, 295, 200, 370, 435, 295, 305, 580, 305, 210, 360, 285, 340, 220, 380, 545, 225, 260, 375, 295, 
405, 310, 385, 385, 385, 280, 565, 380, 290, 310, 475, 270, 235, 405, 420, 265, 500, 605, 120, 375, 240, 175, 380, 295, 675, 600, 215, 160, 330, 370, 225, 100, 670, 275, 345, 330, 190, 205, 315, 120, 225, 180, 220, 185, 200, 180, 220, 310, 315, 125, 475, 185, 175, 265, 140, 235, 275, 130, 365, 345, 115, 415, 615, 140, 595, 420, 100, 385, 300, 430, 185, 380, 190, 150, 175, 560, 360, 210, 200, 380, 505, 325, 245, 225, 225, 425, 175, 290, 125, 200, 150, 185, 200, 350, 265, 265, 415, 180, 235, 320, 215, 220, 155, 185, 455, 180, 695, 235, 180, 195, 135, 315, 160, 165, 225, 180, 285, 555, 175, 130, 175, 310, 200, 525, 175, 225, 105, 315, 195, 370, 210, 220, 210, 155, 295, 315, 520, 245, 230, 280, 190, 230, 125, 605, 130, 430, 245, 300, 195, 125, 465, 455, 385, 120, 260, 260, 155, 125, 215, 100, 270, 640, 275, 350, 390, 220, 105, 245, 240, 160, 365, 620, 175, 175, 390, 400, 400, 215, 345, 310, 165, 250, 235, 245, 595, 215, 120, 460, 235, 215, 430, 245, 185, 310, 205, 230, 195, 295, 295, 305, 435, 475, 470, 290, 725, 250, 470, 250, 
255, 295, 585, 415, 295, 170, 305, 440, 240, 370, 270, 345, 210, 320, 245, 205, 720, 510, 385, 390, 565, 280, 265, 235, 200, 245, 155, 190, 170, 260, 250, 430, 145, 470, 235, 415, 490, 375, 310, 585, 640, 280, 285, 385, 360, 230, 330, 125, 400, 145, 165, 280, 140, 205, 220, 200, 390, 465, 235, 325, 585, 455, 195, 160, 265, 180, 155, 145, 250, 225, 225, 195, 155, 195, 200, 165, 190, 185, 360, 300, 210, 155, 330, 390, 450, 475, 295, 820, 615, 275, 340, 245, 170, 260, 220, 710, 445, 460, 575, 390, 205, 300, 225, 430, 400, 645, 490, 375, 315, 485, 370, 490, 130, 625, 925, 560, 315, 270, 885, 590, 980, 605, 1065, 545, 875, 270, 745, 880, 215, 705, 565, 300, 800, 260, 200, 930, 305, 820, 475, 955, 600, 445, 505, 290, 660, 705, 925, 575, 770, 345, 960, 830, 345, 655, 715, 890, 345, 540, 730, 215, 190, 435, 185, 205, 600, 355, 675, 370, 630, 475, 270, 185, 230, 170, 525, 160, 385, 255, 265, 175, 380, 220, 285, 175, 305, 280, 270, 290, 330, 110, 145, 210, 150, 220, 200, 265, 305, 645, 475, 440, 590, 135, 250, 310, 95, 225, 320, 240, 
110, 305, 85, 180, 340, 200, 240, 220, 210, 465, 355, 365, 420, 400, 420, 270, 155, 380, 795, 475, 240, 540, 705, 490, 340, 585, 390, 715, 610, 335, 285, 370, 655, 165, 510, 910, 265, 430, 225, 575, 250, 325, 265, 385, 590, 610, 905, 650, 495, 635, 505, 530, 660, 480, 205, 580, 200, 440, 415, 660, 230, 270, 220, 325, 530, 405, 485, 525, 340, 450, 340, 450, 280, 305, 225, 380, 535, 370, 560, 195, 480, 430, 150, 125, 390, 385, 560, 310, 180, 505, 375, 470, 540, 270, 580, 790, 350, 235, 505, 575, 670, 290, 175, 435, 460, 350, 150, 165, 365, 310, 280, 450, 580, 200, 115, 445, 175, 285, 545, 105, 250, 250, 145, 435, 180, 
355, 175, 185, 185, 230, 140, 400, 220, 270, 195, 395, 530, 185, 320, 575, 300, 370, 205, 225, 530, 235, 380, 305, 330, 365, 365, 160, 260, 350, 155, 290, 155, 200, 230, 295, 235, 340, 455, 345, 300, 280, 215, 110, 115, 170, 130, 195, 160, 280, 520, 380, 380, 295, 585, 305, 390, 615, 425, 560, 415, 195, 430, 300, 365, 460, 740, 410, 360, 965, 190, 450, 310, 180, 190, 365, 290, 760, 495, 295, 250, 390, 350, 565, 570, 600, 280, 225, 760, 250, 475, 535, 405, 420, 210, 770, 600, 660, 320, 485, 465, 670, 725, 155, 485, 235, 235, 420, 430, 350, 565, 465, 240, 265, 555, 200, 600, 235, 460, 810, 385, 430, 420, 340, 575, 360, 320, 365, 630, 560, 345, 945, 510, 300, 390, 320, 295, 355, 135, 380, 320, 180, 205, 475, 465, 585, 645, 910, 600, 750, 395, 425, 510, 260, 650, 270, 215, 460, 135, 250, 195, 195, 110, 485, 475, 210, 245, 150, 270, 170, 270, 350, 110, 400, 500, 145, 130, 305, 560, 120, 65, 395, 325, 570, 470, 230, 185, 320, 115, 265, 155, 135, 310, 170, 160, 195, 190, 350, 480, 365, 320, 250, 235, 235, 330, 205, 150, 90, 415, 440, 435, 195, 405, 545, 545, 170, 265, 320, 380, 170, 450, 255, 250, 165, 215, 195, 135, 290, 155, 75, 380, 455, 115, 365, 280, 105, 195, 80, 175, 605, 265, 120, 220, 130, 370, 110, 355, 220, 210, 375, 265, 250, 375, 195, 450, 155, 140, 285, 295, 175, 170, 295, 410, 560, 180, 165, 315, 190, 185, 370, 205, 170, 110, 205, 240, 425, 260, 495, 145, 210, 420, 395, 210, 445, 190, 285, 185, 375, 240, 95, 125, 335, 190, 370, 140, 220, 260, 395, 210, 230, 255, 315, 210, 85, 150, 345, 175, 220, 435, 100, 155, 110, 425, 85, 225, 570, 490, 170, 370, 285, 855, 220, 260, 205, 205, 285, 195, 310, 210, 145, 130, 175, 415, 245, 270, 165, 440, 345, 430, 110, 285, 545, 605, 630, 390, 545, 120, 90, 350, 155, 145, 165, 230, 185, 245, 385, 630, 140, 555, 100, 205, 210, 185, 160, 360, 190, 290, 115, 185, 195, 125, 310, 615, 265, 495, 215, 325, 
80, 235, 295, 325, 260, 675, 135, 290, 285, 85, 465, 190, 360, 280, 580, 80, 285, 410, 270, 110, 145, 185, 180, 130, 115, 265, 70, 165, 260, 625, 275, 680, 260, 465, 390, 125, 320, 235, 505, 255, 325, 170, 110, 840, 160, 125, 430, 140, 205, 215, 200, 175, 335, 805, 210, 185, 100, 220, 135, 230, 375, 90, 210, 210, 190, 305, 120, 420, 400, 335, 330, 265, 155, 185, 290, 445, 150, 350, 300, 430, 290, 385, 635, 345, 160, 350, 205, 245, 485, 325, 245, 225, 385, 330, 285, 250, 430, 375, 335, 410, 175, 475, 365, 165, 460, 475, 460, 345, 295, 485, 320, 460, 535, 625, 410, 345, 335, 535, 175, 555, 485, 255, 450, 525, 290, 480, 465, 400, 465, 525, 295, 520, 345, 530, 385, 410, 400, 565, 630, 365, 475, 390, 380, 255, 320, 415, 570, 735, 260, 390, 375, 320, 750, 375, 400, 420, 440, 580, 450, 270, 195, 240, 205, 485, 500, 360, 430, 160, 475, 230, 560, 420, 310, 320, 420, 310, 440, 400, 275, 240, 185, 275, 655, 430, 360, 465, 585, 680, 540, 610, 220, 625, 230, 485, 695, 740, 710, 660, 345, 370, 670, 360, 730, 595, 260, 490, 775, 690, 405, 
235, 590, 180, 230, 235, 325, 520, 240, 415, 445, 370, 255, 205, 355, 235, 325, 395, 135, 235, 550, 270, 115, 310, 290, 320, 145, 85, 310, 195, 305, 100, 305, 335, 530, 365, 240, 420, 170, 215, 460, 200, 530, 245, 225, 315, 175, 655, 560, 585, 185, 235, 490, 160, 315, 265, 645, 430, 570, 365, 415, 295, 470, 370, 520, 435, 225, 355, 265, 315, 690, 480, 270, 275, 355, 335, 290, 315, 345, 740, 435, 245, 670, 465, 230, 370, 250, 560, 545, 545, 430, 320, 305, 425, 255, 250, 615, 275, 435, 480, 675, 300, 340, 425, 495, 575, 310, 765, 155, 330, 630, 420, 335, 485, 315, 335, 290, 370, 265, 420, 635, 645, 550, 650, 715, 400, 
345, 535, 440, 525, 240, 525, 270, 195, 680, 810, 205, 655, 675, 655, 560, 330, 300, 435, 650, 750, 810, 560, 480, 265, 615, 425, 505, 465, 715, 440, 795, 130, 320, 425, 470, 630, 650, 740, 320, 285, 440, 315, 415, 590, 520, 590, 330, 765, 265, 415, 470, 625, 325, 595, 565, 365, 705, 535, 375, 385, 395, 255, 600, 720, 220, 370, 530, 155, 275, 515, 545, 470, 330, 560, 510, 675, 445, 530, 550, 515, 275, 430, 315, 540, 480, 630, 355, 605, 555, 415, 440, 510, 245, 565, 710, 545, 675, 465, 755, 645, 440, 390, 360, 425, 265, 795, 520, 535, 375, 315, 545, 750, 405, 365, 235, 250, 540, 615, 430, 775, 605, 190, 260, 375, 440, 410, 230, 535, 720, 690, 305, 475, 355, 415, 415, 690, 205, 210, 615, 245, 555, 320, 305, 660, 520, 130, 210, 185, 170, 155, 330, 395, 410, 440, 125, 370, 495, 195, 350, 440, 460, 150, 180, 150, 195, 350, 355, 530, 140, 430, 205, 420, 240, 95, 305, 335, 220, 270, 190, 180, 150, 250, 390, 175, 295, 200, 420, 195, 125, 145, 500, 360, 330, 265, 160, 295, 145, 130, 120, 285, 420, 280, 380, 185, 235, 250, 285, 300, 315, 150, 220, 205, 190, 200, 175, 180, 205, 135, 245, 140, 205, 100, 130, 200, 270, 315, 355, 255, 140, 115, 240, 200, 600, 385, 305, 235, 170, 145, 160, 210, 270, 205, 205, 170, 380, 220, 185, 255, 640, 460, 160, 290, 190, 135, 245, 165, 375, 125, 200, 495, 415, 460, 475, 320, 435, 455, 370, 280, 285, 570, 390, 450, 400, 295, 580, 460, 370, 230, 220, 335, 435, 335, 420, 385, 625, 425, 200, 550, 405, 380, 145, 435, 430, 215, 415, 355, 320, 515, 320, 415, 580, 525, 470, 545, 420, 470, 315, 170, 290, 520, 345, 180, 115, 225, 300, 185, 120, 175, 125, 425, 170, 150, 465, 330, 200, 160, 125, 285, 315, 325, 370, 355, 370, 
265, 225, 260, 330, 350, 300, 260, 245, 370, 110, 320, 115, 215, 175, 175, 200, 245, 255, 230, 260, 390, 150, 195, 170, 125, 230, 165, 645, 530, 190, 400, 200, 185, 645, 165, 165, 160, 170, 180, 220, 105, 195, 335, 110, 175, 245, 195, 145, 205, 235, 190, 440, 415, 795, 570, 190, 155, 180, 365, 230, 425, 385, 425, 100, 110, 220, 170, 280, 230, 195, 150, 355, 275, 800, 230, 335, 465, 345, 370, 290, 295, 305, 205, 370, 300, 370, 700, 130, 205, 445, 270, 180, 320, 175, 475, 315, 605, 340, 375, 365, 335, 365, 685, 320, 625, 440, 215, 335, 670, 370, 300, 170, 250, 330, 435, 450, 395, 550, 660, 230, 740, 465, 255, 335, 235, 265, 345, 270, 655, 160, 325, 95, 220, 320, 570, 180, 290, 345, 175, 395, 205, 160, 310, 260, 85, 255, 455, 370, 150, 110, 270, 290, 455, 530, 85, 450, 280, 380, 330, 435, 220, 395, 115, 115, 155, 195, 125, 
310, 350, 125, 310, 350, 300, 470, 115, 325, 335, 535, 120, 355, 630, 195, 135, 365, 205, 350, 310, 780, 470, 500, 395, 445, 210, 285, 180, 630, 445, 205, 135, 220, 115, 190, 205, 375, 405, 600, 200, 340, 120, 215, 135, 200, 315, 365, 105, 165, 545, 235, 150, 140, 175, 550, 110, 200, 195, 100, 445, 100, 90, 595, 380, 125, 170, 140, 125, 180, 300, 305, 170, 120, 75, 390, 120, 130, 290, 195, 120, 250, 50, 80, 255, 
305, 455, 315, 160, 310, 335, 190, 85, 160, 280, 225, 490, 135, 100, 205, 280, 280, 130, 170, 465, 115, 90, 125, 140, 85, 90, 300, 375, 165, 230, 230, 130, 110, 210, 565, 445, 575, 115, 100, 405, 240, 240, 200, 180, 70, 80, 130, 105, 435, 150, 400, 210, 85, 165, 105, 120, 160, 270, 105, 255, 360, 245, 140, 145, 90, 430, 265, 160, 425, 455, 310, 355, 200, 145, 180, 145, 120, 110, 175, 130, 140, 155, 380, 220, 315, 370, 165, 460, 170, 460, 150, 125, 525, 140, 315, 255, 445, 470, 335, 330, 130, 460, 190, 235, 465, 125, 110, 295, 525, 185, 170, 255, 185, 200, 140, 135, 150, 280, 250, 195, 270, 100, 470, 125, 295, 370, 240, 225, 315, 320, 180, 230, 420, 195, 385, 350, 335, 105, 260, 375, 215, 345, 140, 260, 185, 220, 430, 165, 200, 90, 245, 215, 470, 265, 180, 305, 340, 585, 215, 205, 260, 405, 330, 385, 390, 395, 400, 460, 570, 440, 565, 300, 245, 230, 365, 320, 445, 205, 410, 390, 280, 525, 350, 265, 360, 435, 230, 335, 305, 160, 290, 345, 270, 215, 220, 425, 205, 450, 400, 650, 290, 350, 230, 400, 465, 465, 185, 600, 515, 385, 660, 475, 275, 245, 325, 315, 250],  dtype=float)



Grade3Level3Reading = np.array([990, 69, 47, 43, 19, 50, 83, 73, 58, 42, 62, 36, 44, 64, 61, 60, 93, 82, 82, 64, 69, 60, 56, 81, 79, 42, 88, 70, 80, 92, 89, 69, 77, 59, 88, 46, 66, 57, 71, 76, 75, 90, 85, 72, 77, 77, 77, 36, 67, 67, 68, 82, 67, 73, 47, 87, 77, 82, 80, 76, 63, 73, 59, 66, 77, 81, 57, 46, 61, 84, 82, 59, 59, 78, 74, 79, 53, 83, 63, 70, 46, 79, 89, 93, 81, 90, 94, 84, 80, 77, 70, 93, 90, 82, 87, 78, 93, 92, 53, 82, 56, 81, 77, 84, 75, 88, 54, 88, 100, 93, 87, 65, 92, 92, 76, 87, 79, 92, 100, 85, 85, 50, 75, 88, 94, 88, 96, 84, 68, 80, 89, 52, 94, 79, 65, 84, 88, 93, 74, 94, 86, 92, 97, 92, 75, 80, 50, 87, 64, 69, 90, 70, 100, 89, 97, 100, 65, 95, 100, 95, 85, 74, 85, 61, 90, 88, 94, 60, 76, 92, 95, 88, 93, 98, 86, 96, 100, 60, 92, 74, 87, 79, 87, 83, 62, 88, 92, 56, 98, 80, 78, 92, 81, 84, 93, 91, 60, 100, 85, 90, 100, 89, 90, 98, 83, 82, 100, 83, 72, 69, 58, 93, 92, 73, 90, 98, 89, 79, 88, 76, 85, 67, 78, 82, 88, 86, 82, 82, 73, 91, 80, 74, 83, 97, 74, 95, 93, 85, 82, 88, 92, 79, 94, 88, 85, 91, 86, 83, 82, 83, 72, 63, 
79, 83, 77, 75, 100, 84, 95, 97, 74, 100, 94, 81, 88, 73, 80, 15, 76, 78, 79, 80, 65, 86, 91, 79, 70, 74, 73, 78, 89, 68, 88, 73, 91, 73, 64, 68, 66, 86, 80, 71, 76, 79, 77, 88, 60, 78, 86, 91, 61, 78, 85, 59, 68, 74, 72, 81, 64, 81, 62, 89, 82, 85, 77, 94, 93, 95, 93, 76, 73, 87, 70, 89, 95, 71, 71, 88, 79, 82, 85, 50, 69, 86, 98, 55, 84, 85, 81, 90, 73, 94, 84, 82, 59, 74, 100, 54, 89, 75, 69, 65, 62, 81, 83, 57, 77, 95, 84, 85, 92, 73, 89, 88, 64, 67, 90, 91, 79, 75, 88, 84, 80, 85, 63, 86, 89, 64, 81, 88, 74, 90, 90, 84, 76, 84, 62, 89, 100, 91, 76, 71, 77, 76, 76, 96, 93, 62, 62, 65, 79, 90, 57, 78, 80, 83, 61, 
82, 71, 73, 79, 68, 69, 91, 55, 97, 74, 85, 72, 75, 89, 47, 89, 75, 52, 47, 73, 43, 79, 64, 57, 63, 84, 71, 55, 73, 81, 80, 56, 78, 89, 64, 19, 66, 65, 58, 76, 67, 81, 100, 100, 89, 94, 72, 89, 67, 48, 77, 95, 76, 60, 78, 94, 91, 83, 90, 76, 84, 85, 89, 77, 77, 76, 67, 79, 77, 78, 74, 81, 79, 92, 71, 67, 77, 75, 83, 95, 94, 47, 67, 82, 76, 68, 100, 78, 77, 80, 81, 90, 83, 76, 36, 80, 81, 83, 64, 72, 66, 88, 84, 88, 94, 50, 73, 40, 70, 89, 59, 67, 56, 64, 63, 59, 50, 38, 67, 71, 85, 73, 90, 72, 59, 64, 38, 62, 55, 53, 21, 57, 62, 47, 42, 69, 53, 52, 72, 36, 82, 74, 92, 60, 92, 95, 65, 13, 53, 85, 59, 83, 46, 52, 63, 72, 60, 68, 81, 58, 61, 74, 76, 92, 65, 81, 96, 55, 70, 47, 75, 58, 85, 71, 45, 66, 30, 38, 71, 67, 74, 71, 90, 68, 76, 80, 72, 50, 67, 94, 78, 77, 57, 77, 61, 57, 68, 64, 60, 65, 59, 52, 62, 67, 85, 82, 81, 84, 83, 62, 42, 74, 83, 89, 87, 95, 71, 84, 91, 85, 83, 57, 76, 80, 89, 93, 69, 89, 78, 80, 71, 88, 85, 65, 76, 75, 92, 81, 70, 78, 79, 100, 75, 63, 89, 88, 83, 86, 68, 79, 81, 93, 88, 93, 91, 70, 85, 89, 84, 
81, 88, 88, 66, 79, 79, 83, 75, 80, 78, 85, 81, 69, 77, 77, 75, 91, 84, 92, 90, 89, 96, 75, 84, 64, 50, 88, 90, 84, 83, 97, 92, 90, 83, 81, 63, 73, 75, 68, 75, 84, 80, 86, 88, 83, 94, 50, 97, 84, 100, 50, 100, 97, 89, 85, 67, 81, 94, 59, 73, 85, 94, 71, 77, 84, 88, 86, 95, 85, 69, 78, 83, 91, 65, 69, 81, 72, 90, 93, 75, 66, 46, 89, 88, 67, 84, 81, 79, 83, 56, 89, 72, 100, 78, 52, 69, 42, 47, 62, 47, 78, 50, 65, 79, 54, 58, 77, 63, 59, 59, 61, 62, 78, 61, 56, 50, 38, 70, 64, 81, 66, 42, 57, 53, 68, 61, 73, 66, 76, 74, 64, 66, 83, 74, 75, 58, 69, 74, 50, 85, 21, 74, 49, 72, 82, 53, 85, 42, 57, 62, 64, 74, 72, 70, 56, 28, 74, 85, 100, 81, 65, 81, 81, 82, 89, 96, 71, 55, 93, 76, 77, 62, 71, 40, 59, 85, 71, 93, 86, 89, 75, 78, 78, 78, 88, 67, 81, 74, 73, 87, 64, 76, 64, 81, 91, 63, 64, 90, 71, 76, 89, 63, 66, 75, 70, 78, 52, 
35, 86, 79, 71, 92, 70, 77, 72, 75, 92, 77, 59, 32, 24, 21, 52, 69, 79, 68, 100, 69, 84, 94, 86, 91, 52, 100, 67, 74, 67, 77, 69, 30, 97, 83, 77, 59, 62, 69, 83, 100, 88, 100, 50, 86, 62, 68, 68, 67, 57, 92, 
59, 86, 11, 44, 88, 72, 62, 65, 64, 53, 80, 70, 53, 36, 100, 73, 72, 85, 75, 38, 100, 60, 73, 70, 61, 85, 75, 92, 74, 52, 50, 83, 70, 76, 70, 81, 56, 48, 46, 58, 88, 60, 88, 52, 50, 70, 35, 85, 45, 77, 43, 68, 62, 55, 74, 62, 75, 62, 67, 74, 42, 78, 79, 77, 46, 87, 59, 48, 86, 67, 85, 70, 74, 72, 61, 59, 90, 78, 87, 85, 76, 55, 79, 64, 56, 58, 98, 92, 71, 75, 42, 59, 55, 77, 81, 68, 80, 89, 65, 47, 81, 75, 69, 95, 67, 67, 83, 74, 89, 91, 81, 54, 86, 82, 74, 91, 100, 53, 40, 62, 60, 87, 67, 77, 41, 85, 91, 71, 65, 84, 84, 74, 47, 93, 75, 74, 65, 84, 82, 83, 88, 79, 100, 43, 69, 92, 81, 57, 55, 62, 76, 65, 69, 83, 77, 
55, 85, 91, 87, 73, 88, 41, 79, 38, 91, 84, 86, 81, 79, 59, 68, 58, 62, 52, 90, 91, 75, 80, 80, 90, 88, 46, 54, 82, 81, 91, 90, 82, 84, 87, 54, 66, 74, 84, 74, 80, 75, 86, 84, 71, 78, 86, 78, 88, 71, 53, 83, 
77, 83, 66, 86, 76, 62, 67, 76, 82, 80, 81, 46, 83, 85, 89, 70, 79, 79, 68, 72, 87, 92, 88, 88, 95, 52, 74, 53, 83, 55, 56, 58, 77, 94, 88, 59, 64, 77, 69, 89, 58, 74, 75, 56, 81, 91, 97, 74, 76, 88, 100, 69, 73, 72, 79, 51, 39, 53, 90, 87, 65, 38, 60, 46, 71, 66, 77, 86, 77, 88, 92, 91, 70, 80, 90, 76, 89, 54, 71, 71, 92, 68, 66, 75, 100, 62, 72, 78, 81, 84, 67, 74, 71, 78, 68, 67, 71, 55, 92, 89, 64, 66, 72, 100, 64, 79, 89, 80, 55, 68, 33, 75, 61, 83, 59, 63, 79, 85, 74, 88, 80, 68, 89, 52, 47, 69, 78, 42, 65, 82, 72, 66, 69, 72, 72, 67, 82, 90, 76, 90, 85, 50, 67, 62, 67, 32, 73, 59, 59, 67, 57, 85, 58, 62, 58, 86, 47, 65, 69, 83, 67, 78, 75, 52, 69, 67, 90, 57, 74, 62, 71, 79, 73, 79, 56, 86, 91, 57, 64, 68, 61, 58, 46, 83, 57, 70, 75, 88, 72, 43, 39, 49, 44, 74, 76, 45, 89, 70, 80, 69, 64, 76, 66, 65, 64, 41, 77, 54, 65, 82, 72, 81, 93, 100, 86, 90, 39, 91, 85, 82, 77, 92, 85, 71, 80, 70, 93, 85, 92, 86, 72, 81, 68, 66, 77, 73, 64, 64, 73, 65, 67, 24, 94, 41, 74, 38, 54, 41, 46, 75, 51, 87, 86, 85, 29, 67, 82, 74, 63, 
66, 72, 74, 51, 54, 75, 56, 61, 77, 44, 58, 51, 68, 62, 28, 63, 49, 41, 43, 67, 64, 43, 62, 90, 80, 52, 48, 66, 73, 50, 82, 61, 65, 44, 47, 57, 93, 73, 40, 71, 73, 58, 73, 20, 58, 86, 82, 57, 85, 79, 69, 84, 
62, 53, 38, 56, 86, 59, 38, 59, 37, 57, 71, 72, 70, 75, 89, 85, 48, 70, 53, 69, 74, 47, 43, 79, 72, 31, 60, 72, 73, 75, 52, 59, 55, 42, 56, 58, 67, 80, 88, 95, 92, 70, 90, 63, 76, 86, 85, 71, 79, 82, 57, 73, 
92, 56, 62, 72, 80, 84, 83, 43, 71, 81, 72, 78, 76, 95, 89, 63, 67, 91, 76, 98, 88, 79, 52, 68, 91, 78, 70, 65, 89, 86, 55, 65, 79, 87, 92, 62, 67, 83, 50, 86, 79, 95, 83, 91, 92, 83, 53, 73, 97, 94, 43, 76, 
80, 92, 79, 73, 57, 62, 78, 85, 71, 68, 84, 53, 65, 59, 87, 79, 93, 70, 90, 64, 100, 88, 50, 56, 67, 68, 71, 76, 84, 65, 64, 77, 68, 69, 80, 72, 87, 72, 70, 87, 51, 87, 79, 90, 84, 60, 68, 93, 68, 78, 92, 79, 76, 76, 56, 80, 71, 60, 47, 94, 70, 77, 89, 76, 83, 100, 76, 74, 94, 58, 92, 65, 84, 74, 58, 97, 57, 54, 62, 72, 85, 92, 76, 82, 71, 50, 85, 76, 82, 79, 100, 77, 81, 71, 98, 98, 67, 77, 77, 68, 87, 83, 69, 90, 47, 77, 100, 67, 77, 73, 82, 61, 97, 74, 98, 100, 54, 76, 44, 61, 65, 74, 71, 83, 88, 40, 44, 71, 77, 100, 87, 47, 67, 82, 76, 84, 100, 94, 93, 57, 50, 66, 79, 53, 72, 75, 27, 82, 71, 79, 88, 82, 84, 57, 86, 82, 75, 83, 80, 70, 63, 67, 76, 82, 40, 0, 84, 85, 86, 42, 95, 41, 50, 75, 78, 75, 83, 56, 81, 83, 96, 64, 89, 69, 53, 85, 66, 77, 74, 85, 63, 82, 75, 73, 60, 85, 79, 82, 87, 96, 54, 53, 75, 72, 85, 81, 85, 76, 86, 91, 75, 80, 84, 41, 88, 89, 68, 48, 77, 62, 72, 31, 62, 52, 89, 64, 79, 72, 65, 75, 56, 46, 64, 59, 71, 100, 69, 71, 43, 61, 76, 70, 48, 69, 76, 68, 71, 61, 57, 53, 83, 79, 68, 70, 70, 55, 42, 59, 75, 82, 95, 83, 85, 79, 62, 46, 53, 51, 57, 66, 60, 92, 60, 68, 50, 82, 89, 62, 78, 59, 71, 71, 64, 73, 78, 90, 74, 85, 90, 81, 79, 70, 68, 61, 82, 39, 85, 76, 90, 61, 92, 77, 83, 72, 92, 83, 71, 87, 81, 67, 87, 53, 57, 67, 87, 50, 73, 94, 72, 64, 73, 77, 69, 36, 49, 81, 82, 85, 61, 89, 88, 68, 88, 74, 85, 78, 73, 70, 75, 93, 43, 42, 77, 63, 59, 67, 91, 71, 60, 65, 87, 78, 88, 85, 60, 50, 67, 76, 74, 78, 85, 65, 85, 76, 86, 91, 73, 69, 43, 67, 83, 91, 41, 69, 80, 65, 90, 61, 82, 78, 92, 55, 55, 66, 82, 86, 72, 74, 82, 90, 68, 58, 86, 55, 95, 84, 75, 81, 67, 92, 80, 93, 72, 87, 81, 89, 94, 76, 73, 93, 73, 80, 83, 88, 81, 75, 74, 96, 73, 62, 81, 78, 83, 92, 71, 74, 87, 83, 79, 66, 82, 76, 82, 83, 84, 87, 63, 93, 90, 80, 79, 97, 95, 83, 67, 61, 89, 79, 79, 87, 80, 69, 85, 75, 82, 94, 90, 70, 82, 88, 98, 50, 77, 81, 98, 61, 85, 82, 69, 78, 81, 92, 89, 84, 84, 81, 88, 89, 93, 81, 68, 68, 80, 81, 80, 72, 88, 75, 76, 87, 86, 82, 75, 85, 71, 83, 96, 96, 95, 79, 60, 89, 71, 91, 90, 82, 64, 89, 86, 88, 92, 89, 73, 75, 68, 98, 68, 75, 60, 80, 87, 79, 65, 75, 76, 93, 89, 82, 88, 82, 81, 66, 71, 78, 84, 92, 78, 63, 58, 61, 84, 81, 63, 78, 86, 96, 86, 73, 78, 70, 72, 61, 93, 81, 87, 82, 71, 76, 65, 74, 59, 86, 60, 85, 87, 85, 88, 86, 80, 84, 58, 85, 70, 83, 50, 80, 69, 89, 82, 72, 90, 71, 44, 79, 82, 66, 77, 85, 75, 84, 75, 93, 65, 90, 100, 82, 71, 80, 95, 78, 80, 91, 71, 80, 86, 83, 56, 94, 70, 94, 75, 100, 95, 58, 88, 81, 69, 83, 91, 79, 83, 78, 55, 71, 70, 79, 71, 87, 82, 93, 98, 68, 62, 85, 67, 83, 88, 57, 50, 35, 55, 57, 75, 69, 82, 64, 78, 88, 77, 84, 78, 78, 76, 88, 72, 68, 40, 83, 93, 72, 82, 66, 85, 92, 74, 92, 72, 84, 62, 88, 90, 79, 91, 85, 96, 96, 87, 69, 69, 93, 96, 95, 86, 90, 91, 95, 80, 89, 88, 59, 98, 94, 94, 89, 98, 82, 84, 82, 84, 67, 86, 100, 85, 93, 80, 100, 90, 87, 95, 96, 81, 90, 85, 79, 73, 87, 76, 55, 83, 72, 67, 79, 83, 91, 80, 87, 100, 84, 68, 83, 90, 82, 96, 78, 91, 93, 78, 84, 93, 100, 96, 95, 70, 47, 81, 94, 86, 44, 97, 87, 96, 94, 91, 94, 96, 85, 94, 75, 97, 81, 100, 91, 92, 88, 90, 89, 96, 94, 67, 83, 87, 96, 91, 87, 94, 95, 92, 89, 93, 95, 83, 92, 83, 70, 82, 83, 68, 93, 86, 95, 94, 84, 97, 84, 95, 90, 75, 57, 79, 94, 67, 100, 82, 58, 78, 41, 29, 62, 27, 50, 40, 36, 46, 59, 40, 89, 88, 81, 77, 73, 77, 74, 85, 62, 78, 90, 84, 67, 96, 84, 71, 93, 50, 84, 61, 77, 57, 88, 85, 71, 32, 77, 71, 46, 95, 75, 47, 86, 77, 71, 78, 69, 86, 80, 67, 70, 83, 89, 71, 79, 77, 82, 50, 39, 64, 71, 76, 68, 73, 72, 75, 68, 67, 71, 55, 68, 81, 76, 81, 29, 80, 59, 69, 52, 80, 68, 50, 95, 52, 80, 92, 73, 86, 81, 78, 64, 95, 65, 71, 67, 89, 76, 72, 81, 78, 63, 88, 52, 78, 86, 92, 72, 76, 75, 77, 83, 89, 81, 64, 84, 79, 89, 89, 94, 92, 92, 79, 88, 86, 63, 74, 82, 80, 88, 48, 78, 86, 81, 77, 85, 79, 93, 77, 93, 86, 93, 90, 61, 60, 76, 92, 82, 68, 91, 27, 67, 58, 80, 86, 77, 34, 62, 89, 52, 74, 82, 90, 45, 83, 92, 83, 80, 82, 81, 59, 70, 97, 65, 67, 48, 76, 63, 81, 89, 75, 32, 55, 48, 61, 68, 91, 91, 95, 90, 70, 95, 82, 41, 93, 65, 95, 92, 63, 71, 80, 46, 63, 52, 91, 77, 83, 86, 81, 79, 88, 50, 52, 62, 93, 68, 71, 67, 97, 89, 38, 68, 48, 73, 61, 64, 61, 20, 78, 57, 81, 85, 90, 71, 95, 80, 93, 95, 44, 77, 75, 93, 77, 86, 76, 86, 79, 79, 90, 91, 79, 81, 96, 68, 85, 75, 100, 77, 74, 79, 85, 81, 79, 75, 80, 81, 74, 86, 47, 85, 79, 80, 66, 90, 86, 75, 90, 77, 76, 95, 92, 68, 54, 80, 
77, 68, 64, 66, 64, 57, 72, 81, 70, 78, 67, 63, 86, 69, 90, 83, 90, 56, 64, 97, 72, 97, 98, 90, 62, 88, 98, 93, 81, 83, 40, 57, 55, 65, 84, 100, 87, 85, 65, 67, 94, 77, 64, 77, 67, 90, 100, 93, 76, 83, 94, 70, 82, 63, 70, 70, 84, 69, 100, 88, 82, 67, 75, 81, 46, 86, 62, 66, 81, 90, 100, 84, 86, 84, 40, 80, 75, 81, 50, 45, 72, 57, 80, 62, 74, 78, 77, 45, 68, 33, 71, 88, 62, 55, 69, 95, 86, 65, 78, 75, 100, 89, 78, 89, 63, 64, 72, 100, 66, 64, 76, 65, 100, 88, 81, 91, 85, 68, 71, 63, 79, 92, 65, 100, 41, 92, 68, 94, 92, 79, 67, 78, 71, 56, 83, 50, 47, 65, 78, 82, 85, 62, 69, 82, 48, 53, 64, 43, 66, 57, 66, 75, 36, 76, 
78, 77, 66, 80, 78, 56, 71, 43, 65, 79, 77, 83, 54, 78, 89, 74, 41, 83, 37, 77, 77, 85, 76, 60, 70, 62, 31, 78, 52, 69, 70, 77, 74, 79, 69, 55, 68, 61, 43, 76, 56, 78, 83, 49, 61, 65, 58, 74, 82],  dtype=float)

for i,c in enumerate(EnrolledStudents):
  print("{} Studetns Enrolled = {} Percentage of Gr.3's reaching reading level 3".format(c, Grade3Level3Reading[i]))

l0 = tf.keras.layers.Dense(units=4, input_shape=[1])

model = tf.keras.Sequential([l0])

model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.Adam(0.1))

history = model.fit(EnrolledStudents, Grade3Level3Reading, epochs=500, verbose=False)
print("Finished training the model")

# Epoch = number of times the A.I reviews the data set.

# units=1 means 1 variable

#input Shape =  

print(model.predict([220.0]))
print(model.predict([860.0]))
print(model.predict([1145.0]))

print("These are the layer variables: {}".format(l0.get_weights()))

