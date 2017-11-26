from PIL import Image
import numpy as np

# 이미지 데이터를 Averages Hash로 변환 함수 선언
def average_hash(fname, size = 16): 
      img = Image.open(fname) 
      img = img.convert('L')  
      img = img.resize((size, size), Image.ANTIALIAS) 
      pixel_data = img.getdata() 
      pixels = np.array(pixel_data) 
      pixels = pixels.reshape((size, size)) 
      avg = pixels.mean() 
      diff = 1*(pixels>avg)
      return diff


# 이전 해시로 변환하는 함수 선언
def np2hash(n):
      bhash = []
      for n1 in ahash.tolist():
            s1 = [str(i) for i in n1]
            s2 = "".join(s1)
            i = int(s2,2) 
            bhash.append("%04x"%i)
      return "".join(bhash)

# Average Hash 출력하기
avhash_1 = average_hash('python.png')
avhash_2 = average_hash('python2.png')
a = avhash_1.reshape(1,-1) 
b = avhash_2.reshape(1,-1)
print((a == b)) 
print('\n',(a != b).sum()) 
