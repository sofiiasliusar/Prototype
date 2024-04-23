# https://www.geeksforgeeks.org/build-an-image-swiper-app-for-kivymd-in-python/
#  importing packages 
from kivymd.app import MDApp 
from kivy.lang.builder import Builder 
from kivy.core.window import Window 

# adjusting window size 
Window.size = (800, 700) 

# writing kv language 
kv = ''' 


<swiper@MDSwiperItem> 
	
	# loads image 
	FitImage: 
		source: "5.png" 
		radius: [20,] 

# creating screen 
MDScreen: 
	
	# defining MDSwiper 
	MDSwiper: 
		
		# calling MDSwiperItems 
		MDSwiperItem: 
			FitImage: 
				source:"5.png" 
				radius: [20,0] 

'''

# app class 


class Trial(MDApp): 

	def build(self): 
		# this will load kv language 
		screen = Builder.load_string(kv) 

		# returning screen 
		return screen 


# running app 
Trial().run() 
