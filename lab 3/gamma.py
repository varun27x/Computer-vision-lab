import cv2
import numpy as np

def adjust_gamma(image, gamma=1.0):

    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)]).astype("uint8")

    return cv2.LUT(image, table)

def main():

    image_path = input("Enter the path to your image: ")
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return


    gamma_values = [0.4, 1.0, 2.5]

    for gamma in gamma_values:
        corrected = adjust_gamma(image, gamma=gamma)
        window_name = f"Gamma: {gamma}"
        cv2.imshow(window_name, corrected)
        print(f"Displayed image with gamma = {gamma}. Press any key to continue...")
        cv2.waitKey(0)
        cv2.destroyWindow(window_name)

    print("All gamma variations displayed. Program finished.")

if __name__ == "__main__":
    main()