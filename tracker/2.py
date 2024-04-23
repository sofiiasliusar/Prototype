# importing packages 
from kivymd.app import MDApp 
from kivy.lang.builder import Builder 
from kivy.core.window import Window 

# adjusting window size 
Window.size = (800, 700) 

# writing kv language 
kv = ''' 

# creating screen 
MDScreen: 
	
	# defining MDSwiper 
	MDSwiper: 
		
		# defining items for swiper 
		MDSwiperItem: 
			FitImage: 
				source:"4.jpg" 
				radius: [20,0] 
		
		# defining items for swiper 
		MDSwiperItem: 
			FitImage: 
				source:"5.png" 
				radius: [20,0] 
				
		# defining items for swiper 
		MDSwiperItem: 
			FitImage: 
				source:"6.jpg" 
				radius: [20,0] 
'''

# app class 


class Main(MDApp): 

	def build(self): 
		# this will load kv language 
		screen = Builder.load_string(kv) 

		# returning screen 
		return screen 


# running app 
Main().run() 
