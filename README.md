# Line Filtering Using Inverse Radon Transform

This project demonstrates the application of Radon transform and its inverse for line filtering in images. The implementation uses a Gaussian padding technique to enhance specific angular components in the frequency domain.

## Overview

The Radon transform is a fundamental tool in image processing that maps a 2D image into a series of 1D projections along different angles. This transformation is particularly useful in highlighting linear features within an image. This application demonstrates:

1. Applying the Radon transform to convert an image into a sinogram
2. Selectively filtering frequency components using a Gaussian mask
3. Reconstructing the filtered image using the inverse Radon transform

## Features

- Load and display grayscale images
- Apply Radon transform to generate sinograms
- Implement Gaussian padding to selectively filter directional components
- Reconstruct filtered images using inverse Radon transform
- Side-by-side visualization of original, sinogram, and reconstructed images

## Requirements

- Python 3.x
- NumPy
- PIL (Python Imaging Library)
- scikit-image
- matplotlib
- scipy
- tkinter

## Installation

```bash
pip install numpy pillow scikit-image matplotlib scipy
```

Tkinter usually comes pre-installed with Python. If not, you can install it separately.

## Usage

1. Run the script:
```bash
python radon_transform_app.py
```

2. Click "Load Image" to select an input image
3. The application will display:
   - Original image (left)
   - Radon transform sinogram (middle)
   - Reconstructed image after filtering (right)

## How It Works

1. **Image Loading**: The application loads a grayscale image and resizes it to 512×512 pixels.

2. **Radon Transform**: The image is transformed into a sinogram using the Radon transform, where each column represents the projection of the image at a specific angle.

3. **Gaussian Padding**: Instead of applying zero padding, the application uses a Gaussian mask to filter the sinogram. This approach selectively suppresses certain angular components while preserving others, effectively filtering lines of specific orientations in the image.

4. **Inverse Radon Transform**: The filtered sinogram is then reconstructed back into an image using the inverse Radon transform, resulting in an image where specific linear features are enhanced or suppressed.

## Mathematical Background

The Radon transform of a function f(x,y) is defined as:

R{f}(r,θ) = ∫∫ f(x,y)δ(r - x·cos(θ) - y·sin(θ)) dx dy

Where:
- r is the perpendicular distance from the origin to the line
- θ is the angle of the line
- δ is the Dirac delta function

The inverse Radon transform reconstructs the original function from its projections.

## Applications

This technique is useful in:
- Medical imaging (CT scans)
- Directional feature detection
- Edge enhancement in specific orientations
- Removing or highlighting linear artifacts in images

## License

This project is open source and available under the MIT License.

## Acknowledgements

This implementation utilizes the scikit-image library for Radon transform operations and matplotlib for visualization.
