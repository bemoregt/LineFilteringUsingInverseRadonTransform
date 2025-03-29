# Sample Images

This directory will contain sample images demonstrating the application.

## Expected Results

When using the application, you should see something similar to the following process:

1. **Original Image**: A grayscale image with various line structures
2. **Sinogram**: The Radon transform of the image showing projections at different angles
3. **Reconstructed Image**: The inverse Radon transform after applying the Gaussian mask, highlighting specific directional features

## How to Test

1. Run the application using `python radon_transform_app.py`
2. Click "Load Image" and select a grayscale image
3. Observe the three panels showing the original, sinogram, and reconstructed images
