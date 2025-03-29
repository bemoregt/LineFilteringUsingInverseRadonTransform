# Example Workflow

This document illustrates a step-by-step workflow of how the Radon transform filtering works.

## Step 1: Original Image

Consider a sample image with both horizontal and vertical lines:

```
+---------------+
|       |       |
|       |       |
|       |       |
|-------|-------|
|       |       |
|       |       |
|       |       |
+---------------+
```

## Step 2: Radon Transform (Sinogram Creation)

The Radon transform converts the 2D image into a representation of projections at different angles:

```
+-------------------+
|        /|\        |
|       / | \       |
|      /  |  \      |
|     /   |   \     |
|    /    |    \    |
|   /     |     \   |
|  /      |      \  |
| /       |       \ |
+-------------------+
    Angle (0-180°)
```

- Horizontal axis: Projection angle (0-180°)
- Vertical axis: Distance from center

The bright spots/lines in the sinogram correspond to lines in the original image:
- Vertical lines in the original image → Prominent features at 0° in the sinogram
- Horizontal lines in the original image → Prominent features at 90° in the sinogram

## Step 3: Apply Gaussian Mask to Sinogram

We selectively filter specific angular components by applying a Gaussian mask:

```
+-------------------+
|                   |
|                   |
|        |||        |
|        |||        |
|        |||        |
|                   |
|                   |
|                   |
+-------------------+
```

In this example, the mask is designed to preserve information around 90° (horizontal lines in the original image) while suppressing other angles.

## Step 4: Inverse Radon Transform

Applying the inverse Radon transform to the filtered sinogram:

```
+---------------+
|               |
|               |
|               |
|---------------|
|               |
|               |
|               |
+---------------+
```

The result shows enhanced horizontal lines, while the vertical lines have been suppressed.

## Adjusting the Filter

By changing the parameters of the Gaussian mask, we can control which directional features are preserved:

- Changing the center position of the mask allows selecting different orientations
- Adjusting the sigma (width) of the Gaussian controls the specificity of the filter
- Multiple Gaussian components can be combined to select multiple orientations

This selective filtering capability makes the Radon transform a powerful tool for applications like:
- Enhancing specific edge orientations in images
- Removing directional noise or artifacts
- Highlighting structures with known orientations (e.g., blood vessels)
