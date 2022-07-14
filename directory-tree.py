import os

class show_directory:

	def __init__(self,main_dir):

		self.main_dir=main_dir

		self.pipe,self.space_var="||","----"

		self.level,self.parent_dir,self.tree_limit=1,0,10

	def tree_level(self,fullpath):

		i=0

		while 1:

			parts=fullpath

			parts=os.path.split(parts)

			if parts[1]==self.parent_dir:

				break

			else:

				fullpath=parts[0]

			i+=1

		return i+1

	def list_subdirectories(self,fullpath):

		tree_level=self.tree_level(os.path.abspath(fullpath))

		for internal_files in os.listdir(fullpath):

			if tree_level > self.tree_limit:

				break

			print(self.pipe,self.space_var*tree_level,internal_files)

			sub_fullpath=fullpath+'/'+internal_files

			if os.path.isdir(sub_fullpath):

				self.list_subdirectories(sub_fullpath)

	def list_directories(self):

		self.parent_dir = os.path.basename(self.main_dir)

		print("=============================")

		print("====== Directory Tree ======")

		print("=============================")

		print(self.parent_dir,"(Main Directory)")

		dir_list=os.listdir(self.main_dir)

		for content in dir_list:

			print(self.pipe,self.space_var*self.level,content)

			fullpath=self.main_dir+'/'+content

			if os.path.isdir(fullpath):

				self.list_subdirectories(fullpath)

def main():

	parent_directory=input("Please enter the full directory path:")

	if parent_directory and os.path.isdir(parent_directory):

		tree_object=show_directory(parent_directory)

		tree_object.list_directories()

	else:

		print("Please enter a proper path.")

if __name__ == "__main__":
	main()