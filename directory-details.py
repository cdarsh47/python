from pathlib import Path
import os

def update_extension(content,files_types):

	extension=os.path.splitext(content)
	
	final_ex=extension[1][1:]
	
	if final_ex not in files_types:
	
		files_types[final_ex]=1
	
	else:
	
		files_types[final_ex]=files_types[final_ex]+1	

def process_directory(path):

	dir_list=os.listdir(path)

	directory_count,file_count,max_size=0,0,0
	
	files_types={}

	if os.path.isdir(path):
	
		print("=================================================")
		print("Here are the details of the given directory path:")
		print("=================================================")

		for content in dir_list:

			fullpath=path+'/'+content

			if os.path.isdir(fullpath):
			
				print("#########################")
				
				pline=f"Directory name:"+content
				
				print(pline.center(25,'-'))
				
				print("#########################")
				
				directory_count+=1

				print("====================================")

				print("Files list within the directory:",content)

				print("====================================")

				print("============== **** =================")

				for ifiles in os.listdir(fullpath):

					if os.path.isdir(ifiles):
					
						print("----> directory name:",ifiles)
					
						directory_count+=1
					
					else:
					
						size=str(os.path.getsize(fullpath))
				
						if int(size)>int(max_size):max_name=ifiles

						max_size = size if int(size)>int(max_size) else max_size	

						print(f"FileName : {ifiles} ---- Size : {size} bytes \n")
				
						update_extension(ifiles,files_types)
				
						file_count+=1
				print("============== **** =================")						

			else:
				size=str(os.path.getsize(fullpath))
				
				if int(size)>int(max_size):max_name=content
				
				max_size = size if int(size)>int(max_size) else max_size
				
				print(f"FileName : {content} ---- Size : {size} bytes \n")
				
				update_extension(content,files_types)
				
				file_count+=1

	return 	files_types,max_name,max_size,directory_count,file_count

def main():

	response=input("Please enter the full directory path:")

	if response and os.path.isdir(response):
	
		files_types,max_name,max_size,directory_count,file_count = process_directory(response)
	
		print("=======================================================")
		print("==========  Directory Information  ==============")
		print("=======================================================")
		print(" ------> Total no. of folders:",directory_count)
		
		print(" ------> Total no. of files:",file_count)

		print("=======================================================")
		
		print(f"The file \"{max_name}\" has a maximum file size of {max_size} bytes")
		
		print("=======================================================")

		print("======> The file counts based on the extensions: <======")
		
		for file_type,occurance in files_types.items():
			print("--> {o} {f} files".format(f=file_type,o=occurance))

	else:
		print("Seems there is no directory or we are unable to collect!!")		

if __name__ == '__main__':
	main()
