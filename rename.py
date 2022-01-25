import os, cv2

def rename():
    max = 0
    for file in os.listdir('Photos'):
        f = int(file.replace('.jpg',''))
        if f>max: max = f
    print(max)

    for i, name_i in enumerate(os.listdir('PhotosLoadingDock')):
        name_f = '0'*(4-len(str(i+max+1)))+str(i+max+1)+'.jpg'
        src = 'PhotosLoadingDock/' + name_i
        name_f = 'Photos/' + name_f
        os.rename(src,name_f)

def doubleImgSet():
    max = 0
    for file in os.listdir('Photos'):
        f = int(file.replace('.jpg',''))
        if f>max: max = f
    print(max)

    for i in range(max):
        img = cv2.imread('Photos/{}.jpg'.format('0'*(4-len(str(i)))+str(i)))
        img_flipped = cv2.flip(img,1)
        path = 'C:/Users/Sophia/Desktop/LitterBotCleanTests/Photos/{}.jpg'.format(str('0'*(4-len(str(i+max+1)))+str(i+max+1)))
        cv2.imwrite(path, img_flipped)
        print('0'*(4-len(str(i+max+1)))+str(i+max+1))

rename()
doubleImgSet()
