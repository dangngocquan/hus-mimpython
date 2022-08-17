import cv2

if __name__ == '__main__':
    # Read image from "additionalFolder\\assigment02\\dietMoonCake.jpg"
    img = cv2.imread(".\\week06_student42_DangNgocQuan\\additionalFolder\\assigment02\\dietMoonCake.jpg", 1)
    (h, w, d) = img.shape
    
    # Resize image
    img1 = img[0:h-h%2, 0:w-w%2]
    (h1, w1, d1) = img1.shape
    
    # Crop image
    imagesCrop = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append(img1[h1//2*i:h1//2*(i+1), w1//2*j:w1//2*(j+1)])
        imagesCrop.append(row)
    
    # Concatenate images
    img2 = cv2.vconcat([
        cv2.hconcat([imagesCrop[0][1], imagesCrop[1][1]]),
        cv2.hconcat([imagesCrop[0][0], imagesCrop[1][0]])
    ])
    
    # Save image at "additionalFolder\\assigment02\\dietMoonCake2.jpg"
    cv2.imwrite(".\\week06_student42_DangNgocQuan\\additionalFolder\\assigment02\\dietMoonCake2.jpg", img2)