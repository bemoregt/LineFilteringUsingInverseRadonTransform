import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from skimage.transform import radon, iradon
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.btn_load = tk.Button(self)
        self.btn_load["text"] = "Load Image"
        self.btn_load["command"] = self.load_image
        self.btn_load.grid(row=0, column=0)
        
        self.canvas1 = tk.Canvas(self.master, width=512, height=512)
        self.canvas1.grid(row=1, column=0)
        
        self.canvas2 = tk.Canvas(self.master, width=512, height=512)
        self.canvas2.grid(row=1, column=1)
        
        self.canvas3 = tk.Canvas(self.master, width=512, height=512)
        self.canvas3.grid(row=1, column=2)
        
    def load_image(self):
        file_path = filedialog.askopenfilename()
        image = Image.open(file_path).convert('L')
        image = image.resize((512, 512))
        
        # Display the original image
        photo = ImageTk.PhotoImage(image)
        self.canvas1.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas1.image = photo
        
        # Apply radon transform
        image_np = np.array(image)
        theta = np.linspace(0., 180., max(image_np.shape), endpoint=False)
        sinogram = radon(image_np, theta=theta)
        
        # Apply Gaussian padding instead of zero padding
        # Define the region parameters
        x_center, y_center = 239, 214  # Center of the region to pad
        x_size, y_size = 50, 50        # Size of the region
        sigma = 20                     # Standard deviation for Gaussian
        
        # Create a mask with Gaussian falloff
        x, y = np.meshgrid(np.arange(sinogram.shape[1]), np.arange(sinogram.shape[0]))
        mask = 1 - np.exp(-((x - y_center)**2 + (y - x_center)**2) / (2 * sigma**2))
        
        # Apply the mask to the sinogram
        sinogram = sinogram * mask
        
        # Display sinogram
        # Normalize sinogram for display
        sinogram_display = (sinogram - np.min(sinogram)) / np.ptp(sinogram) * 255
        sinogram_image = Image.fromarray(sinogram_display.astype(np.uint8)).convert('L')
        sinogram_photo = ImageTk.PhotoImage(sinogram_image)
        self.canvas2.create_image(0, 0, anchor=tk.NW, image=sinogram_photo)
        self.canvas2.image = sinogram_photo
        
        # Apply inverse radon transform
        reconstructed = iradon(sinogram, theta=theta)
        reconstructed = (reconstructed - np.min(reconstructed)) / np.ptp(reconstructed)  # normalization
        reconstructed_image = Image.fromarray(np.uint8(reconstructed*255)).convert('L')
        reconstructed_photo = ImageTk.PhotoImage(reconstructed_image)
        self.canvas3.create_image(0, 0, anchor=tk.NW, image=reconstructed_photo)
        self.canvas3.image = reconstructed_photo

# Application startup
root = tk.Tk()
root.title("Radon Transform with Gaussian Padding")
root.geometry("1536x512")
app = Application(master=root)
app.mainloop()