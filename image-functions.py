import os
from PIL import Image
from PIL import ImageFilter

def validate_image_path(image_path):
	return 1 if os.path.isfile(image_path) else 0		

def get_image_information(image_url):
	im = Image.open(image_url)
	print("Format:",im.format)
	print("Size:",im.size)
	print("Mode:",im.mode)
	im.close()

def black_white_image(image_url):
	im=Image.open(image_url)
	try:
		gray_scale=im.convert("L")
		img_path, img_name = os.path.split(image_url)
		gray_scale.save(img_path+"/bw_img.jpg")
		print("Image has been transformed in gray scale.")
	except:
		print("There was some error in processing the image.")
	finally:	
		im.close()	

def contour_image(image_url):
	im=Image.open(image_url)
	try:
		img_path, img_name = os.path.split(image_url)
		filtered_image=im.filter(ImageFilter.CONTOUR)
		filtered_image.save(img_path+"/contour.jpg")
		print("Image has been transformed.")
	except:
		print("There was some error in processing the image.")
	finally:	
		im.close()	

def transpose_image(image_url):
	im=Image.open(image_url)
	try:
		img_path, img_name = os.path.split(image_url)
		transposed_img=im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
		transposed_img.save(img_path+"/transposed.jpg")
		print("Image has been transformed.")
	except:
		print("There was some error in processing the image.")
	finally:	
		im.close()

def crop_image(image_url):
	im=Image.open(image_url)
	try:
		img_path, img_name = os.path.split(image_url)
		width, height = im.size
		area = (0, 0, width/2, height/2)
		image = im.crop(area)
		image.save(img_path+"/cropped_picture.jpg")
		print("Image has been cropped.")
	except:
		print("There was some error in processing the image.")
	finally:	
		im.close()	

def main():
	print("Welcome to the images functions.")
	print("Please choose the numbers showes for each functions.")
	print("1. Please enter 1 to get the image imformation.")
	print("2. Please enter 2 to black and white the image.")
	print("3. Please enter 3 to countour the image.")
	print("4. Please enter 4 to rotate the image.")
	print("5. Please enter 5 to crop the image.")
	response=int(input("Please enter the number:"))

	if response:
		response_img=input("Please enter the full path:")
		if validate_image_path(response_img):
			if response == 1:
				get_image_information(response_img)
			elif response == 2:
				black_white_image(response_img)
			elif response == 3:
				contour_image(response_img)
			elif response == 4:
				transpose_image(response_img)
			elif response == 5:
				crop_image(response_img)			
			else:
				print("It seems the entered input is out of range.")		
		else:
			print("It seems we can not find the image. Please enter the valid path.")	
	


if __name__ == '__main__':
	main()	