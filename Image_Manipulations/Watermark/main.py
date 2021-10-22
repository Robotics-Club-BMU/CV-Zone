import cv2


def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    """
    :param src: Input Color Background Image
    :param overlay: transparent Image (BGRA)
    :param pos:  position where the image to be blit.
    :param scale : scale factor of transparent image.
    :return: Resultant Image
    """
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image

    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + \
                (1 - alpha) * src[x + i][y + j]
    return src


def addImageWatermark(logo_image, main_image, opacity, pos=(10, 100),):
    opacity = opacity / 100

    original_image = cv2.imread(main_image, -1)
    water_image = cv2.imread(logo_image, -1)

    temp_image = original_image.copy()
    print(temp_image.shape)

    overlay = transparentOverlay(temp_image, water_image, pos)
    output = original_image.copy()
    # apply the overlay
    cv2.addWeighted(overlay, opacity, output, 1 - opacity, 0, output)

    cv2.imshow('Watermark on Image', output)
    cv2.imwrite('watermarked.jpg', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    addImageWatermark('watermark.png', 'park.jpg', 100, (10, 100))
