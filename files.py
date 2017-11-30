import os
import PIL
from PIL import Image
import send2trash
import shutil

directories = os.environ['directories']

print(directories)

for directory in directories:

	# for folderName, subfolders, filenames in os.walk(directory):

	# 	# Rename all the subfolders
	# 	if ' ' in folderName:
	# 		print('Renaming {0} to >> {1}'.format(folderName, folderName.replace(' ', '_')))
	# 		os.rename(folderName, folderName.replace(' ', '_'))

	# 	for subfolder in subfolders:

	# 		# Rename all the subfolders
	# 		if ' ' in subfolder:
	# 			print('Renaming {0} to >> {1}'.format(subfolder, subfolder.replace(' ', '_')))
	# 			os.rename(folderName + '/' + subfolder, folderName + '/' + subfolder.replace(' ', '_'))

	# 	for filename in filenames:

	# 		# Rename all of the files
	# 		if ' ' in filename:
	# 			print('Renaming {0} to >> {1}'.format(filename, filename.replace(' ', '_')))
	# 			os.rename(folderName + '/' + filename, folderName + '/' + filename.replace(' ', '_'))




	for folderName, subfolders, filenames in os.walk(directory):
		print(folderName)
		if ' ' in folderName:
			print('Renaming {0} to >> {1}'.format(folderName, folderName.replace(' ', '_')))
			os.rename(folderName, folderName.replace(' ', '_'))

		for subfolder in subfolders:
			print(subfolder)
			if ' ' in subfolder:
				print('Renaming {0} to >> {1}'.format(subfolder, subfolder.replace(' ', '_')))
				os.rename(folderName + '/' + subfolder, folderName + '/' + subfolder.replace(' ', '_'))

		for filename in filenames:
			if ' ' in filename:
				print('Renaming {0} to >> {1}'.format(filename, filename.replace(' ', '_')))
				os.rename(folderName + '/' + filename, folderName + '/' + filename.replace(' ', '_'))
				filename = filename.replace(' ', '_')
			else:
				pass

			if filename.lower().endswith(('.png', '.jpg', '.jpeg')) and not filename.startswith('_'):
				print('resizing: ' + filename)
				basewidth = 900
				img = Image.open(folderName + '/' + filename)
				wpercent = (basewidth / float(img.size[0]))
				hsize = int(float(img.size[1]) * float(wpercent))
				img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
				img.save(folderName + '/' + '_' + filename,optimize=True,quality=95)
				send2trash.send2trash(folderName + '/' + filename)
			elif filename.lower().endswith('mp4') and not filename.startswith('_'):
				bash = 'ffmpeg -i {0} -acodec copy -vcodec copy -f mov {1}.mov'.format(folderName + '/' + filename, folderName + '/_' + filename)
				os.system(bash)
				send2trash.send2trash(folderName + '/' + filename)
			elif filename.lower().endswith('mov') and filename.startswith('_'):
				bash = 'ffmpeg -i {0} -c:v libx264 -crf 28 {1}'.format(folderName + '/' + filename, folderName + '/_' + filename)
				os.system(bash)
				shutil.move(folderName + '/' + filename, '/Users/test/Desktop/movies')
				# send2trash.send2trash(folderName + '/' + filename)

		print('')



