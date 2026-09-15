from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


KV = '''
ScreenManager:
    HomeScreen:
    SearchScreen:
    FacilitiesScreen:
    LibraryScreen:
    ComputerLabScreen:
    CampusMapScreen:    
    AboutScreen:


<HomeScreen>:
    name: "home"

    canvas.before:
        Color:
            rgba: 0.95, 1, 0.95, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        spacing: 10
        padding: 20

        Image:
            source: "logo.jpg"
            size_hint: (1, 0.45)
            allow_stretch: True
            keep_ratio: True

        Label:
            text: "NORMI DEEN CAMPUS NAVIGATION"
            font_size: 40
            size_hint_y: None
            heght: 55
            bold: True
            color: 0, 0.5, 0.2, 1

        Button:
            text: "Start Navigation"
            font_size: 22
            size_hint_y: None
            height: 100
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "search"

        Button:
            text: "About"
            font_size: 22
            size_hint_y: None
            height: 100
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "about"


<SearchScreen>:
    name: "search"

    canvas.before:
        Color:
            rgba: 0.95, 1, 0.95, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        spacing: 10
        padding: 20

        Label:
            text: "Choose Destination"
            font_size: 26
            color: 0, 0.5, 0.2, 1

        TextInput:
            hint_text: "Search destination..."
            size_hint_y: None
            height: 50

        Button:
            text: "Facilities"
            font_size: 22
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "facilities"

        Button:
            text: "Research Papers"
            font_size: 22
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1

        Button:
            text: "Campus Map"
            font_size: 22
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "CampusMap"

        Button:
            text: "Category 4"
            font_size: 22
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1

        Button:
            text: "Back"
            font_size: 20
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "home"


<FacilitiesScreen>:
    name: "facilities"

    canvas.before:
        Color:
            rgba: 0.95, 1, 0.95, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        spacing: 10
        padding: 20

        Label:
            text: "Campus Facilities"
            font_size: 40
            color: 0, 0.5, 0.2, 1

        Button:
            text: "Library"
            font_size: 22
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "library"

        Button:
            text: "Computer Laboratory"
            font_size: 22
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "computer_lab"

        Button:
            text: "Clinic"
            font_size: 22
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1

        Button:
            text: "Canteen"
            font_size: 22
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1

        Button:
            text: "Faculty"
            font_size: 22
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1

        Button:
            text: "Back"
            font_size: 20
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "search"


<LibraryScreen>:
    name: "library"

    canvas.before:
        Color:
            rgba: 0.95, 1, 0.95, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        spacing: 8
        padding: 10

        Label:
            text: "NORMI DEEN CAMPUS LIBRARY"
            font_size: 27
            bold: True
            color: 0, 0.5, 0.2, 1
            size_hint_y: None
            height: 50

        Label:
            text: "Campus Library"
            font_size: 18
            color: 0, 0.5, 0.2, 1
            size_hint_y: None
            height: 35

        Image:
            id: library_image
            source: "library_1.png"
            allow_stretch: True
            keep_ratio: True

        Label:
            id: library_label
            text: "Library Route 1"
            font_size: 18
            color: 0, 0.5, 0.2, 1
            size_hint_y: None
            height: 35

        BoxLayout:
            size_hint_y: None
            height: 55
            spacing: 10

            Button:
                text: "← Previous"
                font_size: 18
                background_color: (0, 0.6, 0.2, 1)
                color: 1, 1, 1, 1
                on_release:
                    root.previous_library()

            Button:
                text: "Next →"
                font_size: 18
                background_color: (0, 0.6, 0.2, 1)
                color: 1, 1, 1, 1
                on_release:
                    root.next_library()

        Button:
            text: "School Library Info"
            font_size: 18
            size_hint_y: None
            height: 50
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                root.show_map()

        Button:
            text: "Back to Facilities"
            font_size: 20
            size_hint_y: None
            height: 55
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "facilities"


<ComputerLabScreen>:
    name: "computer_lab"
    
    canvas.before:
        Color:
            rgba: 0.95, 1, 0.95, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        spacing: 8
        padding: 10

        Label:
            text: "ICT / COMPUTER LABORATORY"
            font_size: 27
            bold: True
            color: 0, 0.5, 0.2, 1
            size_hint_y: None
            height: 50

        Label:
            id: route_label
            text: "Route 1 of 6"
            font_size: 18
            color: 0, 0.5, 0.2, 1
            size_hint_y: None
            height: 35

        Image:
            id: route_image
            source: "route_1.png"
            allow_stretch: True
            keep_ratio: True

        BoxLayout:
            size_hint_y: None
            height: 55
            spacing: 10

            Button:
                text: "← Previous"
                font_size: 18
                background_color: (0, 0.6, 0.2, 1)
                on_release:
                    root.previous_route()

            Button:
                text: "Next →"
                font_size: 18
                background_color: (0, 0.6, 0.2, 1)
                on_release:
                    root.next_route()

        Button:
            text: "Computer Lab Info"
            font_size: 18
            size_hint_y: None
            height: 50
            background_color: (0, 0.6, 0.2, 1)
            on_release:
                root.show_map()

        Button:
            text: "Back to Facilities"
            font_size: 20
            size_hint_y: None
            height: 55
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "facilities"
                

<CampusMapScreen>:
    name: "CampusMap"

    canvas.before:
        Color:
            rgba: 0.95, 1, 0.95, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        spacing: 10
        padding: 10

        Label:
            text: "NORMI DEEN CAMPUS MAP"
            font_size: 28
            bold: True
            color: 0, 0.5, 0.2, 1
            size_hint_y: None
            height: 50

        Image:
            source: "sheet2.png"
            allow_stretch: True
            keep_ratio: True

        Button:
            text: "Back "
            font_size: 20
            size_hint_y: None
            height: 55
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "search" 
                
                
<AboutScreen>:
    name: "about"

    canvas.before:
        Color:
            rgba: 0.95, 1, 0.95, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        spacing: 10
        padding: 20

        Label:
            text: "Campus Navigation Prototype\\\\nCapstone Project"
            font_size: 24
            color: 0, 0.5, 0.2, 1

        Label:
            text: "This application is a campus navigation prototype designed to help students, faculty, staff, parents, and visitors locate selected facilities within NORMI Deen Campus. It provides facility information, visual route references, and a campus map for easier navigation and as a based reference for future developers"
            font_size: 25
            color: 0.15, 0.15, 0.15, 1
            text_size: self.width - 40, None
            halign: "center"
            valign: "middle"
            size_hint_y: None
            height: 150

        Button:
            text: "Back"
            font_size: 20
            background_color: (0, 0.6, 0.2, 1)
            color: 1, 1, 1, 1
            on_release:
                app.root.current = "home"
'''


class HomeScreen(Screen):
    pass


class SearchScreen(Screen):
    pass


class FacilitiesScreen(Screen):
    pass


class LibraryScreen(Screen):

    library_routes = [
        "library_1.png",
        "library_2.png",
        "library_3.png",
        "library_4.png",
        "library_5.png",
    ]

    current_library = 0

    def next_library(self):
        if self.current_library < len(self.library_routes) - 1:
            self.current_library += 1
            self.update_library()

    def previous_library(self):
        if self.current_library > 0:
            self.current_library -= 1
            self.update_library()

    def update_library(self):
        self.ids.library_image.source = self.library_routes[self.current_library]
        self.ids.library_label.text = (
            f"Library Route {self.current_library + 1} "
            f"of {len(self.library_routes)}"
        )

    def show_map(self):
        self.ids.library_image.source = "sheet1.jpg"
        self.ids.library_label.text = "Campus Evacuation Map"


class ComputerLabScreen(Screen):

    routes = [
        "route_1.png",
        "route_2.png",
        "route_3.png",
        "route_4.png",
        "route_5.png",
        "route_6.png",
    ]

    current_route = 0

    def next_route(self):
        if self.current_route < len(self.routes) - 1:
            self.current_route += 1
            self.update_route()

    def previous_route(self):
        if self.current_route > 0:
            self.current_route -= 1
            self.update_route()

    def update_route(self):
        self.ids.route_image.source = self.routes[self.current_route]
        self.ids.route_label.text = (
            f"Route {self.current_route + 1} of {len(self.routes)}"
        )

    def show_map(self):
        self.ids.route_image.source = "sheet1.jpg"
        self.ids.route_label.text = "Campus Map"


class AboutScreen(Screen):
    pass
    
    
class CampusMapScreen(Screen):
    pass    


class NavigationApp(App):

    def build(self):
        return Builder.load_string(KV)


NavigationApp().run()