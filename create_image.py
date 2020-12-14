from PIL import Image
 
img = Image.new('RGB', (600, 300), color = 'red')
img.save('sample_image.png')