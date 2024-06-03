
from kivy.core.text import Label
 
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.button import MDIconButton, MDFloatingActionButton, MDFillRoundFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import MDList, OneLineAvatarIconListItem
from kivymd.uix.gridlayout import MDGridLayout 
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import platform
from jnius import autoclass
from kivy.uix.image import Image

KV = '''
ScreenManager:
  id: screen_manager
 
  ScreenOne:
    id: "home"
    name: "home"
 
  ScreenTwo:
    id: "second"
    name: "second"
 
  ScreenThree:
    id: "third"
    name: "third"
    
  ScreenForth:
    id: "forth"
    name: "forth"
 
<ScreenOne>:
  MDScreen:
 
    MDBoxLayout:
      orientation: "vertical"
 
      MDTopAppBar:
        left_action_items: [["menu", lambda x: x]]
 
      MDBoxLayout:
        MDFloatingActionButton:
          icon: "pencil"
          on_press: app.root.current = "second"
          pos_hint: {"center_x": 0.9, "center_y": 0.1}
 
<ScreenTwo>:
  MDScreen:
 
    MDBoxLayout:
      orientation: "vertical"
      id: g_two
      
      MDBoxLayout:
        size_hint_y: 0.1
        
        
        
        MDIconButton:
          icon: "arrow-left"
          on_press: app.root.current = "home"
        MDLabel:
          text: "     kirAwnw "
          font_name: "AmrLipiHeavy"
          pos_hint: {'center_x': 0.8,'center_y': 0.5}
 
 
      MDBoxLayout:
        orientation: "vertical"
        id: left
        
 
        ScrollView:
          do_scroll_x: False
 
          
              
          MDList:
            id: grocery
            
            
            OneLineAvatarIconListItem:
              MDLabel:
                id:a
                text: "KMf"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: aa
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:b
                text: "golfn sylw col"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:bb
                
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:c
                text: "nmk pYkt"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: cc
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:d
                text: "qyl"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:dd
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:e
                text: "iGE"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: ee
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:f
                text: "vysx"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: ff
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:g
                text: "mYdw"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: gg
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:h
                text: "Awtw"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: hh
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:i
                text: "rPYNf"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: ii
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:j
                font_name: "AmrLipiHeavy"
                text: "ikcnikMg f`bI"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:jj
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:k
                text: "cwtmswlw f`bI"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:kk
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:l
                text: "dygIimrc f`bI"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:ll
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:m
                text: "jvYx"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:mm
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:n
                text: "zIrw"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:nn
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:o
                text: "qyj p`qw"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: oo
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:p
                text: "sONP"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:pp
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:q
                text: "hldI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: qq
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:r
                text: "ic`ty Coly"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: rr
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:s
                text: "kwly Coly"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: ss
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:t
                text: "lwl imrc"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: tt
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:u
                text: "ihNg"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: uu
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:v
                font_name: "AmrLipiHeavy"
                text: "Anwrdwxw pIisAW"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:vv
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:W
                text: "dwlm`KxI mswlw f`bI"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:WW
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:y
                text: "lONg"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: yy
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:z
                text: "CotI lwcI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:zz
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ab
                text: "sUjI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: abb
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ac
                text: "dwl cInI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: acc
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ad
                text: "iemlI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: add
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ae
                text: "Arwrot"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: aee
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:af
                text: "im`Tw sofw"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: aff
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ag
                font_name: "AmrLipiHeavy"
                text: "mUMgI DoqI"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:agg
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ah
                text: "vnIlw kstf f`bI"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:ahh
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              MDLabel:
                id:ai
                text: "rMgkwt"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: aii
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:aj
                text: "pOxy/ purwxy k`pVy"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:ajj
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ak
                text: "ieSt"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: akk
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:al
                text: "stIl vUl/swbx"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: all
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:am
                text: "DnIAw pIisAw"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: amm
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:an
                text: "cnwmswlw f`bI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: ann
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ao
                text: "SwhIpnIrmswlw f`bI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: aoo
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ap
                font_name: "AmrLipiHeavy"
                text: "ksUrImyQI f`bI"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:apa
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:aq
                text: "grmmswlw f`bI"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:aqq
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ar
                text: "sONgI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: arr
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:sa
                text: "kwjU"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:ass
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:at
                text: "bdwm"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: att
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:au
                text: "rwjmwh"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: auu
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:av
                text: "msr"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: avv
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:aw
                text: "moTw dI dwl"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: aww
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ax
                text: "ColyAW dI dwl"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: axx
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ay
                text: "swbq mUMgI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:ayy
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:az
                text: "jIrw pwaUfr f`bI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: azz
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:ba
                text: "DnIAw pwaUfr f`bI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: baa
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:bc
                text: "lwl rMg"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: bcc
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:bd
                text: "dyg vwsty awta"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: bdd
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:be
                text: "inMbU dw s`t"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: bee
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:bf
                font_name: "AmrLipiHeavy"
                text: "byikMg pwaUfr f`bI"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:bff
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              TextInput:
                id:bg
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:bgg
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:bh
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:bhh
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:bi
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:bii
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:bj
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:bjj
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:bk
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:bkk
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:bl
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:bll
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
      MDBoxLayout:
        size_hint_y: 0.1
        orientation: 'vertical'
        MDBoxLayout:
          orientation: 'horizontal'
          pos_hint: {'center_x': 0.9,'center_y': 0.5}
          
          MDRaisedButton:
            text: "Save"
            on_press: app.printthing()
            pos_hint: {'center_x': 0.9,'center_y': 0.5}
          
            
           
       
          
          MDRaisedButton:
            text: 'Next'
            on_press: app.root.current = "third"
            pos_hint: {'center_x': 0.9,'center_y': 0.5}
          
          
           
        
          
        
<ScreenThree>:
  MDScreen:
 
    MDBoxLayout:
      orientation: "vertical"
      MDBoxLayout:
        size_hint_y: 0.1
        
        
        
        
        MDIconButton:
          icon: "arrow-left"
          on_press: app.root.current = "second"
        MDLabel:
          text: "    sbzIAw"
          pos_hint: {'center_x': 0.8,'center_y': 0.5}
          font_name: "AmrLipiHeavy"
 
 
 
      
 
      MDBoxLayout:
        orientation: "vertical"
 
        ScrollView:
          do_scroll_x: False
 
          
              
          MDList:
            id: vegetables
            
            
            
            OneLineAvatarIconListItem:
              MDLabel:
                id:a
                text: "ipAwz"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: aa
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:b
                text: "tmwtr"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:bb
                
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:c
                text: "Adrk"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: cc
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:d
                text: "lsx"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:dd
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:e
                text: "hrI imrc"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: ee
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:f
                text: "hrw DnIAw"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: ff
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:g
                text: "gobI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: gg
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:h
                text: "iSmlw imrc"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: hh
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:i
                text: "mSrUm"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: ii
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:j
                font_name: "AmrLipiHeavy"
                text: "mtr"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:jj
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:k
                text: "gwjr"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:kk
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:l
                text: "AwlU"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:ll
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:m
                text: "KIrw"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:mm
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:n
                text: "ickMdr"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
                font_name: "AmrLipiHeavy"
              TextInput:
                id:nn
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:o
                text: "mUlI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: oo
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
 
            OneLineAvatarIconListItem:
              MDLabel:
                id:p
                text: "pwlk"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id:pp
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              MDLabel:
                id:q
                text: "iBMfI"
                font_name: "AmrLipiHeavy"
                pos_hint: {'center_x': 0.5, 'top': 1.0} 
 
              TextInput:
                id: qq
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
            OneLineAvatarIconListItem:
              TextInput:
                id:r
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:rr
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:s
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:ss
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:t
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:tt
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:u
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:uu
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:v
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:vv
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:W
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:WW
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:y
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:yy
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8}
            OneLineAvatarIconListItem:
              TextInput:
                id:z
                size_hint_x: 0.53
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.299, 'top': 0.8}  
 
              TextInput:
                id:zz
        
                size_hint_x: 0.35
                size_hint_y: 0.5
                pos_hint: {'center_x': 0.75, 'top': 0.8} 
      MDBoxLayout:
        size_hint_y: 0.1
        orientation: 'vertical'
        MDBoxLayout:
          orientation: 'horizontal'
          pos_hint: {'center_x': 0.9,'center_y': 0.5}
          
          MDRaisedButton:
            text: "Save"
            on_press: app.listing()
            pos_hint: {'center_x': 0.9,'center_y': 0.5}
          
            
           
       
          
          MDRaisedButton:
            text: 'Next'
            on_press: app.root.current = "forth"
            pos_hint: {'center_x': 0.9,'center_y': 0.5}


<ScreenForth>:
  MDScreen:
    
    MDBoxLayout:
      orientation: 'vertical'
      MDBoxLayout:
        size_hint_y: 0.1
        
        
        
        MDIconButton:
          icon: "arrow-left"
          on_press: app.backscreen()
        MDLabel:
          text: "         Finallist "
          pos_hint: {'center_x': 0.8,'center_y': 0.5}
 
 
 
      
      
      MDBoxLayout:
        orientation: "horizontal"
        MDBoxLayout:
          id: leftpart
          orientation: "vertical"
          
          
          MDLabel:
            id:hin
            text: ""
            markup: True
            pos_hint: {'center_x': 0.5, 'top': 0.7}
            font_size: "9sp"
            
            
          
        MDBoxLayout:
          orientation: "vertical"
          id: rightpart
          size_hint_x: 0.8
          
          MDLabel:
            id: sim
            text:""
            font_size: "9sp"
            markup: True
            
      
      MDBoxLayout:
        size_hint_y: 0.1
        orientation: 'vertical'
        MDBoxLayout:
          orientation: 'horizontal'
          pos_hint: {'center_x': 0.9,'center_y': 0.5}
          
          
          
          MDRaisedButton:
            text: "PRINT"
            
            on_press: app.capture()
            pos_hint: {'center_x': 0.9,'center_y': 0.5}
          
          
           
       
          
          
        
      
        
 
'''
 
class ScreenOne(Screen):
    pass
 
class ScreenTwo(Screen):
    value_list=[]
    name_list=[]
    
    
    
    
 
class ScreenThree(Screen):
  
    value_list=[]
    name_list=[]
    
    
class ScreenForth(Screen):
  
    pass
 
class YourContainer(IRightBodyTouch, MDBoxLayout):
    pass
 
class EasyListerApp(MDApp):
    def listing(self):
        third= self.root.get_screen("third")
        text= third.ids.bb.text
        label= third.ids.b.text
        a= third.ids.aa.text
        b= third.ids.a.text
        cc=third.ids.cc.text
        c=third.ids.c.text
        dd=third.ids.dd.text
        d=third.ids.d.text
        ee=third.ids.ee.text
        e=third.ids.e.text
        ff=third.ids.ff.text
        f=third.ids.f.text
        gg=third.ids.gg.text
        g=third.ids.g.text
        hh=third.ids.hh.text
        h=third.ids.h.text
        ii=third.ids.ii.text
        i=third.ids.i.text
        jj=third.ids.jj.text
        j=third.ids.j.text
        kk=third.ids.kk.text
        k=third.ids.k.text
        ll=third.ids.ll.text
        l=third.ids.l.text
        mm=third.ids.mm.text
        m=third.ids.m.text
        nn=third.ids.nn.text
        n=third.ids.n.text
        o= third.ids.o.text
        oo= third.ids.oo.text
        p= third.ids.p.text
        pp= third.ids.pp.text
        q=third.ids.q.text
        qq=third.ids.qq.text
        r=third.ids.r.text
        rr=third.ids.rr.text
        s=third.ids.s.text
        ss=third.ids.ss.text
        t=third.ids.t.text
        tt=third.ids.tt.text
        u=third.ids.u.text
        uu=third.ids.uu.text
        v=third.ids.v.text
        vv=third.ids.vv.text
        W=third.ids.W.text
        WW=third.ids.WW.text
        y=third.ids.y.text
        yy=third.ids.yy.text
        z=third.ids.z.text
        zz=third.ids.zz.text
        
        
        value_data=[text,a,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,WW,yy,zz]
        name_data=[label,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,W,y,z,]
        
        forth = self.root.get_screen("forth")
        forth.ids.sim.text = ""
        
        for i in range(len(value_data)):
          if value_data[i] and (value_data[i]) != 0 :
            if  name_data[i] not in third.name_list:
              third.value_list.append(value_data[i])
              third.name_list.append(name_data[i])

        for i in range(len(third.value_list)):
          formatted_text=f"{i+1}. [font=AmrLipiHeavy]{third.name_list[i]} [/font]{third.value_list[i]}"
          
          forth = self.root.get_screen("forth")

   
          
          
          
          forth= self.root.get_screen("forth")
          
          forth.ids.sim.text += formatted_text + "\n"
           

        
      
    def printthing(self):
        second= self.root.get_screen("second")
        
        text= second.ids.bb.text
        label= second.ids.b.text
        a= second.ids.aa.text
        b= second.ids.a.text
        cc=second.ids.cc.text
        c=second.ids.c.text
        dd=second.ids.dd.text
        d=second.ids.d.text
        ee=second.ids.ee.text
        e=second.ids.e.text
        ff=second.ids.ff.text
        f=second.ids.f.text
        gg=second.ids.gg.text
        g=second.ids.g.text
        hh=second.ids.hh.text
        h=second.ids.h.text
        ii=second.ids.ii.text
        i=second.ids.i.text
        jj=second.ids.jj.text
        j=second.ids.j.text
        kk=second.ids.kk.text
        k=second.ids.k.text
        ll=second.ids.ll.text
        l=second.ids.l.text
        mm=second.ids.mm.text
        m=second.ids.m.text
        nn=second.ids.nn.text
        n=second.ids.n.text
        o= second.ids.o.text
        oo= second.ids.oo.text
        p= second.ids.p.text
        pp= second.ids.pp.text
        q=second.ids.q.text
        qq=second.ids.qq.text
        r=second.ids.r.text
        rr=second.ids.rr.text
        s=second.ids.s.text
        ss=second.ids.ss.text
        t=second.ids.t.text
        tt=second.ids.tt.text
        u=second.ids.u.text
        uu=second.ids.uu.text
        v=second.ids.v.text
        vv=second.ids.vv.text
        W=second.ids.W.text
        WW=second.ids.WW.text
        y=second.ids.y.text
        yy=second.ids.yy.text
        z=second.ids.z.text
        zz=second.ids.zz.text
        ab= second.ids.ab.text
        abb= second.ids.abb.text
        acc=second.ids.acc.text
        ac=second.ids.ac.text
        add=second.ids.add.text
        ad=second.ids.ad.text
        aee=second.ids.aee.text
        ae=second.ids.ae.text
        aff=second.ids.aff.text
        af=second.ids.af.text
        agg=second.ids.agg.text
        ag=second.ids.ag.text
        ahh=second.ids.ahh.text
        ah=second.ids.ah.text
        aii=second.ids.aii.text
        ai=second.ids.ai.text
        ajj=second.ids.ajj.text
        aj=second.ids.aj.text
        akk=second.ids.akk.text
        ak=second.ids.ak.text
        all=second.ids.all.text
        al=second.ids.al.text
        amm=second.ids.amm.text
        am=second.ids.am.text
        ann=second.ids.ann.text
        an=second.ids.an.text
        ao= second.ids.abb.text
        aoo= second.ids.ab.text
        ap= second.ids.ap.text
        apa= second.ids.apa.text
        aq=second.ids.aq.text
        aqq=second.ids.aqq.text
        ar=second.ids.ar.text
        arr=second.ids.arr.text
        sa=second.ids.sa.text
        ass=second.ids.ass.text
        at=second.ids.at.text
        att=second.ids.att.text
        au=second.ids.au.text
        auu=second.ids.auu.text
        av=second.ids.av.text
        avv=second.ids.avv.text
        aw=second.ids.aw.text
        aww=second.ids.aww.text
        ax=second.ids.ax.text
        axx=second.ids.axx.text
        ay=second.ids.ay.text
        ayy=second.ids.ayy.text
        az=second.ids.az.text
        azz=second.ids.azz.text
        ba= second.ids.ba.text
        baa= second.ids.baa.text
        bcc=second.ids.bcc.text
        bc=second.ids.bc.text
        bdd=second.ids.bdd.text
        bd=second.ids.bd.text
        bee=second.ids.bee.text
        be=second.ids.be.text
        bff=second.ids.bff.text
        bf=second.ids.bf.text
        bgg=second.ids.bgg.text
        bg=second.ids.bg.text
        bhh=second.ids.bhh.text
        bh=second.ids.bh.text
        bii=second.ids.bii.text
        bi=second.ids.bi.text
        bjj=second.ids.bjj.text
        bj=second.ids.bj.text
        bkk=second.ids.bkk.text
        bk=second.ids.bk.text
        bll=second.ids.bll.text
        bl=second.ids.bl.text
        
        
        value_data=[text,a,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,WW,yy,zz,abb,acc,add,aee,aff,agg,ahh,aii,ajj,akk,all,amm,ann,ao,apa,aqq,arr,ass,att,auu,avv,aww,ayy,azz,baa,bcc,bdd,bee,bff,bgg,bhh,bii,bjj,bkk,bll]
        name_data=[label,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,W,y,z,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,aoo,ap,aq,ar,sa,at,au,av,aw,ay,az,ba,bc,bd,be,bf,bg,bh,bi,bj,bk,bl]
        
        forth = self.root.get_screen("forth")
        forth.ids.hin.text = ""
        
        for i in range(len(value_data)):
          if value_data[i] and (value_data[i]) != 0 :
            if  name_data[i] not in second.name_list:
              second.value_list.append(value_data[i])
              second.name_list.append(name_data[i])

        for i in range(len(second.value_list)):
          formatted_text=f"{i+1}. [font=AmrLipiHeavy]{second.name_list[i]} [/font]{second.value_list[i]}"
          
          forth = self.root.get_screen("forth")

   
          
          
          
          forth= self.root.get_screen("forth")
          
          forth.ids.hin.text += formatted_text + "\n"
          

    def backscreen(self,*args):
      
      forth = self.root.get_screen("forth")
      forth.ids.hin.text = ""
      self.root.current = 'third'
      
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
        screen = Builder.load_string(KV)
        LabelBase.register(name='AmrLipiHeavy', fn_regular='AmrLipiHeavy Regular.ttf')
        return screen
    
       
    def switchscreen(self,*args):
      self.root.current = 'third'
    def switch(self,*args):
      self.root.current = 'forth'
      
    
    def capture(self):
        screenshot_path = '/sdcard/DCIM/forth_screenshot.png'
        Window.screenshot(name=screenshot_path)

        if platform == 'android':
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            String = autoclass('java.lang.String')

            intent = Intent()
            intent.setAction(Intent.ACTION_SEND)
            intent.putExtra(Intent.EXTRA_TEXT, String('Created List'))
            intent.setType('image/*')

            gallery_path = '/sdcard/DCIM/' + screenshot_path
            Image(screenshot_path).save(gallery_path)

            chooser = Intent.createChooser(intent,String('Share via'))
            PythonActivity.mActivity.startActivity(chooser)

      
      
    
      
      
    
if __name__ == "__main__":   
      
 
  EasyListerApp().run()


