import numpy as np
import time
import cv2
from tqdm import trange
from ipycanvas import Canvas, hold_canvas
from ipywidgets import Button, HBox
from IPython.display import display


class NeuralNetwork:

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate, epochs=5):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate
        self.epochs = epochs

        self.weight_input_hidden = np.random.normal(0.0, pow(self.hidden_nodes, -0.5), (self.hidden_nodes, self.input_nodes))
        self.weight_hidden_output = np.random.normal(0.0, pow(self.output_nodes, -0.5), (self.output_nodes, self.hidden_nodes))

        self.activation_function = lambda x: 1 / (1 + np.exp(-x))
        
    def predict(self, inputs):

        hidden_inputs = np.dot(self.weight_input_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(self.weight_hidden_output, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return hidden_outputs, final_outputs
    
    def weight_update(self, errors, outputs_1, outputs_2):
        return  self.learning_rate * np.dot((errors * outputs_2 * (1.0 - outputs_2)), np.transpose(outputs_1))

    
    def fit(self, inputs, targets):
         for epoch in range(self.epochs):
             for i in trange(inputs.shape[0]):
                
                input = np.array(inputs[i, :], ndmin=2).T
                target = np.zeros(self.output_nodes)
                target[int(targets[i])] = 1
            
                target = np.array(target, ndmin=2).T
        
                hidden_outputs, final_outputs = self.predict(input)

                output_errors = target - final_outputs
                hidden_errors = np.dot(self.weight_hidden_output.T, output_errors)

                self.weight_hidden_output += self.weight_update(output_errors, hidden_outputs, final_outputs)

                self.weight_input_hidden += self.weight_update(hidden_errors, input, hidden_outputs)
                time.sleep(10**(-8))
        
    def score(self, test_inputs, test_targets):
        score_card = []
        for i in range(test_inputs.shape[0]):
            inputs = test_inputs[i, :]
            correct_label = test_targets[i]
            outputs = self.predict(inputs)[1]
            label = np.argmax(outputs)
            score_card.append(label == correct_label)
        accuracy = sum(score_card) / len(score_card)
        print('Accuracy = ', accuracy)
        
    def writer(self):
        canvas = Canvas(width=280, height=280, sync_image_data=True)
        canvas.fill_style = '#fec'
        canvas.fill_rect(0, 0, canvas.width, canvas.height)

        drawing = False

        def on_mouse_down(x, y):
            global drawing

            drawing = True

        def on_mouse_move(x, y):
            global drawing

            if not drawing:
                return

            with hold_canvas(canvas):
                canvas.fill_style = 'black'
                canvas.fill_circle(x, y, 8)

        def on_mouse_up(x, y):
            global drawing

            drawing = False


        canvas.on_mouse_down(on_mouse_down)
        canvas.on_mouse_move(on_mouse_move)
        canvas.on_mouse_up(on_mouse_up)

        def on_button_clear(*args, **kwargs):
            with hold_canvas(canvas):
                canvas.clear()
                canvas.fill_style = '#fec'
                canvas.fill_rect(0, 0, canvas.width, canvas.height)
                
        def save_to_file(*args, **kwargs):
            with hold_canvas(canvas):
                canvas.to_file('Images/my_file.png')
                
        def on_predict(*args, **kwargs):
            with hold_canvas(canvas):
                img_array = canvas.get_image_data() 
                img_array = cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
                img_array = cv2.bitwise_not(img_array)
                img_array = cv2.resize(img_array,(28,28))
                    
                img_array = img_array/255.0
                img_array = np.reshape(img_array, 784)
                img_array = np.array(img_array, ndmin=2).T
                result = self.predict(img_array)[1]
                label = np.argmax(result)
                canvas.font = '32px serif'
                canvas.fill_text(label, 10, 32)   

        clear_button = Button(description="Clear")
        predict_button = Button(description="Predict")
        save_button = Button(description="Save")

        save_button.on_click(save_to_file)
        clear_button.on_click(on_button_clear)
        predict_button.on_click(on_predict)
        all_widgets = HBox((canvas, clear_button, predict_button, save_button))
        display(all_widgets)