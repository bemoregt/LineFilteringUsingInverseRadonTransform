# Mathematical Foundation of Radon Transform and Inverse Radon Transform

This document provides a deeper understanding of the mathematical principles behind the Radon transform and its inverse, which are fundamental to the line filtering application.

## The Radon Transform

The Radon transform maps a function f(x,y) defined in the Cartesian plane to a function Rf(ρ,θ) in the two-dimensional space of lines in the plane, parameterized by (ρ,θ).

### Definition

For a continuous function f(x,y), the Radon transform is defined as:

```
Rf(ρ,θ) = ∫∫ f(x,y) δ(ρ - x·cos(θ) - y·sin(θ)) dx dy
```

Where:
- ρ is the perpendicular distance from the origin to the line
- θ is the angle of the line with respect to the y-axis
- δ is the Dirac delta function

### Interpretation

The Radon transform Rf(ρ,θ) represents the line integral of the function f along the line defined by parameters (ρ,θ). In the context of image processing:

- f(x,y) is the image intensity at point (x,y)
- Rf(ρ,θ) is the projection (sum of intensities) along the line perpendicular to the vector (cos(θ), sin(θ)) at distance ρ from the origin

### Sinogram

The result of applying the Radon transform to an image is a sinogram, where:
- The horizontal axis represents the angle θ (typically from 0° to 180°)
- The vertical axis represents the distance ρ
- The intensity value at each point (ρ,θ) represents the line integral along the corresponding line

## The Inverse Radon Transform

The inverse Radon transform reconstructs the original function f(x,y) from its Radon transform Rf(ρ,θ).

### Filtered Back Projection (FBP)

The most common approach to compute the inverse Radon transform is the filtered back projection method:

```
f(x,y) = ∫₀^π Q(x·cos(θ) + y·sin(θ), θ) dθ
```

Where Q(ρ,θ) is the filtered projection defined as:

```
Q(ρ,θ) = ∫₋∞^∞ Rf(s,θ) h(ρ-s) ds
```

Here, h(ρ) is a filter function typically implemented as a ramp or Ram-Lak filter in the frequency domain.

### Frequency Domain Interpretation

The Fourier Slice Theorem provides an alternative way to understand the Radon transform:

1. The 1D Fourier transform of a projection at angle θ equals the slice at angle θ of the 2D Fourier transform of the original image.
2. By collecting these slices for all angles, we can reconstruct the 2D Fourier transform of the image.
3. An inverse 2D Fourier transform then yields the original image.

## Gaussian Filtering in Sinogram Domain

In our application, we apply a Gaussian mask to the sinogram before performing the inverse Radon transform:

```
Filtered_Sinogram(ρ,θ) = Rf(ρ,θ) × G(ρ,θ)
```

Where G(ρ,θ) is a 2D Gaussian function:

```
G(ρ,θ) = 1 - exp(-((θ-θ₀)² + (ρ-ρ₀)²)/(2σ²))
```

The parameters:
- (ρ₀,θ₀) define the center of the region we want to preserve
- σ controls the width of the Gaussian (larger σ means a wider region is preserved)
- The "1-exp(...)" formulation ensures that the mask preserves the targeted region while attenuating others

This filtering selectively preserves or enhances linear features at specific orientations while suppressing others.

## Implementation in the Code

In the application code, these mathematical principles are implemented as:

1. The Radon transform is computed using scikit-image's `radon()` function
2. A Gaussian mask is applied to the resulting sinogram
3. The inverse Radon transform is computed using `iradon()` function

The parameters in the code:
- `x_center, y_center = 239, 214` define the center of the Gaussian mask
- `sigma = 20` defines the width of the Gaussian
- The mask is applied as `sinogram = sinogram * mask`

By adjusting these parameters, users can control which linear features are preserved or enhanced in the reconstructed image.
