def convolve2d(image, kernel, verbose=True):
    H, W = image.shape
    k = kernel.shape[0]

    out_h = H - k + 1
    out_w = W - k + 1

    if verbose:
        print(f"Image shape: ({H}, {W})")
        print(f"Kernel shape: ({k}, {k})")
        print(f"Output shape: ({out_h}, {out_w})")
        print(f"  → That's ({H}-{k}+1, {W}-{k}+1) = ({out_h}, {out_w})")
        print(f"  → We'll compute {out_h * out_w} output pixels total")
        print()

    output = np.zeros((out_h, out_w), dtype=np.float32)

    for i in range(out_h):
        for j in range(out_w):

            # Show which patch we're looking at
            patch = image[i:i+k, j:j+k]

            if verbose:
                print(f"--- Position (i={i}, j={j}) ---")
                print(f"  Patch = image[{i}:{i+k}, {j}:{j+k}]")
                print(f"  {patch}")

            # Inner loops: element-wise multiply and accumulate
            total = 0.0
            terms = []  # collect strings for display
            for m in range(k):
                for n in range(k):
                    pixel = image[i + m, j + n]
                    weight = kernel[m, n]
                    product = pixel * weight
                    total += product
                    terms.append(f"{pixel:.0f}×{weight:.0f}={product:.0f}")

            if verbose:
                print(f"  Products: {', '.join(terms)}")
                print(f"  Sum = {total:.0f}")
                print()

            output[i, j] = total
            break

    return output