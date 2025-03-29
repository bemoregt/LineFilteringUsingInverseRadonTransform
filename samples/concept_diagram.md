# Radon Transform Concept

The process of the Radon transform and its application in line filtering can be visualized as follows:

```
Original Image              Radon Transform (Sinogram)
+---------------+           +---------------+
|       |       |           |     /|\      |
|       |       |           |    / | \     |
|       |       |           |   /  |  \    |
|-------|-------|    ==>    |  /   |   \   |
|       |       |           | /    |    \  |
|       |       |           |/     |     \ |
|       |       |           +---------------+
+---------------+             Angle vs. Distance

                                   ||
                                   \/

Filtered Sinogram             Reconstructed Image
+---------------+           +---------------+
|     /|\      |           |       |       |
|    / | \     |           |       |       |
|     |        |           |       |       |
|     |        |    ==>    |-------|       |
|     |        |           |       |       |
|     |        |           |       |       |
|     |        |           |       |       |
+---------------+           +---------------+
 (After Gaussian              (Horizontal line
  mask applied)                emphasized)
```

This diagram illustrates:
1. An original image with horizontal and vertical lines
2. Its Radon transform (sinogram), showing projections at different angles
3. The application of a Gaussian mask to selectively filter specific angular components
4. The reconstructed image with enhanced horizontal lines and suppressed vertical lines

The Gaussian mask in this example is configured to preserve horizontal line information while suppressing vertical line information.
